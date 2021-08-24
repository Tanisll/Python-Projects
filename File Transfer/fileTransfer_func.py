import shutil, os, time, datetime
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory

import fileTransfer_main
import fileTransfer_gui

def last_mod_time(file):
    return os.path.getmtime(file)

def creation_time(file):
    return os.path.getctime(file)

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def app_quit(self):
    self.master.destroy()
    os._exit(0)

def browse_button_source(self):
    global folder_path
    filename = filedialog.askdirectory()
    self.source_entry.insert(tk.END, filename)
    print(filename)

def browse_button_destination(self):
    global folder_path
    filename = filedialog.askdirectory()
    self.destination_entry.insert(tk.END, filename)
    print(filename)

def fileTransfer(self):
    var_source = self.source_entry.get()
    var_destination = self.destination_entry.get()
    now = time.time()
    day = 60*60*24 #Number of seconds in one day
    past = now - day
    for file in os.listdir(var_source):
        mtime = os.path.join(var_source, file)
        ctime = os.path.join(var_source, file)
        if last_mod_time(mtime) > past:
            destination_file = os.path.join(var_destination, file)
            shutil.copy(mtime, destination_file)
        if creation_time(ctime) > past:
            destination_cfile = os.path.join(var_destination, file)
            shutil.copy(ctime, destination_cfile)
