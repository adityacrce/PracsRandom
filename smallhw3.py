# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:50:36 2019

@author: ahirr
"""

def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
  
# Driver code 
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string))