import os


def generic_create_folder(folder_path:str) -> None:
    try:
        os.makedirs(folder_path, exist_ok=True)
        #print(f"Folder created successfully: {folder_path}")
    except Exception as e:
        print(f"Error creating folder: {e}")