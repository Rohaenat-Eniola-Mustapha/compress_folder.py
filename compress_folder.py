import os
import shutil
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    try:
        current_date = datetime.now().strftime("%Y_%m_%d")
        folder_name = os.path.basename(folder_path)
        compressed_filename = f"{folder_name}_{current_date}.{compress_type}"

        if compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, 'w') as zip_file:
                for folder_root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(folder_root, file)
                        zip_file.write(file_path, os.path.relpath(file_path, folder_path))
        elif compress_type == "tar":
            with tarfile.open(compressed_filename, 'w') as tar_file:
                tar_file.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == "tgz":
            with tarfile.open(compressed_filename, 'w:gz') as tar_gz_file:
                tar_gz_file.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Invalid compression type selected.")
            return

        print(f"Compression successful. Compressed file saved as: {compressed_filename}")
    except Exception as e:
        print(f"Compression failed. Error: {str(e)}")

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    
    if not os.path.exists(folder_path):
        print("Invalid folder path. Please provide a valid folder path.")
        return

    print("\nAvailable compressed file types:")
    print("1. Zip (.zip)")
    print("2. Tar (.tar)")
    print("3. Tar Gzipped (.tgz)")

    compress_type_option = input("Select the desired compressed file type (1/2/3): ")

    if compress_type_option == "1":
        compress_type = "zip"
    elif compress_type_option == "2":
        compress_type = "tar"
    elif compress_type_option == "3":
        compress_type = "tgz"
    else:
        print("Invalid option selected.")
        return

    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()
