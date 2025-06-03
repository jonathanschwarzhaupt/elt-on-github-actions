from extract.main import main


def test_main_without_env_variable(capsys, monkeypatch):
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    assert main() == "Starting extraction in environment: default"


def test_main_with_env_variable(capsys, monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "production")
    assert main() == "Starting extraction in environment: production"
