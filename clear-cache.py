from contextlib import suppress
from pathlib import Path


def clean() -> None:
    with suppress(BaseException):
        for f in Path(".").rglob("*.py[cod]"):
            f.unlink(missing_ok=True)
        for d in Path(".").rglob("__pycache__"):
            d.rmdir()


def main() -> None:
    clean()


if __name__ == "__main__":
    raise SystemExit(main())
