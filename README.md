# Zero-Downtime Deployment Platform

A production-style DevOps project demonstrating how to deploy application updates on Kubernetes with minimal service disruption using rolling deployments, health checks, container security, CI/CD validation, autoscaling configuration, and monitoring.

## Project Overview

The goal of this project is to build a deployment platform where a new application version can be released without intentionally taking the application offline.

The platform demonstrates:

- Containerized FastAPI application
- Docker image hardening
- Kubernetes rolling deployments
- Readiness and liveness probes
- Kubernetes resource requests and limits
- Horizontal Pod Autoscaler configuration
- Kubernetes Service
- Ingress configuration
- ConfigMap
- Container security controls
- GitHub Actions CI
- GitHub Actions Kubernetes manifest validation
- Prometheus monitoring
- Grafana visualization
- Alertmanager
- Rollback testing
- Terraform infrastructure-as-code scaffold

## Architecture

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
