import shutil
import os

#FolderA destination path
source = '/Users/Owner/Desktop/One Page Site/New/folderA/'

#FolderB destination path
destination = '/Users/Owner/Desktop/One Page Site/New/folderB/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
