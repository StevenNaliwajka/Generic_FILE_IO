from pathlib import Path

def generic_append_to_file(file_path:str, data:str) -> None:
    file_path = Path(file_path)

    # Open the file in append mode and write new content
    with file_path.open("a") as file:
        file.write(data)

    # print(f"Content appended to: {file_path}")
