"""
Created on 28-May-2020
@author: Lavendra rajput
"""

from jenkins_utils.jenkins_utils import DevOpsJenkins
import tkinter as tk 


def on_start():
    """
    Start Bulid execution on clicking start button
    """
    NAME_OF_JOB = "Python_Automation_Framework"
    TOKEN_NAME = "python_automation_framework"
    # Example Parameter
    PARAMETERS = None
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    print ("Jenkins Build URL: {}".format(output['url']))

    
def on_stop():
    """
    Stop the jenkins build execution on clicking stop button
    """
    jenkins_obj2 = DevOpsJenkins()
    jenkins_obj2.build_stop("Python_Automation_Framework")

    
def get_console_output():
    """
    Get the jenkins console output
    """
    jenkins_obj2 = DevOpsJenkins()
    output = jenkins_obj2.get_console_output("Python_Automation_Framework")
    text = tk.Text(root, height=400, width=200)
    text.config(bg="skyblue")
    text.insert(tk.END, output)
    text.pack()

    
root = tk.Tk()
root.geometry("1920x1080")
root.title("Jenkins Buid Trigger")
button1 = tk.Button(root, text="Start", bg='green', command=on_start, height=2, width=10)
button1.pack(padx=5, pady=10, side=tk.LEFT,)
button2 = tk.Button(root, text="Stop", bg='Red', command=on_stop, height=2, width=10)
button2.pack(padx=5, pady=10, side=tk.LEFT)
button3 = tk.Button(root, text="ConsoleOutput", bg='Blue', command=get_console_output, height=2, width=10)
button3.pack(padx=5, pady=10, side=tk.LEFT)
root.mainloop()
