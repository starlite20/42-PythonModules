#!/usr/bin/env python3
"""
Module: loading.py
Description: Data analysis tool demonstrating dependency management.
Uses numpy for data generation, pandas for analysis, and matplotlib for visualization.
"""

import sys
import importlib.metadata
from typing import List, Dict


def get_package_version(package_name: str) -> str:
    """
    Safely retrieve the version of an installed package.
    Returns 'Not Found' if the package is missing.
    """
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return "Not Found"


def main() -> None:
    """
    Main execution flow: Check dependencies -> Analyze Data -> Visualize.
    """
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    # Define required packages and their descriptions
    required_packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    missing_dependencies: List[str] = []

    # Check availability of packages
    for pkg, desc in required_packages.items():
        version = get_package_version(pkg)
        if version != "Not Found":
            print(f"  [OK] {pkg} ({version}) - {desc}")
        else:
            print(f"  [MISSING] {pkg} - {desc}")
            missing_dependencies.append(pkg)

    # If dependencies are missing, print instructions and exit
    if missing_dependencies:
        print("\nERROR: Missing critical Matrix programs.")
        print("Please install missing packages using one of the following methods:")
        print("\n[Option 1: Pip]")
        print("  pip install -r requirements.txt")
        print("\n[Option 2: Poetry]")
        print("  poetry install")
        print("  poetry run python loading.py")
        sys.exit(1)

    # If we are here, imports should be safe. 
    # We import inside the function to avoid linter errors before installation.
    try:
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError as e:
        print(f"Unexpected Import Error: {e}")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    # 1. Generate Data using Numpy (Source of data)
    # Generating 1000 data points with 4 columns (A, B, C, D)
    data_points = 1000
    raw_matrix = np.random.randint(0, 100, size=(data_points, 4))
    columns = ['Agent_Smiths', 'Neos', 'Oracles', 'Morpheus']
    
    print(f"  Processing {data_points} data points...")

    # 2. Manipulate Data using Pandas
    df = pd.DataFrame(raw_matrix, columns=columns)
    summary_stats = df.describe()

    # 3. Visualize using Matplotlib
    print("  Generating visualization...")
    
    # Create a simple bar chart of the mean values
    mean_values = df.mean()
    
    plt.figure(figsize=(10, 6))
    mean_values.plot(kind='bar', color=['red', 'green', 'purple', 'blue'])
    plt.title('Average Power Levels in the Matrix')
    plt.ylabel('Power Level')
    plt.xlabel('Entities')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot
    output_file = 'matrix_analysis.png'
    plt.savefig(output_file)
    print(f"  Analysis complete!")
    print(f"Results saved to: `{output_file}`")


if __name__ == "__main__":
    main()