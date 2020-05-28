'''
Created on 26-May-2020

@author: Lavendra rajput
'''
import os

import tkinter as tk 

def on_start():
    os.startfile('SeleniumExecutable.exe')

root = tk.Tk()
root.geometry("800x200")
root.title("Selenium Test Cases")

button1 = tk.Button(root, text = "Start",bg = 'green', command =on_start, height = 5, width = 100)
button2 = tk.Button(root, text = "Stop", bg = 'red' ,command = root.destroy, height = 5, width = 100)

button1.pack()
button2.pack()

root.mainloop()
