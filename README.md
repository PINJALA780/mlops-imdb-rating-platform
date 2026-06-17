# 🎬 IMDb Rating Prediction — End-to-End Production MLOps Platform

# 📌 Project Overview

This project is a **production-grade end-to-end MLOps system** that automates the full machine learning lifecycle — from data ingestion to training, model tracking, containerization, CI/CD, Kubernetes deployment, GitOps, and monitoring.

It demonstrates real-world DevOps + ML engineering practices used in modern cloud-native systems.

---

# 🏗️ System Architecture

IMDb Dataset  
→ Data Preprocessing  
→ Model Training (Scikit-learn)  
→ MLflow Experiment Tracking  
→ Model Artifact (.pkl)  
→ FastAPI Service  
→ Docker Containerization  
→ GitHub Actions CI/CD Pipeline  
→ Docker Hub Registry  
→ Kubernetes Cluster (AWS EC2)  
→ ArgoCD (GitOps Continuous Deployment)  
→ Prometheus (Metrics Collection)  
→ Grafana (Visualization Dashboard)

---

# 🧠 Machine Learning Pipeline

## Dataset
IMDb movie dataset used for regression task.

## Features
- Year of release  
- Runtime  
- Number of votes  

## Model
- Scikit-learn regression model  
- Predicts IMDb rating  

## Output Artifact
models/movie_rating_model.pkl

---

# 🌐 FastAPI Service

## API Endpoints

### Health Check
GET /

### Prediction API
POST /predict

## Sample Request
{
  "year": 2020,
  "runtime_minutes": 120,
  "num_votes": 50000
}

## Sample Response
{
  "predicted_rating": 7.8
}

## Metrics Endpoint
/metrics (Prometheus scraping endpoint)

---

# 🐳 Docker Setup

## Build Docker Image
docker build -t imdb-rating-api .

## Run Container
docker run -p 8000:8000 imdb-rating-api

## Purpose
- Ensures environment consistency  
- Portable deployment across systems  
- Works locally and in Kubernetes  

---

# ⚙️ CI/CD Pipeline (GitHub Actions)

## Workflow Summary

This pipeline automates the entire deployment process:

✔ Code checkout  
✔ Docker image build  
✔ Push image to Docker Hub  
✔ Update Kubernetes deployment YAML  
✔ Commit updated manifests  
✔ Trigger automatic deployment  


# ☸️ Kubernetes Deployment

## Deployment
FastAPI application deployed in Kubernetes cluster.

## Service Type
NodePort service exposed externally.

## Access URL
http://<EC2-PUBLIC-IP>:30007

## Features
- Auto scaling  
- Self-healing pods  
- High availability  

---

# 🔁 GitOps with ArgoCD

## Setup
- ArgoCD installed on Kubernetes cluster  
- GitHub repository connected  
- Auto-sync enabled  

## Workflow
Git Push → ArgoCD detects changes → Kubernetes automatically updates deployment  

## Benefits
- No manual kubectl apply  
- Fully automated deployments  
- Version-controlled infrastructure  

---

# 📊 Monitoring & Observability

## Prometheus
Collects metrics such as:
- HTTP request counts  
- Latency  
- Application performance  

## Grafana
Provides dashboards for:
- API performance  
- Traffic monitoring  
- System health  

---

# 🔐 Infrastructure Used

- AWS EC2 (Kubernetes Cluster Node)  
- Docker (Containerization)  
- Docker Hub (Image Registry)  
- GitHub Actions (CI/CD Automation)  
- Kubernetes (Orchestration)  
- ArgoCD (GitOps Deployment)  
- Prometheus (Monitoring)  
- Grafana (Visualization)  

---

# 🚀 Key Features

✔ End-to-end ML lifecycle automation  
✔ Production-grade deployment architecture  
✔ CI/CD pipeline using GitHub Actions  
✔ Kubernetes orchestration  
✔ GitOps-based deployment (ArgoCD)  
✔ Monitoring & observability system  
✔ Scalable cloud-native design  

---

# 🧠 What This Project Demonstrates

This project demonstrates real-world engineering skills:

- Machine Learning Engineering  
- MLOps pipeline design  
- DevOps automation  
- Cloud deployment (AWS)  
- Kubernetes orchestration  
- CI/CD pipeline implementation  
- Observability and monitoring  
- Production system architecture  

---

# 👨‍💻 Author

Venkatesh Pinjala
