import shutil
import os
import datetime as dt

# set where the source of the files are
source = '../File Transfer/Old Files/'

#set the destination path to Folder B
destination = '../File Transfer/To-Be-Uploaded/'
files = os.listdir(source)

now = dt.datetime.now()
delta = dt.timedelta(hours=24)

for i in files:
    if i.endswith('.txt'):
        set_date = os.path.getmtime(i)
        if delta <= set_date <= now:
            # we are saying move the files represented by 'i' to their new destination
            shutil.move(source+i, destination)

print(source)
