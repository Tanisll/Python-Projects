import sqlite3

conn = sqlite3.connect('fileType.db')

with conn:
    cur = conn.cursor()
    cur.execute('create table if not exists Files( \
        id integer primary key autoincrement, \
        txtFiles text)')
    conn.commit()



fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')



for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('insert into Files (txtFiles) values (?)',(x,))
            print(x)
conn.close()
