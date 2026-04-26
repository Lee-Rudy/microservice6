from project.dtos.second_degre_dto import SecondDegreDTO, SecondDegreResultDTO


def test_second_degre_dto_model():
    payload = SecondDegreDTO(a=1.0, b=-3.0, c=2.0)

    assert payload.a == 1.0
    assert payload.b == -3.0
    assert payload.c == 2.0


def test_second_degre_result_dto_model():
    result = SecondDegreResultDTO(
        discriminant=1.0,
        solutions=[1.0, 2.0],
        has_real_solutions=True,
    )

    assert result.discriminant == 1.0
    assert result.solutions == [1.0, 2.0]
    assert result.has_real_solutions is True
