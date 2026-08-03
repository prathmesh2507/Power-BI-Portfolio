from fastapi import FastAPI

app = FastAPI(
    title="Global Investment Intelligence Platform",
    description="Enterprise-grade backend for global financial data engineering",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to GIIP Backend",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
