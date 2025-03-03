import os

from generic_file_io.core.generic_append_to_file import generic_append_to_file
from generic_file_io.csv_manager.support.format_csv_entry import format_csv_entry


def csv_append(file_path: str, dict_of_items: dict, prevent_duplicates: bool = False):
    """Appends a dictionary as a new row in a CSV file, optionally preventing duplicates."""

    # Format the entry
    new_entry = format_csv_entry(dict_of_items)

    if prevent_duplicates:
        # Read existing entries if the file exists
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_entries = set(line.strip() for line in file)

            # Check for duplicates
            if new_entry in existing_entries:
                print("Duplicate entry detected. Skipping append.")
                return

    # Append the new entry
    generic_append_to_file(file_path, new_entry)