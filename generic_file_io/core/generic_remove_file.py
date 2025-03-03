from pathlib import Path

def generic_remove_file(file_path:str) -> None:
    file_path = Path(file_path)

    # Attempt to remove the file, raising an error if it does not exist
    file_path.unlink(missing_ok=False)
    