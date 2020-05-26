'''
Created on 26-May-2020

@author: Lavendra rajput
'''
import tkinter as tk 
r = tk.Tk()
r.title("Counting the seconds ")
greeting =  tk.Label(
    text="Hello, Tkinter",
    foreground="Red",  # Set the text color to white
    background="Yellow"  # Set the background color to black
)
greeting.pack()
b = tk.Button(r, text='Start', width=25, command=r.destroy)
b.pack()
r.mainloop()