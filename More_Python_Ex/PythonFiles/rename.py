# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:42:00 2020

@author: Manisha
"""

import os

os.chdir('C:\\Users\\Manisha\\mystuff\\sample files')

#print(os.getcwd())

for f in os.listdir():
    #print(f)
    #print(os.path.splitext(f))
    
    f_name, f_type_name, f_ext = os.path.splitext(f)
    
    f_title,f_num = f_name.split('-')
    
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    
    renamed_to = '{}-{}{}'.format(f_num, f_title, f_ext)
    
    os.rename(f, renamed_to)