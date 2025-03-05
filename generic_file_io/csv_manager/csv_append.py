import os

from generic_file_io.core.generic_append_to_file import generic_append_to_file
from generic_file_io.csv_manager.support.format_csv_entry import format_csv_entry


def csv_append(file_path: str, dict_of_items: dict, prevent_duplicates: bool = False, separator: bool = False):
    """Appends a dictionary as a new row in a CSV file, optionally preventing duplicates.
       Inserts a blank row if `separator=True` (for separating sections/tables)."""

    if not isinstance(dict_of_items, dict):
        raise TypeError(f"Expected a dictionary, got {type(dict_of_items)}: {dict_of_items}")

    # Format the entry
    new_entry = format_csv_entry(dict_of_items) + "\n"

    if prevent_duplicates:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    existing_entries = set(line.strip() for line in file if line.strip())
            except Exception as e:
                print(f"Warning: Could not read {file_path}. Assuming no existing entries. Error: {e}")
                existing_entries = set()

            if new_entry.strip() in existing_entries:
                print("Duplicate entry detected. Skipping append.")
                return

    # Insert a blank line if needed
    if separator:
        generic_append_to_file(file_path, "\n")

    # Append the new entry
    generic_append_to_file(file_path, new_entry)
