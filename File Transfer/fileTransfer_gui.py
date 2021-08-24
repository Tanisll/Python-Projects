from tkinter import *
import tkinter as tk

import fileTransfer_main
import fileTransfer_func

def load_gui(self):
    self.source_header = tk.Label(self.master, text='Input source folder below:')
    self.source_header.grid(row=0,column=0,padx=(10,0),pady=(10,0))
    
    self.source_entry = tk.Entry(self.master,text='')
    self.source_entry.grid(row=1,column=0,columnspan=3,padx=(10,10),pady=(10,10),sticky=EW)

    self.source_button = tk.Button(self.master, text='Browse...',command=lambda:fileTransfer_func.browse_button_source(self))
    self.source_button.grid(row=1,column=4)
    
    self.lbl_4 = tk.Label(self.master, text='                                                 ')
    self.lbl_4.grid(row=2,column=0)
    self.lbl_5 = tk.Label(self.master, text='                                                 ')
    self.lbl_5.grid(row=2,column=1)
    self.lbl_6 = tk.Label(self.master, text='                                                 ')
    self.lbl_6.grid(row=2,column=2)
    
    self.destination_header = tk.Label(self.master, text='Input destination folder below:')
    self.destination_header.grid(row=3,column=0,padx=(20,0),pady=(10,0))

    self.destination_entry = tk.Entry(self.master,text='')
    self.destination_entry.grid(row=4,column=0,columnspan=3,padx=(10,10),pady=(10,10),sticky=EW)

    self.source_button = tk.Button(self.master, text='Browse...',command=lambda:fileTransfer_func.browse_button_destination(self))
    self.source_button.grid(row=4,column=4)
    
    self.lbl_7 = tk.Label(self.master, text='                                             ')
    self.lbl_7.grid(row=5,column=0, pady=(30,30))
    self.lbl_8 = tk.Label(self.master, text='                                             ')
    self.lbl_8.grid(row=5,column=1, pady=(30,30))
    self.lbl_9 = tk.Label(self.master, text='                                             ')
    self.lbl_9.grid(row=5,column=2, pady=(30,30))

    self.transfer_button = tk.Button(self.master, text='Transfer Files',command=lambda:fileTransfer_func.fileTransfer(self))
    self.transfer_button.grid(row=6,column=0,sticky=E)
    self.cancel_button = tk.Button(self.master, text='Cancel and Close',command=lambda:fileTransfer_func.app_quit(self))
    self.cancel_button.grid(row=6,column=2,sticky=W)
    
    #self.entrySource = tk.Entry(self.master)
    #self.entrySource.grid(row=1,column=0,columnspan=3,padx=(10,100),pady=(10,100))
    



if __name__ == "__main__":
    pass
