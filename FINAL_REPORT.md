# DevOps Mini API - Final Report

**Student**: Mahdi Jenhani  
**Project**: DevOps End-to-End Pipeline  
**Date**: January 17, 2026

---

## 1. Project Overview

This project demonstrates a complete DevOps lifecycle for a REST API, covering development, containerization, automation, security, observability, and orchestration. The goal was to implement industry-standard DevOps practices on a small-scale application (under 150 lines of code).

**GitHub Repository**: https://github.com/M-Jenhani/devops-mini-api  
**Docker Hub Image**: https://hub.docker.com/r/mahdij8/devops-api

---

## 2. Architecture

### 2.1 Application Architecture

The application is a **FastAPI-based REST API** with the following components:

- **Backend Service**: Python FastAPI exposing 4 endpoints (`/health`, `/items` GET/POST, `/metrics`)
- **Observability Layer**: Prometheus metrics, structured logging, request tracing middleware
- **Containerization**: Docker container running on Python 3.10 slim image
- **Orchestration**: Kubernetes deployment with 1 replica and NodePort service

### 2.2 DevOps Pipeline Architecture

```
Developer → Git Push → GitHub Actions → Build & Test → SAST Scan → Docker Build
                                                                         ↓
                                                              Docker Hub Registry
                                                                         ↓
                                                              Kubernetes Cluster
                                                                         ↓
                                                              Running Application
```

**Flow**:
1. Code pushed to GitHub triggers CI/CD pipeline
2. Automated tests run (pytest)
3. Security scan (Bandit) validates code
4. Docker image built and pushed to Docker Hub
5. Kubernetes pulls image and deploys service
6. Application accessible via port-forwarding

---

## 3. Tools & Technologies

| Component          | Tool/Technology      | Justification                                      |
|--------------------|----------------------|---------------------------------------------------|
| **Backend**        | FastAPI              | Lightweight, fast, modern Python framework        |
| **Testing**        | pytest               | Industry standard for Python testing              |
| **Containerization** | Docker            | De facto standard for application packaging       |
| **Orchestration**  | Kubernetes (Minikube)| Production-grade container orchestration          |
| **CI/CD**          | GitHub Actions       | Integrated with repository, easy configuration    |
| **SAST**           | Bandit               | Python-specific static security analyzer          |
| **DAST**           | OWASP ZAP            | Industry-standard dynamic security testing        |
| **Metrics**        | Prometheus           | Standard for cloud-native monitoring              |
| **Registry**       | Docker Hub           | Public container registry for image storage       |

---

## 4. Implementation Details

### 4.1 Backend Functionality (10%)

**Code**: [app/main.py](app/main.py) (~80 lines)

The API implements:
- ✅ RESTful endpoints (GET, POST)
- ✅ In-memory data storage
- ✅ Health check endpoint
- ✅ Metrics exposure
- ✅ Request logging and tracing middleware

**Testing**: Unit tests with 100% endpoint coverage using FastAPI's TestClient.

### 4.2 GitHub Workflow (10%)

**Implementation**:
- ✅ Created 7 GitHub Issues for project tracking
- ✅ Each issue mapped to a dedicated feature branch
- ✅ Pull Requests created for all major changes
- ✅ Peer review process followed (constructive feedback)
- ✅ All PRs merged to main after review

**Branches Created**:
- `issue-3-docker` - Containerization
- `issue-4-cicd` - CI/CD pipeline
- `issue-5-dast` - Security scanning
- `issue-6-kubernetes` - K8s deployment
- `issue-7-documentation` - Documentation

### 4.3 CI/CD Pipeline (15%)

**Configuration**: [.github/workflows/ci.yml](.github/workflows/ci.yml)

**Pipeline Stages**:
1. **Checkout**: Pull latest code
2. **Setup**: Install Python 3.10
3. **Dependencies**: Install requirements + testing tools
4. **Test**: Run pytest test suite
5. **SAST**: Execute Bandit security scan

