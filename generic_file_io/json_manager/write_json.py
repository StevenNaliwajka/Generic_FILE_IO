import json
from pathlib import Path

from generic_file_io.core.generic_create_file import generic_create_file

'''
Example Data:

config_data = {
    "api_key": "12345",
    "url": "https://example.com",
    "enabled": True
}
'''

def write_json(file_path:str, data:dict, overwrite:bool=False) -> None:
    str_file_path = Path(file_path)

    generic_create_file(file_path, overwrite)

    if overwrite or str_file_path.stat().st_size == 0:
        json_data = data
    else:
        with open(file_path, 'r') as f:
            try:
                existing_data = json.load(f)
                json_data = {**existing_data, **data}
            except json.JSONDecodeError:
                json_data = data

    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=4)