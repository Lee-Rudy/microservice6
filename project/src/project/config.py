from __future__ import annotations

import os


class Settings:
    """Configuration applicative.

    variables d'environnement attendues (avec valeurs par défaut) :
    - DATABASE_URL: URL SQLAlchemy (ex: postgresql+psycopg://user:pass@host:5432/db)

    """

    def __init__(self) -> None:
        self.database_url = os.getenv(
            "DATABASE_URL",
            "postgresql+psycopg://postgres:postgres@localhost:5432/db_ms6",
        )


settings = Settings()

