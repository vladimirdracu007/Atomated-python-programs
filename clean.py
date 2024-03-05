# Clean your Temporary files
import shutil
import os

def delete_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

parent_folder_path1 = 'C:/Users/DELL/AppData/Local'
folder_to_delete1 = 'Temp'

parent_folder_path2 = 'C:/Windows'
folder_to_delete2 = 'Temp'

folder_to_delete_path1 = os.path.join(parent_folder_path1, folder_to_delete1)
folder_to_delete_path2 = os.path.join(parent_folder_path2, folder_to_delete2)

if os.path.exists(folder_to_delete_path1):
    delete_folder_contents(folder_to_delete_path2)
if os.path.exists(folder_to_delete_path1):
    delete_folder_contents(folder_to_delete_path2)
