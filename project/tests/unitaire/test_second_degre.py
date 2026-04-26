import pytest

from project.domains.second_degre import SecondDegre


def test_discriminant_and_solutions_two_solutions():
    equation = SecondDegre(1, -3, 2)

    assert equation.discriminant() == 1.0
    assert equation.has_two_solutions()
    assert equation.has_no_real_solution() is False
    assert equation.solutions() == (1.0, 2.0)


def test_discriminant_and_solutions_one_solution():
    equation = SecondDegre(1, 2, 1)

    assert equation.discriminant() == 0.0
    assert equation.has_one_solution()
    assert equation.solutions() == (-1.0, -1.0)


def test_no_real_solutions():
    equation = SecondDegre(1, 0, 1)

    assert equation.discriminant() == -4.0
    assert equation.has_no_real_solution()
    assert equation.solutions() == (None, None)


def test_zero_a_raises_value_error():
    with pytest.raises(ValueError, match="a ne peut pas être zéro"):
        SecondDegre(0, 2, 1)


def test_non_numeric_coefficient_raises_type_error():
    with pytest.raises(TypeError, match="doit être un nombre"):
        SecondDegre("1", 2, 1)


def test_from_strings_converts_valid_values():
    equation = SecondDegre.from_strings("2", "-5.5", "3")

    assert equation.a == 2.0
    assert equation.b == -5.5
    assert equation.c == 3.0


def test_from_strings_rejects_none():
    with pytest.raises(ValueError, match="requis"):
        SecondDegre.from_strings(None, "1", "1")


def test_from_strings_rejects_empty_string():
    with pytest.raises(ValueError, match="ne peut pas être vide"):
        SecondDegre.from_strings("1", "", "1")


def test_from_strings_rejects_invalid_number():
    with pytest.raises(ValueError, match="nombre valide"):
        SecondDegre.from_strings("1", "a", "1")


def test_to_dict_includes_coefficients():
    equation = SecondDegre(2, 1, -1)

    assert equation.to_dict() == {"a": 2.0, "b": 1.0, "c": -1.0}
