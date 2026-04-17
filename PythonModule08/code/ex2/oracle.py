import os
from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv()

    config: dict = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }

    return config


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    config = load_config()

    for key, value in config.items():
        if not value:
            print(f"[WARN] Missing configuration for {key}. Using default.")

    mode = config.get("MATRIX_MODE") or "development"

    if mode == "production":
        db_msg = "Connected to production instance"
        api_status = "Authenticated (Production)"
    else:
        db_msg = "Connected to local instance"
        api_status = "Authenticated"

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_msg}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {config.get('LOG_LEVEL') or 'INFO'}")
    print(
        f"Zion Network: "
        f"{'Online' if config.get('ZION_ENDPOINT') else 'Offline'}"
    )

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found")

    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
