# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:11:39 2022

@author: Nadeshkumar
"""

#Creating an Image editor

import tkinter as tk
from tkinter import ttk

window_dimension = '500x400'


class MainFrame:
    '''
        A custom class that creates the Label frame
    '''
    def __init__(self,master):
        self.master = master
        self.frame = tk.LabelFrame(self.master,text = 'Login',bg = '#66ccff',fg='white',font=('Helvetica Bold',14))
        self.frame.pack(fill = 'both',expand = True)
        
        #initialize label style
        self.style = ttk.Style(self.master)
        self.style.configure('TLabel',font=('Helvetica',14),foreground='white',background='#66ccff')
        # self.style.configure('Tentry')
        #Label to enter Username
        self.uname_lbl = ttk.Label(self.frame,text='Username -')
        self.uname_lbl.place(x=50,y=100)
        #Label to enter Passsword
        self.password_lbl = ttk.Label(self.frame,text='Password -')
        self.password_lbl.place(x=50,y=150)
        
        #Entry for uname
        self.uname_temp = ''
        self.uname_entry = ttk.Entry(self.uname_temp,width=40)
        self.uname_entry.place(x=220,y=128)
        #Entry for uname
        self.pass_temp = ''
        self.pass_entry = ttk.Entry(self.pass_temp,width=40)
        self.pass_entry.place(x=220,y=178)
        
        #Add a button for Login
        
        #add an action funtion



root = tk.Tk()
root.geometry(window_dimension)
root.title('Login Page')

#Create the main frame
root_frame = MainFrame(root)
root.mainloop()