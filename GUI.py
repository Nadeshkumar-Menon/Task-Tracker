# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:11:39 2022

@author: Nadeshkumar
"""

#Creating an Image editor

import tkinter as tk
from tkinter import ttk

window_dimension = '1000x500'

#Try creating a button class


class MainFrame:
    '''
        A custom class that creates the Label frame
    '''
    def __init__(self,master):
        self.master = master
        self.frame = tk.LabelFrame(self.master,text = 'New Task',bg = '#66ccff',fg='white',font=('Helvetica Bold',14))
        self.frame.pack(fill = 'both',expand = True)
        
        #initialize label style
        self.style = ttk.Style(self.master)
        self.style.configure('TLabel',font=('Helvetica 14 underline'),foreground='white',background='#66ccff')
        # self.style.configure('TButton',font = 'Helvetica 14',background = 'black',foreground = 'white')
        # self.style.map('TButton',background = [('active','#4d0000'),('disabled','#000000')])
        #Label to enter Username
        self.uname_lbl = ttk.Label(self.frame,text='Title -')
        self.uname_lbl.place(x=50,y=50)
        #Label to enter Passsword
        self.password_lbl = ttk.Label(self.frame,text='Description -')
        self.password_lbl.place(x=50,y=100)
        
        #Entry for Title
        self.uname_temp = ''
        self.uname_entry = ttk.Entry(self.master,self.uname_temp,width=70)
        self.uname_entry.place(x=220,y=78)
        #Text box for Description
        self.pass_temp = ''
        self.pass_entry = tk.Text(self.master,width=80,height=15)
        self.pass_entry.place(x=220,y=128)
        #Button to add new entry
        self.new_entry = tk.Button(text='New Entry',command = self.add_new_entry,font='Helvetica 14',
                                   width = 10,height = 2,background='#000000',foreground='white')
        self.new_entry.place(x=50,y=400)
    def add_new_entry(self):        
        pass



root = tk.Tk()
root.geometry(window_dimension)
root.title('Task Tracker')

#Create the main frame
root_frame = MainFrame(root)
root.mainloop()