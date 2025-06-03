import os


def main() -> str:
    """Entry point for running the programm"""

    env = os.getenv("ENVIRONMENT", "default")
    return f"Starting extraction in environment: {env}"


# Comment to trigger CI
# Comment to trigger CI


if __name__ == "__main__":
    print(main())
