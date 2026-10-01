from fastapi import FastAPI

APP_VERSION = "1.0.0"

app = FastAPI(
    title="Zero Downtime Deployment API",
    version=APP_VERSION,
    description="A production-style API for demonstrating zero-downtime deployments."
)


@app.get("/")
def root():
    return {
        "message": "Zero Downtime Deployment API",
        "version": APP_VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": APP_VERSION
    }


@app.get("/version")
def version():
    return {
        "version": APP_VERSION
    }


@app.get("/api/status")
def status():
    return {
        "application": "zero-downtime-deployment",
        "status": "running",
        "version": APP_VERSION
    }
