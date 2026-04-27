from __future__ import annotations

from fastapi import FastAPI

from project.controllers.validator_controller import router as validator_controller

app = FastAPI(
    title="MS6 Service API",
    version="0.1.0",
    description="Microservice 6",
)

app.include_router(validator_controller)


@app.get("/", tags=["system"])
def root():
    return {"status": "ms6"}


@app.get("/health", tags=["system"])
def health():
    return {"status": "healthy"}
