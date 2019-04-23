# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:59:43 2019

@author: ahirr
"""

import tkinter as tk 
r = tk.Tk() 
r.title('Counting Seconds') 
button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack() 
r.mainloop()