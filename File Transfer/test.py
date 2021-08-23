import shutil, os, time, datetime


now = time.time()
day = 60*60*24 #Number of seconds in one day
destination = 'C:/Users/Jacob/Documents/GitHub/Python-Projects/File Transfer/To-Be-Uploaded/'
source = 'C:/Users/Jacob/Documents/GitHub/Python-Projects/File Transfer/Old Files/'
past = now - day
print(int(past))

def last_mod_time(file):
    return os.path.getmtime(file)


for file in os.listdir(source):
    mtime = os.path.join(source, file)
    #ctime = os.path.getctime(source + file)
    print('File Name: {}'.format(file))
    print('Last Modified Time: {}'.format(mtime))
    #print('Original Created Time: {}'.format(ctime))
    print('')
    if last_mod_time(mtime) > past:
        destination_file = os.path.join(destination, file)
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
