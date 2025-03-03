from pathlib import Path

def generic_create_file(file_path:str) -> None:
    file_path = Path(file_path)

    # Check and create file if it doesn't exist
    if not file_path.exists():
        file_path.touch()
        # print(f"File created: {file_path}")