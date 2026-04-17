import sys
import importlib.metadata


def check_dependencies() -> bool:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    required_packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    missing_dependencies: list[str] = []

    for pkg, desc in required_packages.items():
        try:
            version = importlib.metadata.version(pkg)
            print(f"  [OK] {pkg} ({version}) - {desc}")
        except importlib.metadata.PackageNotFoundError:
            print(f"  [MISSING] {pkg} - {desc}")
            missing_dependencies.append(pkg)

    if missing_dependencies:
        print("\nERROR: Missing critical Matrix programs.")
        print(
            "Please install missing packages using "
            "one of the following methods:"
        )
        print("\n==> PIP method")
        print("pip install -r requirements.txt")
        print("\n==> POETRY method")
        print("poetry install")
        print("poetry run python loading.py")
        return False

    return True


def main() -> None:
    if not check_dependencies():
        sys.exit(1)

    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"Unexpected Import Error: {e}")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    data_points = 1000
    raw_matrix = np.random.randint(0, 100, size=(data_points, 4))
    columns = ['Agent_Smiths', 'Neos', 'Oracles', 'Morpheus']

    print(f"Processing {data_points} data points...")

    df = pd.DataFrame(raw_matrix, columns=columns)

    print("Generating visualization...")

    mean_values = df.mean()

    plt.figure(figsize=(10, 6))
    mean_values.plot(kind='bar', color=['red', 'green', 'purple', 'blue'])
    plt.title('Average Power Levels in the Matrix')
    plt.ylabel('Power Level')
    plt.xlabel('Entities')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    output_file = 'matrix_analysis.png'
    plt.savefig(output_file)

    print("\nAnalysis complete!")
    print(f"Results saved to: `{output_file}`")


if __name__ == "__main__":
    main()
