from __future__ import annotations

import re
from typing import Optional, Tuple

"""
Logique métier d'une équation de second degré
- a ne peut pas être nul
- les coefficients doivent être des nombres réels
- on peut calculer le discriminant et les solutions
- on gère les cas sans solution réelle
"""


class SecondDegre:
    COEFFICIENT_PATTERN = re.compile(r"^-?\d+(?:\.\d+)?$")

    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = self._validate_coefficient(a, "a")
        self.b = self._validate_coefficient(b, "b")
        self.c = self._validate_coefficient(c, "c")
        self._validate_equation()

    @classmethod
    def from_strings(cls, a: str, b: str, c: str) -> SecondDegre:
        return cls(
            cls._parse_number(a, "a"),
            cls._parse_number(b, "b"),
            cls._parse_number(c, "c"),
        )

    @classmethod
    def _parse_number(cls, value: str, name: str) -> float:
        if value is None:
            raise ValueError(f"Le coefficient {name} est requis.")

        text = value.strip()
        if not text:
            raise ValueError(f"Le coefficient {name} ne peut pas être vide.")

        if not cls.COEFFICIENT_PATTERN.match(text):
            raise ValueError(
                f"Le coefficient {name} doit être un nombre valide."
            )

        return float(text)

    @staticmethod
    def _validate_coefficient(value: float, name: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Le coefficient {name} doit être un nombre.")

        if name == "a" and float(value) == 0:
            raise ValueError(
                "Le coefficient a ne peut pas être zéro pour une équation de second degré."
            )

        return float(value)

    def _validate_equation(self) -> None:
        if self.a == 0:
            raise ValueError(
                "L'équation doit rester de second degré : a ne peut pas être nul."
            )

    def discriminant(self) -> float:
        return self.b * self.b - 4 * self.a * self.c

    def has_two_solutions(self) -> bool:
        return self.discriminant() > 0

    def has_one_solution(self) -> bool:
        return self.discriminant() == 0

    def has_no_real_solution(self) -> bool:
        return self.discriminant() < 0

    def solutions(self) -> Tuple[Optional[float], Optional[float]]:
        delta = self.discriminant()

        if delta < 0:
            return None, None

        sqrt_delta = delta**0.5
        x1 = (-self.b - sqrt_delta) / (2 * self.a)
        x2 = (-self.b + sqrt_delta) / (2 * self.a)

        if delta == 0:
            return x1, x1

        return x1, x2

    def to_dict(self) -> dict[str, float]:
        return {"a": self.a, "b": self.b, "c": self.c}
