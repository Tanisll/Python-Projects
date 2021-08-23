import os

for file in os.listdir('../File Transfer/Old Files/'):
    if file.endswith('.txt'):
        time_mod = int(os.path.getmtime('../File Transfer/Old Files/' + file))
        x=time_mod//3600
        print(x)
