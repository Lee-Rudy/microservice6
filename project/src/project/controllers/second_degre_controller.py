from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from project.domains.second_degre import SecondDegre
from project.dtos.second_degre_dto import SecondDegreDTO, SecondDegreResultDTO

router = APIRouter(prefix="/degre", tags=["degre"])


@router.post("/calculer", response_model=SecondDegreResultDTO)
def calculer_second_degre(payload: SecondDegreDTO) -> SecondDegreResultDTO:
    """Calcule les solutions d'une équation de second degré.

    Règles:
    - valide les coefficients selon la logique métier (`domains.SecondDegre`)
    - calcule le discriminant
    - détermine les solutions réelles
    - retourne les résultats
    """

    try:
        equation = SecondDegre(a=payload.a, b=payload.b, c=payload.c)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))

    discriminant = equation.discriminant()
    solutions = equation.solutions()
    has_real_solutions = equation.has_no_real_solution() is False

    return SecondDegreResultDTO(
        discriminant=discriminant,
        solutions=list(solutions),
        has_real_solutions=has_real_solutions
    )

