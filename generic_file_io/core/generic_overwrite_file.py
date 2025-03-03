from pathlib import Path

def generic_overwrite_file(file_path:str, data:str) -> None:
    file_path = Path(file_path)

    # Overwrite the file with new content

    with file_path.open("w") as file:
        file.write(data)

    # print(f"File overwritten: {file_path}")
