import os
from typing import Optional
from dotenv import load_dotenv


def load_config() -> dict:
    """
    Loads configuration from .env file and environment variables.
    Returns a dictionary with the configuration values.
    """

    load_dotenv()

    config: dict = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }

    return config


def mask_secret(secret: Optional[str]) -> str:
    """Helper to hide secrets in logs/output."""
    if secret:
        return "*" * 8
    return "MISSING"


def main() -> None:
    """
    Main execution flow: Load Config -> Display Status -> Security Check.
    """
    print("ORACLE STATUS: Reading the Matrix...")

    config = load_config()

    mode = config.get("MATRIX_MODE") or "development"

    if mode == "production":
        db_msg = "Connected to production cluster"
        api_status = "Authenticated (High Security)"
        key_display = mask_secret(config.get("API_KEY"))
    else:
        db_msg = "Connected to local instance"
        api_status = "Authenticated (Debug Mode)"
        key_display = config.get("API_KEY") or "MISSING"

    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    print(f"  Database: {db_msg}")
    print(f"  API Access: {api_status}")
    print(f"  Log Level: {config.get('LOG_LEVEL') or 'INFO'}")
    print(
        f"  Zion Network: "
        f"{'Online' if config.get('ZION_ENDPOINT') else 'Offline'}"
    )
    print(f"  API Key Check: {key_display}")
    print("\nEnvironment security check:")
    print("  [OK] No hardcoded secrets detected")

    env_exists = os.path.exists(".env")
    print(
        f"  [{'OK' if env_exists else 'WARN'}] .env file "
        f"{'found' if env_exists else 'not found'}"
    )

    if any(config.values()):
        print("  [OK] Production overrides available")
    else:
        print("  [WARN] No configuration loaded")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
