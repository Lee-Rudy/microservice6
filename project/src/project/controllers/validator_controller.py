from __future__ import annotations

from dataclasses import asdict

from fastapi import APIRouter, HTTPException, status

from project.domains.validator import InvalidValueError, validate_sensor_reading
from project.dtos.validator_dto import SensorReadingDTO, ValidationResponseDTO

router = APIRouter(tags=["validate"])

# code avec la correction après sonarcloud
@router.post(
    "/validate",
    status_code=status.HTTP_200_OK,
)

# code avant la correction sonarcloud (ce code fonctionne)
# @router.post(
#     "/validate",
#     response_model=ValidationResponseDTO,
#     status_code=status.HTTP_200_OK,
# )

def validate(payload: SensorReadingDTO) -> ValidationResponseDTO:
    try:
        result = validate_sensor_reading(sensor=payload.sensor, value=payload.value)
        return ValidationResponseDTO(**asdict(result))
    except InvalidValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )

