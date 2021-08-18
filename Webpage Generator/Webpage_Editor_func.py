import os
from tkinter import *
import tkinter as tk
import webbrowser

import Webpage_Editor_main
import Webpage_Editor_gui

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def onClose(self):
    self.master.destroy()
    os._exit(0)

def onUpdate(self):
    v = self.txt_editor.get()
    c = open("SummerSale.html", "w")
    c.write("<html>\n"
            "   <body>\n"
            "      <h1>{}</h1>\n"
            "   </body>\n"
            "</html>".format(v))
    c.close()
    c = open("SummerSale.html", "r")
    print(c.read())
    url = "SummerSale.html"
    webbrowser.open_new_tab(url)
    
