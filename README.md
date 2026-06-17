# 🎬 IMDb Rating Prediction Platform

## End-to-End Production MLOps Pipeline with Kubernetes, GitOps, CI/CD, Monitoring & Model Versioning

![MLOps](https://img.shields.io/badge/MLOps-Production%20Ready-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-blue)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Automated-success)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-red)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-yellow)

---

# 📌 Project Overview

This project demonstrates a **Production-Grade End-to-End MLOps Platform** for IMDb Rating Prediction.

The entire machine learning lifecycle is automated using modern DevOps and MLOps practices, including:

* Data Processing
* Model Training
* Experiment Tracking
* Model Versioning
* Artifact Management
* API Deployment
* CI/CD Automation
* Kubernetes Orchestration
* GitOps Deployment
* Monitoring & Observability

The objective of this project is to simulate how machine learning systems are deployed and maintained in real-world enterprise environments.

---

# 🏗️ Solution Architecture

```text
IMDb Dataset
     │
     ▼
Data Preprocessing
     │
     ▼
Model Training
     │
     ▼
MLflow Experiment Tracking
     │
     ▼
Model Artifact (.pkl)
     │
     ▼
DVC Version Control
     │
     ▼
AWS S3 Remote Storage
     │
     ▼
FastAPI Inference Service
     │
     ▼
Docker Containerization
     │
     ▼
GitHub Actions CI/CD
     │
     ▼
Docker Hub Registry
     │
     ▼
Kubernetes Cluster (AWS EC2)
     │
     ▼
ArgoCD GitOps Deployment
     │
     ▼
Prometheus Monitoring
     │
     ▼
Grafana Dashboards
```

---

# 🎯 Key Features

### Machine Learning

* IMDb Rating Prediction Model
* Scikit-Learn Regression Pipeline
* Feature Engineering
* Automated Training Workflow

### Experiment Tracking

* MLflow Integration
* Parameter Tracking
* Metrics Tracking
* Model Artifact Logging

### Data & Model Versioning

* DVC Integration
* AWS S3 Remote Storage
* Reproducible Model Management

### API Development

* FastAPI-based Prediction Service
* RESTful API Endpoints
* Health Checks
* Metrics Exposure

### Containerization

* Dockerized Application
* Portable Deployments
* Environment Consistency

### CI/CD Automation

* GitHub Actions Pipeline
* Automated Docker Builds
* Docker Hub Push Automation
* Deployment Manifest Updates

### Kubernetes Deployment

* Kubernetes Deployments
* Services
* Self-Healing Pods
* Scalable Architecture

### GitOps Automation

* ArgoCD Integration
* Automated Synchronization
* Continuous Delivery
* Version-Controlled Deployments

### Monitoring & Observability

* Prometheus Metrics Collection
* Grafana Dashboards
* Application Monitoring
* Request Tracking

---

# 🧠 Machine Learning Workflow

## Dataset

IMDb Movies Dataset

## Features

* Release Year
* Runtime
* Number of Votes

## Target

IMDb Movie Rating Prediction

## Model

Scikit-Learn Regression Model

## Output Artifact

models/movie_rating_model.pkl

---

# 🌐 FastAPI Endpoints

## Health Check

```http
GET /
```

## Prediction Endpoint

```http
POST /predict
```

### Request Example

```json
{
  "year": 2020,
  "runtime_minutes": 120,
  "num_votes": 50000
}
```

### Response Example

```json
{
  "predicted_rating": 7.8
}
```

## Metrics Endpoint

```http
GET /metrics
```

Used by Prometheus for application monitoring.

---

# 🐳 Docker

## Build Image

```bash
docker build -t imdb-rating-api .
```

## Run Container

```bash
docker run -p 8000:8000 imdb-rating-api
```

---

# ⚙️ CI/CD Pipeline

The GitHub Actions workflow automates:

* Source Code Checkout
* Docker Image Build
* Docker Hub Push
* Kubernetes Manifest Update
* Automatic Commit
* Continuous Deployment Trigger

### Workflow

```text
Developer Push
      │
      ▼
GitHub Actions
      │
      ▼
Docker Build
      │
      ▼
Docker Hub Push
      │
      ▼
Manifest Update
      │
      ▼
GitHub Repository
      │
      ▼
ArgoCD Sync
      │
      ▼
Kubernetes Deployment
```

---

# ☸️ Kubernetes Deployment

Resources Used:

* Deployment
* Service
* Namespace
* Configurations

### Benefits

* Auto Recovery
* High Availability
* Scalability
* Production Deployment

---

# 🔁 GitOps with ArgoCD

ArgoCD continuously monitors the Git repository.

Whenever a deployment manifest changes:

```text
Git Push
    │
    ▼
ArgoCD Detects Change
    │
    ▼
Automatic Synchronization
    │
    ▼
Kubernetes Updated
```

### Advantages

* Fully Automated Deployments
* No Manual kubectl Apply
* Git as Single Source of Truth

---

# 📊 Monitoring Stack

## Prometheus

Collects:

* HTTP Request Metrics
* API Latency
* Application Metrics
* System Metrics

## Grafana

Visualizes:

* Request Traffic
* API Performance
* Resource Usage
* Service Health

---

# ☁️ Cloud Infrastructure

### AWS EC2

Hosts Kubernetes Cluster

### AWS S3

Stores DVC Versioned Artifacts

### Docker Hub

Stores Container Images

---

# 🛠️ Technology Stack

| Category            | Tools          |
| ------------------- | -------------- |
| Programming         | Python         |
| ML Framework        | Scikit-Learn   |
| Experiment Tracking | MLflow         |
| Versioning          | DVC            |
| Storage             | AWS S3         |
| API                 | FastAPI        |
| Containerization    | Docker         |
| CI/CD               | GitHub Actions |
| Registry            | Docker Hub     |
| Orchestration       | Kubernetes     |
| GitOps              | ArgoCD         |
| Monitoring          | Prometheus     |
| Dashboards          | Grafana        |
| Cloud               | AWS EC2        |

---

# 🚀 Skills Demonstrated

* Machine Learning Engineering
* MLOps
* DevOps
* Kubernetes
* GitOps
* CI/CD
* Cloud Computing
* Monitoring & Observability
* Containerization
* Infrastructure Automation

---

# 📈 Project Impact

This project showcases how modern machine learning systems are:

* Built
* Versioned
* Tracked
* Containerized
* Deployed
* Monitored
* Automated

using industry-standard tools and cloud-native practices.

---

# 👨‍💻 Author

**Venkatesh Pinjala**


---

⭐ If you found this project useful, consider giving it a star.
