from pathlib import Path

from generic_file_io.core.generic_create_file import generic_create_file


def csv_create(file_path:str, overwrite:bool=False):
    generic_create_file(file_path, overwrite)