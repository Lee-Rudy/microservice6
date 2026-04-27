import pytest

from project.domains.validator import (
    InvalidValueError,
    validate_sensor_reading,
)


def test_validate_unknown_sensor_returns_unknown_level():
    result = validate_sensor_reading("not-a-sensor", 1.0)
    assert result.valid is False
    assert result.level == "unknown"
    assert result.message == "Capteur non répertorié"
    assert result.sensor is None


def test_validate_value_type_error_raises_invalidvalueerror():
    with pytest.raises(InvalidValueError):
        validate_sensor_reading("co2", "abc")  # type: ignore[arg-type]


def test_validate_moderate_boundary_is_moderate():
    result = validate_sensor_reading("co2", 800.0)
    assert result.valid is True
    assert result.level == "moderate"
    assert result.threshold == 800.0


def test_validate_critical_boundary_is_critical():
    result = validate_sensor_reading("co2", 1000.0)
    assert result.valid is False
    assert result.level == "critical"
    assert result.threshold == 1000.0
