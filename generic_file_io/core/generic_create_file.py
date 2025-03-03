from pathlib import Path

def generic_create_file(file_path:str, overwrite:bool = False) -> None:
    file_path = Path(file_path)

    if overwrite or not file_path.exists():
        # Overwrites if existing
        # creates empty file if not.
        file_path.write_text("")
        #print(f"File {'overwritten' if overwrite else 'created'}: {file_path}")