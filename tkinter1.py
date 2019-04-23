# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:49:04 2019

@author: ahirr
"""

import tkinter as tk
r= tk.Tk()
r.title('counting seconds')
button=tk.Button(r, text='stop', width=25, command= r.destroy)
button.pack()
r.mainloop()