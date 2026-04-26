from __future__ import annotations

from pydantic import BaseModel, Field
from typing import List, Optional


class SecondDegreDTO(BaseModel):
    a: float = Field(..., description="Coefficient a de l'équation de second degré")
    b: float = Field(..., description="Coefficient b de l'équation de second degré")
    c: float = Field(..., description="Coefficient c de l'équation de second degré")

    class Config:
        schema_extra = {
            "example": {
                "a": 1.0,
                "b": -3.0,
                "c": 2.0
            }
        }


class SecondDegreResultDTO(BaseModel):
    discriminant: float = Field(..., description="Le discriminant de l'équation")
    solutions: List[Optional[float]] = Field(..., description="Les solutions réelles de l'équation")
    has_real_solutions: bool = Field(..., description="Indique si l'équation a des solutions réelles")

    class Config:
        schema_extra = {
            "example": {
                "discriminant": 1.0,
                "solutions": [1.0, 2.0],
                "has_real_solutions": True
            }
        }

