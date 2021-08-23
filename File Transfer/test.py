import shutil, os, time, datetime


now = time.time()
oneDay_ago = now - 60*60*24 #Number of seconds in one day
destination = '../File Transfer/To-Be-Uploaded/'

for file in os.listdir('../File Transfer/Old Files/'):
    if file.endswith ('.txt'):
        mtime = os.path.getmtime('../File Transfer/Old Files/' + file)
        ctime = os.path.getctime('../File Transfer/Old Files/' + file)
        print('File Name: {}'.format(file))
        print('Last Modified Time: {}'.format(mtime))
        print('Original Created Time: {}'.format(ctime))
        print('')
        if mtime > oneDay_ago:
            shutil.move(file, destination)



"""
for file in os.listdir('../File Transfer/Old Files/'):
    if file.endswith ('.txt'):
        mtime = os.path.getmtime('../File Transfer/Old Files/' + file)
        ctime = time.localtime(mtime)
        ftime = time.strftime('%d%m%Y %H:%M:%S',ctime)
        dtime = datetime.datetime.strptime(ftime,'%d%m%Y %H:%M:%S')
        print(dtime)
        
        
        #if dtime >= delta >= now:
         #   shutil.move(source+i, destination)

"""
