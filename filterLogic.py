# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 20:17:11 2022

@author: Nadeshkumar
"""

from PIL import Image,ImageFilter

path = r'image.jpg'

with Image.open(path) as img :
    # img.filter(ImageFilter.SHARPEN).show()
    img.filter(ImageFilter.BLUR).show()

