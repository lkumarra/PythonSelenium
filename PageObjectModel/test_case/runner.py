'''
Created on 26-May-2020

@author: Lavendra rajput
'''
import os
import subprocess

import tkinter as tk 


def on_start():
    subprocess.run(r'C:\Users\Lavendra rajput\git\PythonSelenium\PageObjectModel\SeleniumExecutable.exe', shell = True)

    
def on_stop():
    root.destroy


root = tk.Tk()
root.geometry("1500x500")
root.title("Selenium Test Cases")

button1 = tk.Button(root, text = "Start",bg = 'green', command =on_start(), height = 5, width = 100)
button2 = tk.Button(root, text = "Stop", bg = 'red' ,command = on_stop, height = 5, width = 100)


button1.pack()
button2.pack()

root.mainloop()
