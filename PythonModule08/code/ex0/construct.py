import sys
import os


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("  python -m venv matrix_env")
        print("  source matrix_env/bin/activate # On Unix")
        print("  matrix_env\\Scripts\\activate # On Windows")
        print("Then run this program again.")
    else:
        venv_name = os.path.basename(sys.prefix)
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        site_pkg_path = os.path.join(
            sys.prefix, "lib", f"python{python_version}", "site-packages")

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("Package installation path:")
        print(f"  {site_pkg_path}")


if __name__ == "__main__":
    main()
