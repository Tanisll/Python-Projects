from tkinter import *
import tkinter as tk


import Webpage_Editor_gui
import Webpage_Editor_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        Webpage_Editor_func.center_window(self,500,300)
        self.master.title("Summer Sale Webpage Editor")
        self.master.configure(bg="#EFE4B0")
        Webpage_Editor_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
