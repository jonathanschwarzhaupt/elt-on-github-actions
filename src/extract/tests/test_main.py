import runpy
import pytest
from extract.main import main


def test_main_default(monkeypatch, capsys):
    """
    ENVIRONMENT not set  →  message should contain 'default'
    """
    monkeypatch.delenv("ENVIRONMENT", raising=False)

    main()  # <-- prints the message
    captured = capsys.readouterr()

    assert captured.out.strip() == "Starting extraction in environment: default"


def test_main_custom(monkeypatch, capsys):
    """
    ENVIRONMENT=production  →  message should contain 'production'
    """
    monkeypatch.setenv("ENVIRONMENT", "production")

    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == "Starting extraction in environment: production"


def test_module_as_script(monkeypatch, capsys):
    """
    Execute the file via `python -m extract.main` (i.e. __name__ == "__main__")
    so the guard at the bottom of main.py is covered too.
    The script should exit with code 0 and still print the right line.
    """
    monkeypatch.setenv("ENVIRONMENT", "ci")

    # run_module will raise SystemExit because your __main__ block calls sys.exit(0)
    with pytest.raises(SystemExit) as excinfo:
        runpy.run_module("extract.main", run_name="__main__")

    # Ensure we exited cleanly
    assert excinfo.value.code == 0

    # First line on stdout is the message from main()
    out_lines = capsys.readouterr().out.strip().splitlines()
    assert out_lines[0] == "Starting extraction in environment: ci"
