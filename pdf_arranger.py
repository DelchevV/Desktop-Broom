import os
import shutil
from datetime import datetime

def move_PDFs():
    # Redirect us to the desktop folder
    desktop_path = os.path.expanduser("~/Desktop")

    # Make a folder 'PDFs', if it doesn't exist
    pdfs_folder = os.path.join(desktop_path, 'PDFs')
    if not os.path.exists(pdfs_folder):
        os.makedirs(pdfs_folder)

    # Makes a new folder inside 'PDFs' folder according to the date
    date = datetime.now().strftime("%A-%B-%d")
    current_folder = os.path.join(pdfs_folder, date)
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)

    # Get all the files on the desktop
    files_on_desktop = os.listdir(desktop_path)

    for file_name in files_on_desktop:
        if file_name.lower().endswith('.pdf'):
            file_path = os.path.join(desktop_path, file_name)
            # Construct the destination path using os.path.join()
            final_destination = os.path.join(current_folder, file_name)
            # Check if the file already exists in the destination folder
            if os.path.exists(final_destination):
                print(f"Error: File '{file_name}' already exists in the {date} folder.")
            else:
                shutil.move(file_path, current_folder)
                print(f"Moved {file_name} to {current_folder}.")

if __name__ == "__main__":
    move_PDFs()
