import pathlib

def consolidate_python_files(source_dir, output_file):
    # Convert string to a Path object
    root = pathlib.Path(source_dir).resolve()
    output_path = pathlib.Path(output_file)
    
    # Use rglob to find all .py files recursively
    py_files = list(root.rglob("*.py"))
    
    print(f"Found {len(py_files)} Python files. Compiling...")

    with open(output_path, "w", encoding="utf-8") as outfile:
        for file_path in py_files:
            # Skip the output file if it's in the same directory
            if file_path == output_path.resolve():
                continue
                
            # Get the path relative to the root for cleaner headers
            relative_path = file_path.relative_to(root)
            
            try:
                content = file_path.read_text(encoding="utf-8")
                
                # Write header
                outfile.write(f"=======\n{relative_path}\n==========\n\n")
                
                # Write actual code
                outfile.write(content)
                
                # Write footer
                outfile.write(f"\n\n=======\nEND OF : {relative_path}\n==========\n\n")
                
            except Exception as e:
                print(f"Could not read {relative_path}: {e}")

if __name__ == "__main__":
    # CONFIGURATION: Change these to your needs
    TARGET_DIRECTORY = "/home/suhail/Documents/github/42-PythonModules/PythonModule07/code" 
    OUTPUT_FILENAME = "codebase_summary.txt"
    
    consolidate_python_files(TARGET_DIRECTORY, OUTPUT_FILENAME)
    print(f"Done! Saved to {OUTPUT_FILENAME}")