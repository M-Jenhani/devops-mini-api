# DevOps Mini API

A simple REST API demonstrating end-to-end DevOps practices including containerization, CI/CD, security scanning, observability, and Kubernetes deployment.

## 🚀 Project Overview

This project is a FastAPI-based REST API (under 150 lines of code) that demonstrates:
- **Backend Development**: Python FastAPI
- **Containerization**: Docker
- **CI/CD Pipeline**: GitHub Actions
- **Observability**: Prometheus metrics, structured logging, request tracing
- **Security**: SAST (Bandit) and DAST (OWASP ZAP) scanning
- **Orchestration**: Kubernetes deployment with Minikube

## 📋 Prerequisites

- **Python** 3.10+
- **Docker** (latest version)
- **Kubernetes Tools**: `kubectl` and `minikube`
- **Git**

## 🏗️ Project Structure

```
devops-mini-api/
├── app/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt      # Python dependencies
│   └── test_main.py         # Unit tests
├── k8s/
│   ├── deployment.yaml      # Kubernetes deployment
│   └── service.yaml         # Kubernetes service
├── .github/workflows/
│   └── ci.yml               # CI/CD pipeline
├── Dockerfile               # Container image definition
├── zap-report.txt           # DAST security scan results
└── README.md                # This file
```

## 🔧 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/M-Jenhani/devops-mini-api.git
cd devops-mini-api
```

### 2. Install Dependencies

```bash
cd app
pip install -r requirements.txt
```

## 🏃 Running Locally

### Start the API

```bash
cd app
uvicorn main:app --reload
```

The API will be available at: **http://localhost:8000**

### Test the API

```bash
# Health check
curl http://localhost:8000/health

# Get items
curl http://localhost:8000/items

# Add item
curl -X POST "http://localhost:8000/items?item=test"

# View metrics
curl http://localhost:8000/metrics
```

### Run Tests

```bash
pytest app/test_main.py
```

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t mahdij8/devops-api .
```

### Run Container

```bash
docker run -p 8000:8000 mahdij8/devops-api
```

Access the API at: **http://localhost:8000**

### Pull from Docker Hub

```bash
docker pull mahdij8/devops-api
docker run -p 8000:8000 mahdij8/devops-api
```

**Docker Hub**: [mahdij8/devops-api](https://hub.docker.com/r/mahdij8/devops-api)

## ☸️ Kubernetes Deployment

### Start Minikube

```bash
minikube start
```

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Verify Deployment

```bash
kubectl get pods
kubectl get services
```

### Access the API

```bash
kubectl port-forward service/devops-api 8080:8000
```

Access at: **http://localhost:8080/health**

### Clean Up

```bash
kubectl delete -f k8s/
minikube stop
```

## 🔄 CI/CD Pipeline

The project uses **GitHub Actions** for continuous integration and deployment:

- **Automated Testing**: Runs `pytest` on every push/PR
- **SAST Security Scan**: Bandit static analysis
- **Python Version**: 3.10
- **Trigger**: Push and Pull Request events

**View Pipeline**: [GitHub Actions](.github/workflows/ci.yml)

## 📊 Observability

### Metrics

Prometheus-compatible metrics exposed at `/metrics`:
- `request_count`: Total number of requests
- `request_duration_seconds`: Request latency histogram

### Logs

Structured logging for all requests:
- Request method and path
- Response time
- Error tracking

### Tracing

Basic request tracing via middleware:
- Captures request lifecycle
- Measures execution time

## 🔒 Security

### SAST (Static Application Security Testing)

**Tool**: Bandit

Automated security scanning in CI/CD pipeline to detect:
- SQL injection vulnerabilities
- Hardcoded credentials
- Insecure dependencies

### DAST (Dynamic Application Security Testing)

**Tool**: OWASP ZAP

Runtime security scanning results:
- ✅ 66 security checks passed
- ⚠️ 1 minor warning (cacheable content)
- ❌ 0 critical vulnerabilities

**Report**: [zap-report.txt](zap-report.txt)

## 🎯 API Endpoints

| Method | Endpoint   | Description              |
|--------|------------|--------------------------|
| GET    | `/health`  | Health check             |
| GET    | `/items`   | Retrieve all items       |
| POST   | `/items`   | Add a new item           |
| GET    | `/metrics` | Prometheus metrics       |

### Example Requests

```bash
# Health check
GET http://localhost:8000/health
Response: {"status": "ok"}

# Get items
GET http://localhost:8000/items
Response: []

# Add item
POST http://localhost:8000/items?item=example
Response: {"message": "item added"}

# View metrics
GET http://localhost:8000/metrics
Response: Prometheus format metrics
```

## 🛠️ Technologies Used

- **Backend**: FastAPI, Uvicorn
- **Testing**: pytest
- **Containerization**: Docker
- **Orchestration**: Kubernetes, Minikube
- **CI/CD**: GitHub Actions
- **Security**: Bandit (SAST), OWASP ZAP (DAST)
- **Observability**: Prometheus, Python logging
- **Version Control**: Git, GitHub

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)

## 👤 Author

**Mahdi Jenhani**
- GitHub: [@M-Jenhani](https://github.com/M-Jenhani)
- Docker Hub: [mahdij8](https://hub.docker.com/u/mahdij8)

## 📄 License

This project is created for educational purposes as part of a DevOps course.

---

**Project Status**: ✅ Complete