**Triggers**: Automated on push and pull request events

**Results**: ✅ All builds passing successfully

### 4.4 Containerization (10%)

**Dockerfile**: [Dockerfile](Dockerfile)

**Features**:
- Multi-stage build for optimization
- Python 3.10 slim base image
- Non-root user execution
- Port 8000 exposed
- Health check included

**Published Image**: `mahdij8/devops-api:latest`  
**Size**: ~150 MB  
**Pulls**: Available publicly on Docker Hub

**Docker Compose**: Could be added for multi-container setups (future enhancement)

### 4.5 Observability (15%)

#### Metrics
- **Tool**: Prometheus client library
- **Endpoint**: `/metrics`
- **Metrics Exposed**:
  - `request_count`: Total API requests (Counter)
  - `request_duration_seconds`: Request latency (Histogram)
- **Format**: OpenMetrics compatible

#### Logs
- **Implementation**: Python's logging module
- **Format**: Structured logs with timestamp, level, message
- **Content**: HTTP method, path, status code for each request
- **Example**: `INFO:root:GET /health`

#### Tracing
- **Implementation**: Custom middleware
- **Functionality**: Captures request start/end time, calculates duration
- **Future Enhancement**: OpenTelemetry integration for distributed tracing

### 4.6 Security (10%)

#### SAST (Static Application Security Testing)
- **Tool**: Bandit
- **Integration**: Automated in GitHub Actions CI pipeline
- **Scope**: Scans all Python files (excluding tests)
- **Results**: ✅ No high or medium severity issues found
- **False Positives**: Test assertions flagged (excluded from scan)

#### DAST (Dynamic Application Security Testing)
- **Tool**: OWASP ZAP Baseline Scan
- **Method**: Scanned running API container
- **Results**:
  - ✅ **66 security checks passed**
  - ⚠️ **1 low-severity warning** (cacheable content - expected behavior)
  - ❌ **0 critical vulnerabilities**
- **Report**: [zap-report.txt](zap-report.txt)

### 4.7 Kubernetes Deployment (10%)

**Manifests**:
- **Deployment**: [k8s/deployment.yaml](k8s/deployment.yaml)
  - 1 replica
  - Container: `mahdij8/devops-api:latest`
  - Port: 8000
- **Service**: [k8s/service.yaml](k8s/service.yaml)
  - Type: NodePort
  - Port mapping: 8000 → 30000

**Platform**: Minikube (local Kubernetes cluster)

**Access Method**: Port-forwarding via `kubectl port-forward service/devops-api 8080:8000`

**Status**: ✅ Successfully deployed and accessible at `http://localhost:8080`

**Verification**:
```bash
$ kubectl get pods
NAME                         READY   STATUS    RESTARTS   AGE
devops-api-859b4dc78-qcjjm   1/1     Running   0          5m

$ kubectl get services
NAME         TYPE        CLUSTER-IP      PORT(S)
devops-api   NodePort    10.111.27.253   8000:30000/TCP
```

---

## 5. Deliverables Checklist

| # | Deliverable                              | Status | Evidence                          |
|---|------------------------------------------|--------|-----------------------------------|
| 1 | GitHub repository with source code       | ✅     | https://github.com/M-Jenhani/devops-mini-api |
| 2 | Functioning CI/CD pipeline               | ✅     | .github/workflows/ci.yml          |
| 3 | Published Docker image                   | ✅     | mahdij8/devops-api on Docker Hub  |
| 4 | Service deployed locally                 | ✅     | Kubernetes on Minikube            |
| 5 | Observability evidence                   | ✅     | /metrics endpoint, logs, tracing  |
| 6 | Security scan results (SAST + DAST)      | ✅     | Bandit + ZAP reports              |
| 7 | Documentation (README.md)                | ✅     | Comprehensive setup guide         |
| 8 | Final report                             | ✅     | This document                     |

---

## 6. Challenges & Solutions

