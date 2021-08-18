from tkinter import *
import tkinter as tk

import Webpage_Editor_main
import Webpage_Editor_func

def load_gui(self):
    self.lbl_header = tk.Label(self.master, text='Edit the body of your website below')
    self.lbl_header.grid(row=0,column=0,columnspan=2,padx=(100,0),pady=(10,0))
    
    self.txt_editor = tk.Entry(self.master,text='')
    self.txt_editor.grid(row=1,column=0,rowspan=5,columnspan=2,padx=(100,0),pady=(10,10),sticky=N+E+S+W)

    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: Webpage_Editor_func.onUpdate(self))
    self.btn_update.grid(row=6,column=0,padx=(100,0),pady=(100,10),sticky=S)
    self.btn_cancel = tk.Button(self.master,width=12,height=2,text='Cancel',command=lambda: Webpage_Editor_func.onClose(self))
    self.btn_cancel.grid(row=6,column=1,padx=(100,0),pady=(100,10),sticky=S)
    



if __name__ == "__main__":
    pass
