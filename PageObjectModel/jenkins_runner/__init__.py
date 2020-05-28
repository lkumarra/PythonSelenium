'''
Created on 26-May-2020
@author: Lavendra rajput
'''
import os

from jenkins_utils.jenkins_runner import DevOpsJenkins
import tkinter as tk 


def on_start():
    NAME_OF_JOB = "Python_Automation_Framework"
    TOKEN_NAME = "python_automation_framework"
    # Example Parameter
    PARAMETERS = None
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    label1 = tk.Label(root, text= "Jenkins Build URL: {}".format(output['url']))
    label1.pack()
    
    print ("Jenkins Build URL: {}".format(output['url']))

root = tk.Tk()
root.geometry("800x200")
root.title("Jenkins Buid Trigger")

button1 = tk.Button(root, text = "Start",bg = 'green', command =on_start, height = 2, width = 10)
button1.pack()

root.mainloop()