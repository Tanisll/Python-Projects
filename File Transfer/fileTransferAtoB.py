import shutil
import os

# set where the source of the files are
source = '../File Transfer/Folder A/'

#set the destination path to Folder B
destination = '../File Transfer/Folder B/'
files = os.listdir(source)

for i in files:
    # we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
