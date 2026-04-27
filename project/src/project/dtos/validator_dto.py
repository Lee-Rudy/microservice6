from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


class SensorReadingDTO(BaseModel):
    sensor: str = Field(..., description="Nom du capteur (ex: co2, temperature)")
    value: float = Field(..., description="Valeur mesurée")

    model_config = {
        "json_schema_extra": {
            "example": {"sensor": "co2", "value": 500.0}
        }
    }


class ValidationResponseDTO(BaseModel):
    valid: bool
    level: Literal["normal", "moderate", "critical", "unknown"]
    sensor: Optional[str] = None
    value: Optional[float] = None
    threshold: Optional[float] = None
    timestamp: Optional[str] = None
    message: Optional[str] = None

