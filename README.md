# Compress Folder Program

## Owner of this Python script
- Rohaenat Mustapha

## Description
This Python program allows users to compress files and folders into various compressed file types such as .zip, .tar, and .tgz. If the user selects .tgz as the compress type, the archive is saved as "name_of_the_folder_date_month_year.tgz".

## Requirements
- Python 3.x
- The program assumes that the necessary libraries and tools for compression are installed.

## How to Run
1. Clone the repository or download the source code.
2. Open a terminal or command prompt.
3. Navigate to the directory where the program is located.
4. Run the program using the following command:

    ```bash
    python compress_folder.py
    ```

5. Follow the on-screen prompts to enter the folder path and select the desired compressed file type.

## Example
```bash
Enter the path of the folder to compress: /path/to/your/folder

Available compressed file types:
1. Zip (.zip)
2. Tar (.tar)
3. Tar Gzipped (.tgz)

Select the desired compressed file type (1/2/3): 3
Compression successful. Compressed file saved as: folder_name_2024_02_14.tgz