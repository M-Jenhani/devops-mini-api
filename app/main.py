from fastapi import FastAPI
import time
import logging
from prometheus_client import Counter, Histogram, generate_latest

app = FastAPI()

logging.basicConfig(level=logging.INFO)

REQUEST_COUNT = Counter("request_count", "Total HTTP requests")
REQUEST_TIME = Histogram("request_duration_seconds", "Request duration")

items = []

@app.middleware("http")
async def metrics_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    REQUEST_COUNT.inc()
    REQUEST_TIME.observe(time.time() - start)
    logging.info(f"{request.method} {request.url.path}")
    return response

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def add_item(item: str):
    items.append(item)
    return {"message": "item added"}

@app.get("/metrics")
def metrics():
    return generate_latest()

