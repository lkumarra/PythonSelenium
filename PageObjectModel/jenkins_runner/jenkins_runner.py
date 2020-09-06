"""
Created on 28-May-2020
@author: Lavendra rajput
"""

from jenkins_utils.jenkins_utils import DevOpsJenkins
import tkinter as tk 
from tkinter import *
import threading

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

#Decorator
def start_thraed():
    '''Decorator for Threading implementation'''
    def start_func(func):
        def func_wrapper(*arg):
            thread = threading.Thread(target = func, args = [*arg])
            thread.start()
            return thread
        return func_wrapper
    return start_func

class JenkinsBuildTrigger():
    
    def __init__(self, obj):
        self.root = obj
        self.root.title("Jenkinks Runner")
        self.root.geometry("1280x900")
        self.root.minsize(width=1280, height=900)
        self.root.iconphoto(True, PhotoImage(master=self.root,file = "Guru99.PNG"))
        self.pm = PanedWindow(self.root, orient = VERTICAL, sashpad = 4, sashrelief = 'raised', sashwidth = 6)
        self.console_frame = Frame(self.root, padx = 3, pady = 3)
        self.console_frame.rowconfigure(0, weight = 1)
        self.console_frame.columnconfigure(0, weight = 1)
        self.pm.add(self.console_frame)
        self.pm.paneconfigure(self.console_frame, minsize=135)
        self.label_frame = LabelFrame(self.console_frame, text = "Console", padx = 5, pady = 5, font = "TkHeadingFont", background = "snow", borderwidth = 8,foreground = "gray1")
        self.select_frame = LabelFrame(self.console_frame, text = "Script", padx = 5, pady = 5, font = "TkMenuFont", background = "snow", borderwidth = 8, foreground = "Black")
        self.start_button = Button(self.select_frame, text = "Start", padx = 5, pady =5, width=9,highlightthickness=2,background = "lawn green", foreground = "gray1",command = self.on_start, borderwidth =3)
        self.stop_button = Button(self.select_frame, text = "Stop", padx = 5, pady =5,  width=9,highlightthickness=2,background = "orange red", foreground = "gray1", command = self.on_stop, borderwidth =3)
        self.console_output = Button(self.select_frame, text = "Output", padx = 5, pady =5,  width=9,highlightthickness=2,background = "steelBlue1", foreground = "gray1", command = self.get_console_output, borderwidth =3)
        self.image = PhotoImage(file = "guru99demo.PNG")
        self.label= Label(self.select_frame, image = self.image, background = "white")
        self.scrolled_text = Text(self.label_frame, state = "normal", wrap = "none", borderwidth = 0, height = 20, width = 20)
        self.text_vsb = Scrollbar(self.label_frame, orient ="vertical", command = self.scrolled_text.yview, background = "gray21")
        self.text_hsb = Scrollbar(self.label_frame, orient ="horizontal", command = self.scrolled_text.xview, background = "gray21")
        self.scrolled_text.configure(yscrollcommand = self.text_vsb.set, xscrollcommand = self.text_hsb.set)
        self.scrolled_text.grid(row = 0, column = 0, sticky = N+S+W+E)
        self.text_vsb.grid(row = 0, column = 1, sticky = "ns")
        self.text_hsb.grid(row = 1, column = 0, sticky = "ew")
        self.scrolled_text.configure(font="TkFixedFont", background = "black")
        self.label_frame.rowconfigure(1, weight=1)
        self.label_frame.columnconfigure(0, weight = 1)
        self.label_frame.grid(row = 1, column = 0, sticky = E+W+N+S, padx = 5, pady = 5)
        self.label.pack(side = TOP, fill = "both", expand = "yes")
        self.start_button.pack(side = LEFT, padx = 5, pady = 5)
        self.stop_button.pack(side = RIGHT, padx = 5, pady = 5)
        self.console_output.pack(side = BOTTOM, padx = 5, pady = 5) 
        self.select_frame.grid(row =0, column = 0, sticky = E+W+N+S, padx = 5, pady = 5)
        self.scrolled_text.tag_config("DEBUG", foreground ="RoyalBlue1")
        self.scrolled_text.tag_config("DEFAULT", foreground ="snow")
        self.scrolled_text.tag_config("STOP", foreground = "Red", font = "bold")
        self.scrolled_text.tag_config("FAILED", foreground ="Red2")
        self.scrolled_text.tag_config("PASSED", foreground = "SpringGreen2")
        self.scrolled_text.tag_config("FAILURES", foreground = "Red2", font="bold")
        self.scrolled_text.tag_config("WARNING", foreground = "yellow")
        self.pm.pack(fill = BOTH, expand = 1)
    
    @start_thraed()
    def on_start(self):
        """
        Start Bulid execution on clicking start button
        """
        NAME_OF_JOB = "Python_Automation_Framework"
        TOKEN_NAME = "python_automation_framework"
        # Example Parameter
        PARAMETERS = None
        jenkins_obj = DevOpsJenkins()
        output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
        self.scrolled_text.insert(END, "Jenkins Build URL: {}".format(output['url']), "DEBUG")

    @start_thraed()
    def on_stop(self):
        """
        Stop the jenkins build execution on clicking stop button
        """
        jenkins_obj2 = DevOpsJenkins()
        jenkins_obj2.build_stop("Python_Automation_Framework")
    
    @start_thraed()
    def get_console_output(self):
        """
        Get the jenkins console output
        """
        jenkins_obj2 = DevOpsJenkins()
        output = jenkins_obj2.get_console_output("Python_Automation_Framework")
        self.scrolled_text.insert(END, output, "DEFAULT")
        
if __name__ == "__main__":
    root = Tk()
    JenkinsBuildTrigger(root)
    root.mainloop()
