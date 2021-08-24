from tkinter import *
import tkinter as tk

import fileTransfer_gui
import fileTransfer_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.master = master
        self.master.minsize(600,300)
        self.master.maxsize(600,300)
        fileTransfer_func.center_window(self,500,300)
        self.master.title("File Checker")
        fileTransfer_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
