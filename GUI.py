# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:11:39 2022

@author: Nadeshkumar
"""

#Creating an Image editor

import tkinter as tk

window_dimension = '800x400'


class MainFrame:
    '''
        A custom class that creates the Label frame
    '''
    def __init__(self,master):
        self.master = master
        self.frame = tk.LabelFrame(self.master,text = 'Login',bg = '#66ccff')
        self.frame.pack(fill = 'both',expand = True)
        
        #Label to enter filename
        
        #Add a button for Action
        
        #Add a close button



root = tk.Tk()
root.geometry(window_dimension)
root.title('Login Page')

#Create the main frame
root_frame = MainFrame(root)
root.mainloop()