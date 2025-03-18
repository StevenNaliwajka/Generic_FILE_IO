import json
from pathlib import Path

def read_json(file_path: str, key: str):
    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        return None

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return None

    return data.get(key, None)