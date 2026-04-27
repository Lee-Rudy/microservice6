from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Literal

from project.repositories.sensor import SensorThreshold, get_threshold

Level = Literal["normal", "moderate", "critical", "unknown"]


class UnknownSensorError(ValueError):
    pass


class InvalidValueError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class ValidationResult:
    valid: bool
    level: Level
    sensor: str | None = None
    value: float | None = None
    threshold: float | None = None
    timestamp: str | None = None
    message: str | None = None


def _now_iso_z() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def validate_sensor_reading(sensor: str, value: float) -> ValidationResult:
    threshold = get_threshold(sensor)
    if threshold is None:
        return ValidationResult(
            valid=False,
            level="unknown",
            message="Capteur non répertorié",
        )

    numeric_value = _coerce_value(value)
    level, is_valid, used_threshold = _evaluate(numeric_value, threshold)

    return ValidationResult(
        valid=is_valid,
        level=level,
        sensor=sensor.strip().lower(),
        value=numeric_value,
        threshold=used_threshold,
        timestamp=_now_iso_z(),
    )


def _coerce_value(value: float) -> float:
    if not isinstance(value, (int, float)):
        raise InvalidValueError("La valeur doit être un nombre.")
    return float(value)


def _evaluate(value: float, threshold: SensorThreshold) -> tuple[Level, bool, float]:
    if value < threshold.moderate:
        return "normal", True, threshold.moderate
    if value < threshold.critical:
        return "moderate", True, threshold.moderate
    return "critical", False, threshold.critical
