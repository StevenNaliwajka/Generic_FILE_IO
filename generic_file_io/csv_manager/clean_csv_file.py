import csv
import shutil
import sys

from generic_file_io.core.generic_remove_file import generic_remove_file


def clean_csv_file(file_to_modify: str, final_path: str, og_copy_path: str = '') -> None:
    try:
        # Open and read
        with open(file_to_modify, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read the header row
            cleaned_rows = [header]  # Keep header

            # Filter out rows with 'null' or 'N/A' values
            for row in reader:
                if not any(cell.lower() in ('null', 'n/a') for cell in row):
                    cleaned_rows.append(row)

        # Write the cleaned data to file_path_2
        with open(final_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleaned_rows)

        print(f"Cleaned data saved to: {final_path}")

        # If file_path_3 is provided, copy the original file to file_path_3
        if og_copy_path:
            shutil.copy(file_to_modify, og_copy_path)
            print(f"Original file copied to: {og_copy_path}")

        # Delete the original file
        generic_remove_file(file_to_modify)
        print(f"Original file deleted: {file_to_modify}")

    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python clean_csv_file.py <file_path_1> <file_path_2> [file_path_3]")
    else:
        file_path_1 = sys.argv[1]
        file_path_2 = sys.argv[2]
        file_path_3 = sys.argv[3] if len(sys.argv) > 3 else ''
        clean_csv_file(file_path_1, file_path_2, file_path_3)
