import os
import shutil
from datetime import datetime

def move_screenshots():
    # redirect us to desktop folder
    desktop_path = os.path.expanduser("~/Desktop")

    # make a folder 'images', if doesnt't exist
    images_folder = os.path.join(desktop_path, 'screens')
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)

    # Makes a new folder inside 'screens' folder according to the dates
    date = datetime.now().strftime("%A-%B-%d")
    current_folder = os.path.join(images_folder, date)
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)


    # Get all the files on Desktop
    files_on_desktop = os.listdir(desktop_path)

    for file_name in files_on_desktop:
        if file_name.lower().startswith('screenshot'):
            file_path = os.path.join(desktop_path, file_name)
            shutil.move(file_path, current_folder)
            print(f'Moved {file_name} to image_folder')


move_screenshots()
