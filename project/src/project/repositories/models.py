from __future__ import annotations

from datetime import datetime
from sqlalchemy import Float, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from project.repositories.database import Base


class DeltaModel(Base):
    """Représentation en base de données d'une équation du second degré.

    Stocke les coefficients (a, b, c) pour permettre le recalcul
    du discriminant et des solutions.
    """

    __tablename__ = "delta"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # Utilisation de Float (équivalent DOUBLE PRECISION dans PostgreSQL)
    coeff_a: Mapped[float] = mapped_column(
        Float(precision=53),
        nullable=False,
    )

    coeff_b: Mapped[float] = mapped_column(
        Float(precision=53),
        nullable=False,
    )

    coeff_c: Mapped[float] = mapped_column(
        Float(precision=53),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    def __repr__(self) -> str:
        return (
            f"<DeltaModel(id={self.id}, a={self.coeff_a}, b={self.coeff_b}, c={self.coeff_c})>"
        )