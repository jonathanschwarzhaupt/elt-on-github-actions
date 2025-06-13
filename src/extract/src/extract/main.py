import os
import sys


def main() -> None:
    """Entry point for running the programm"""

    # Comment to trigger CI
    env = os.getenv("ENVIRONMENT", "default")
    print(f"Starting extraction in environment: {env}")


if __name__ == "__main__":
    main()

    sys.exit(0)
