# Zero-Downtime Deployment Platform

A hands-on DevOps capstone project demonstrating how to deploy application updates on Kubernetes using rolling deployments, health checks, container security, CI/CD, rollback, monitoring, and infrastructure-as-code concepts.

> **Implementation note:** The completed deployment is currently demonstrated locally using Docker Desktop Kubernetes. GitHub Actions performs application testing, Docker image builds, and Kubernetes manifest validation. AWS/EKS and ECR are documented as production extensions and are not claimed as completed infrastructure.

---

## Project Overview

The objective of this project is to solve a common production deployment problem:

> How can a new application version be released without intentionally taking the application offline?

The platform uses multiple Kubernetes replicas and a controlled RollingUpdate strategy. New Pods must become healthy before old Pods are removed, allowing application capacity to remain available during the deployment.

The project combines:

- FastAPI
- Python
- Docker
- Kubernetes
- GitHub Actions
- Kubernetes health probes
- Rolling deployments
- Rollback
- Kubernetes Service
- Ingress
- ConfigMap
- Horizontal Pod Autoscaler configuration
- Container security
- Prometheus
- Grafana
- Alertmanager
- Terraform
- Production troubleshooting

---

# Architecture

```mermaid
flowchart LR

    A[Developer] --> B[GitHub Repository]

    B --> C[GitHub Actions CI]
    C --> D[Python Tests]
    C --> E[Docker Build]

    B --> F[GitHub Actions CD]
    F --> G[Kubernetes Manifest Validation]

    E --> H[Docker Image]

    H --> I[Docker Desktop Kubernetes]

    I --> J[Kubernetes Deployment]

    J --> K[Pod 1]
    J --> L[Pod 2]
    J --> M[Pod 3]

    K --> N[Kubernetes Service]
    L --> N
    M --> N

    N --> O[Application Traffic]

    I --> P[Prometheus]
    P --> Q[Grafana]
    P --> R[Alertmanager]
