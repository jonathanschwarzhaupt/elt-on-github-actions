import os
import sys


def main() -> str:
    """Entry point for running the programm"""

    env = os.getenv("ENVIRONMENT", "default")
    return f"Starting extraction in environment: {env}"


if __name__ == "__main__":
    print(main())

    sys.exit(0)
