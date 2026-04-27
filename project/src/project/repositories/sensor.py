from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SensorThreshold:
    moderate: float
    critical: float
    unit: str


THRESHOLDS: list[dict[str, object]] = [
    {"sensor": "co2", "moderate": 800.0, "critical": 1000.0, "unit": "ppm"},
    {"sensor": "temperature", "moderate": 35.0, "critical": 40.0, "unit": "°C"},
    {"sensor": "noise", "moderate": 70.0, "critical": 85.0, "unit": "dB"},
    {"sensor": "pm25", "moderate": 25.0, "critical": 50.0, "unit": "µg/m3"},
    {"sensor": "humidity", "moderate": 60.0, "critical": 80.0, "unit": "%"},
]

_INDEX: dict[str, SensorThreshold] = {
    str(item["sensor"]): SensorThreshold(
        moderate=float(item["moderate"]),
        critical=float(item["critical"]),
        unit=str(item["unit"]),
    )
    for item in THRESHOLDS
}


def get_threshold(sensor: str) -> SensorThreshold | None:
    if sensor is None:
        return None
    return _INDEX.get(sensor.strip().lower())
