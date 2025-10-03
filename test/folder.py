import os

folder_name = "my_new_folder"
file_name = "my_file.txt"
file_content = "placeholder"

os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, file_name)

with open(file_path, "w") as f:
    f.write(file_content)

print(f"Folder '{folder_name}' created and file '{file_name}' created inside it.")
