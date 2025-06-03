import os


def main() -> None:
    env = os.getenv("ENVIRONMENT", "default")
    print(f"Starting extraction in environment: {env}")


if __name__ == "__main__":
    main()