### Challenge 1: httpx Missing Dependency
**Problem**: TestClient failed in CI pipeline due to missing `httpx` package.  
**Solution**: Added `httpx` to `requirements.txt`. Lesson: Always test CI configuration with complete dependencies.

### Challenge 2: Bandit False Positives
**Problem**: Bandit flagged test assertions (`assert`) as security issues.  
**Solution**: Excluded test files from Bandit scan using `--exclude` flag. Lesson: Configure security tools to match project context.

### Challenge 3: Minikube SSH Tunnel Error
**Problem**: `minikube service` command failed due to missing SSH in Windows PATH.  
**Solution**: Used `kubectl port-forward` as an alternative access method. Lesson: Multiple approaches exist for accessing Kubernetes services.

### Challenge 4: OWASP ZAP Image Not Found
**Problem**: Original ZAP Docker image name was outdated.  
**Solution**: Used updated image name `zaproxy/zap-stable` and `host.docker.internal` for Windows Docker networking. Lesson: Container image names evolve; check official documentation.

---

## 7. Lessons Learned

### Technical Lessons
1. **Docker Networking**: Container-to-host communication requires special hostnames (`host.docker.internal` on Windows)
2. **Kubernetes Access**: Port-forwarding is more reliable than tunneling for local development
3. **CI/CD Testing**: Always run the full pipeline locally before pushing to ensure dependencies are complete
4. **Security Tool Configuration**: Static analysis tools need tuning to avoid false positives

### DevOps Best Practices
1. **Issue-Driven Development**: Breaking work into small, tracked issues improves organization and progress visibility
2. **Branch-Per-Feature**: Dedicated branches for each feature enable clean history and easy rollbacks
3. **Automated Testing**: CI pipeline catches issues early, before they reach production
4. **Infrastructure as Code**: Kubernetes manifests enable reproducible deployments

### Process Improvements
1. **Documentation Early**: Writing README incrementally would have saved time at the end
2. **Peer Review Value**: External feedback catches issues self-review misses
3. **Observability Planning**: Designing metrics/logging upfront is easier than retrofitting

---

## 8. Future Enhancements

### Short-term Improvements
- Add Docker Compose for local multi-service development
- Implement health check probes in Kubernetes deployment
- Add Grafana dashboards for metrics visualization
- Expand test coverage to include edge cases

### Long-term Goals
- **Cloud Deployment**: Deploy to AWS EKS or Google GKE
- **Distributed Tracing**: Full OpenTelemetry integration
- **Database Integration**: Add PostgreSQL for persistent storage
- **Advanced CI/CD**: Multi-environment deployments (dev/staging/prod)
- **Monitoring Alerts**: Prometheus Alertmanager for incident response

---

## 9. Conclusion

This project successfully demonstrates an end-to-end DevOps workflow, from code development through deployment and monitoring. All project objectives were achieved:

- ✅ Backend service implemented (under 150 lines)
- ✅ GitHub workflow with issues, PRs, and peer reviews
- ✅ Automated CI/CD pipeline with testing and security scans
- ✅ Containerized application published to Docker Hub
- ✅ Kubernetes deployment with local accessibility
- ✅ Observability with metrics, logs, and tracing
- ✅ Security validation via SAST and DAST
- ✅ Comprehensive documentation

The project reinforces the importance of automation, security, and observability in modern software development. The skills gained—including Docker, Kubernetes, CI/CD, and security scanning—are directly applicable to real-world DevOps engineering roles.

**Key Takeaway**: DevOps is not just about tools, but about building reliable, secure, and observable systems through automation and continuous improvement.

---

## 10. References

- FastAPI Documentation: https://fastapi.tiangolo.com/
- Docker Documentation: https://docs.docker.com/
- Kubernetes Documentation: https://kubernetes.io/docs/
- GitHub Actions Documentation: https://docs.github.com/en/actions
- Prometheus Documentation: https://prometheus.io/docs/
- OWASP ZAP: https://www.zaproxy.org/
- Bandit Security: https://bandit.readthedocs.io/

---

**End of Report**