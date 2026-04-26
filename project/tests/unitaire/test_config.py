from project.config import Settings


def test_settings_database_url_default(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)

    settings = Settings()

    assert "postgresql+psycopg" in settings.database_url


def test_settings_database_url_from_env(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")

    settings = Settings()

    assert settings.database_url == "sqlite:///test.db"
