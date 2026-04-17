    # Detection Logic:
    # 'sys.prefix' points to the current installation prefix.
    # 'sys.base_prefix' points to the original Python installation.
    # If they differ, we are inside a virtual environment.


        # 1. Load variables from .env file into environment.
    # NOTE: load_dotenv does NOT override variables that are already set in the shell.
    # This automatically satisfies our Priority Rule: Shell > .env