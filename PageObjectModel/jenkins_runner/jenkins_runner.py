"""
Created on 28-May-2020
@author: Lavendra rajput
"""
import tkinter as tk 
from tkinter import *
import threading
from ttkwidgets import CheckboxTreeview
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def _destroy_widget(obj, widget_name):
        getattr(obj, widget_name).destroy()
        
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

import jenkins
import time

class DevOpsJenkins:

    def __init__(self, url, username, password):
        self.jenkins_server = jenkins.Jenkins(url, username=username, password=password)
        user = self.jenkins_server.get_whoami()
        version = self.jenkins_server.get_version()
        print ("Jenkins Version: {}".format(version))
        print ("Jenkins User: {}".format(user['id']))
        
    def get_user(self,):
        user = self.jenkins_server.get_whoami()
        return user['id'];
    
    def get_version(self):
        version = self.jenkins_server.get_version()
        return version;

    def build_job(self, name, parameters=None, token=None):
        next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        print(self.jenkins_server.build_job(name, parameters=parameters, token=token))
        time.sleep(10)
        build_info = self.jenkins_server.get_build_info(name, next_build_number)
        return build_info
    
    def build_stop(self, name):
        self.jenkins_server.stop_build(name, self.jenkins_server.get_job_info(name)['nextBuildNumber'] - 1)
        
    def get_console_output(self, name):
        return self.jenkins_server.get_build_console_output(name, self.jenkins_server.get_job_info(name)['nextBuildNumber'] - 1)
    
    def get_build_report(self, name):
        return self.jenkins_server.get_build_test_report(name, self.jenkins_server.get_job_info(name)['nextBuildNumber'] - 1)
    
    def get_all_jobs(self):
        return self.jenkins_server.get_all_jobs()

class JenkinsBuildTrigger():
    
    def __init__(self, obj):
        self.root = obj
        self.root.title("Jenkins Runner")
        self.root.geometry("1280x900")
        self.root.minsize(width=1280, height=900)
        self.root.iconphoto(True, PhotoImage(master=self.root,file = "jenkins.png"))
        self.pm = PanedWindow(self.root, orient = VERTICAL, sashpad = 4, sashrelief = 'raised', sashwidth = 6)
        self.console_frame = Frame(self.root, padx = 3, pady = 3)
        self.console_frame.rowconfigure(0, weight = 1)
        self.console_frame.columnconfigure(0, weight = 1)
        self.pm.add(self.console_frame)
        self.pm.paneconfigure(self.console_frame, minsize=135)
        self.label_frame = LabelFrame(self.console_frame, text = "Console Output", padx = 5, pady = 5, font = "TkHeadingFont", background = "snow", borderwidth = 8,foreground = "gray1")
        self.select_frame = LabelFrame(self.console_frame, text = "Input", padx = 5, pady = 5, font = "TkMenuFont", background = "snow", borderwidth = 8, foreground = "Black")
        self.jenkins_url = Label(self.select_frame, text = "Jenkins Url", bg  = "blue", fg = "white")
        self.jenkins_url_entry = Entry(self.select_frame, bd = 5, bg = "AntiqueWhite1", fg = "Black")
        self.username_label = Label(self.select_frame, text = "Username", bg = "blue", fg = "white")
        self.username_entry = Entry(self.select_frame, bd = 5,  bg = "AntiqueWhite1", fg = "Black")
        self.password_label = Label(self.select_frame, text = "Password", bg = "blue", fg = "white")
        self.password_entry = Entry(self.select_frame, bd = 5,  show='*', bg = "AntiqueWhite1", fg = "Black")
        self.login_button = Button(self.select_frame, text = "Login", padx = 5, pady =5,width = 8,height = 1, background = "RoyalBlue1", foreground = "white", command = self.on_login)
        self.reset_button = Button(self.select_frame, text = "Reset", padx = 5, pady =5,width = 8,height = 1, background = "orange red", foreground = "white", command = self.on_reset)
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
        self.jenkins_url.grid(row = 0, column = 0, padx = 5, pady = 5);
        self.jenkins_url_entry.grid(row = 0, column = 1, padx = 5, pady = 5);
        self.username_label.grid(row = 1, column = 0, padx = 5, pady = 5);
        self.username_entry.grid(row = 1, column = 1, padx = 5, pady = 5);
        self.password_label.grid(row = 2, column = 0, padx = 5, pady = 5);
        self.password_entry.grid(row = 2, column = 1, padx = 5, pady = 5);
        self.login_button.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.reset_button.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.scrolled_text.tag_config("DEBUG", foreground ="RoyalBlue1")
        self.scrolled_text.tag_config("DEFAULT", foreground ="snow")
        self.scrolled_text.tag_config("STOP", foreground = "Red", font = "bold")
        self.scrolled_text.tag_config("FAILED", foreground ="Red2")
        self.scrolled_text.tag_config("PASSED", foreground = "SpringGreen2")
        self.scrolled_text.tag_config("FAILURES", foreground = "Red2", font="bold")
        self.scrolled_text.tag_config("WARNING", foreground = "yellow")
        self.select_frame.grid(row =0, column = 0, sticky = E+W+N+S, padx = 5, pady = 5)
        self.pm.pack(fill = BOTH, expand = 1)
        
    
    @start_thraed()
    def on_login(self):
        url = self.jenkins_url_entry.get();
        username = self.username_entry.get();
        password = self.password_entry.get();
        self.jenkins_obj = DevOpsJenkins(url, username, password)
        jenkins_version = self.jenkins_obj.get_version()
        self.jenkins_url_label = Label(self.select_frame, text = "Jenkins URL: {}".format(url), bg = "SpringGreen2",width = 30)
        self.jenkins_version_label = Label(self.select_frame, text = "Jenkins Version: {}".format(jenkins_version), bg = "SpringGreen2",width = 30)
        self.jenkins_user_label = Label(self.select_frame, text = "Jenkins User: {}".format(self.jenkins_obj.get_user()), bg = "SpringGreen2", width = 30)
        self.select_job = Button(self.select_frame, text = "Select Job",padx = 5, pady =5,width = 8,height = 1, background = "deep sky blue", foreground = "white", command = self.select_jobs)
        self.result = Button(self.select_frame, text = "Result", padx = 5, pady =5,width = 8,height = 1, background = "slate blue", foreground = "white", command = self.on_result)
        self.console_output = Button(self.select_frame, text = "Console", padx = 5, pady =5,width = 8,height = 1, background = "light sea green", foreground = "white",command = self.on_console)
        self.buld_status = Button(self.select_frame, text = "Buid Status", padx = 5, pady =5,width = 8,height = 1, background = "gold", foreground = "white",command = self.on_build_status)
        self.jenkins_url_label.grid(row = 0, column = 2)
        self.jenkins_version_label.grid(row = 1, column = 2)
        self.jenkins_user_label.grid(row = 2, column = 2)
        self.select_job.grid(row = 3, column = 2, padx = 5, pady = 5)
        self.result.grid(row = 4, column = 0,padx = 5, pady = 5)
        self.console_output.grid(row = 4, column = 1,padx = 5, pady = 5)
        self.buld_status.grid(row = 4, column = 2, padx = 5, pady = 5)
        self.jenkins_url_entry.delete("0","end")
        self.username_entry.delete("0","end")
        self.password_entry.delete("0","end")
        self.select_job.configure(state = ACTIVE)
        
    def select_jobs(self):
        self.select_job.configure(state = DISABLED)
        self.select_script = Toplevel(self.root)
        self.select_script.title("Select Job")
        self.select_script.focus_force()
        self.select_script.geometry("600x800")
        self.select_script.minsize(width=500, height=700)
        top_frame = LabelFrame(self.select_script, text = "Select Jobs", padx = 5, pady = 5, font = "TkHeadingFont", background = "light grey", borderwidth = 8,foreground = "gray1")
        bottom_frame = LabelFrame(self.select_script, text = "Buttons", padx = 5, pady = 5, font = "TkHeadingFont", background = "light grey", borderwidth = 8,foreground = "gray1")
        scrollbar = Scrollbar(top_frame)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.view = CheckboxTreeview(master=top_frame, yscrollcommand = scrollbar.set)
        self.view.heading("#0", text = "JenkinsJobs")
        scrollbar.config(command = self.view.yview)
        self.view.pack(side = TOP, fill = 'both', expand = 'yes')
        self.get_jobs()
        top_frame.pack(side=TOP, fill = "both", expand = "yes", padx = 5, pady=5)
        ok_button = Button(bottom_frame, text = "OK", width = 10, background = "gray89", foreground = "gray1",command = lambda:self.on_ok())
        ok_button.pack(side = LEFT, padx = 5, pady=5)
        cancel_button = Button(bottom_frame, text = "Close", width = 10,background = "gray89", foreground = "gray1", command = lambda:self.on_close())
        cancel_button.pack(side = RIGHT, padx = 5, pady=5)
        bottom_frame.pack(side=BOTTOM, fill = "both",padx = 5, pady=5)
        
    @start_thraed()
    def get_jobs(self):
        for i in self.jenkins_obj.get_all_jobs():
            self.view.insert('', 'end', i.get("name"), text = i.get("name"))
    
    @start_thraed()
    def on_ok(self):
        self.job = self.view.get_checked()[0]
        self.select_job.configure(state = ACTIVE)
        _destroy_widget(self, "select_script")
        self.jenkins_obj.build_job(self.job)
    
    def on_close(self):
        self.select_job.configure(state = ACTIVE)
        _destroy_widget(self, "select_script")
    
    @start_thraed()
    def on_result(self):
        result = self.jenkins_obj.get_build_report(self.job)
        self.failcount = result.get("failCount")
        self.failed_label = Label(self.select_frame, text = "Failed: {}".format(result.get("failCount")), bg = "Red2",width = 20)
        self.passed_label = Label(self.select_frame, text = "Passed: {}".format(result.get("passCount")), bg ="Green", width = 20)
        self.skipped_label = Label(self.select_frame, text = "Skipped: {}".format(result.get("skipCount")), bg ="Yellow", width = 20)
        self.failed_label.grid(row = 0, column = 3, padx = 5, pady = 5)
        self.passed_label.grid(row = 1, column = 3, padx = 5, pady = 5)
        self.skipped_label.grid(row = 2, column = 3, padx = 5, pady = 5)
    
    @start_thraed() 
    def on_console(self):
        console_output = self.jenkins_obj.get_console_output(self.job);
        self.scrolled_text.insert(END, console_output, "DEFAULT");
    
    @start_thraed()
    def on_build_status(self):
        if self.failcount > 0:
            self.fail_lable = Label(self.select_frame, text = "Build Status : Unstable", bg = "red2", width = 20)
            self.fail_lable.grid(row = 0, column = 4, padx = 5, pady = 5)
        else:
            self.pass_label = Label(self.select_frame, text = "Build Status : Stable", bg = "green", width = 20)
            self.pass_label.grid(row = 0, column = 4)
    
    @start_thraed()
    def on_reset(self):
        self.jenkins_url_entry.delete("0","end")
        self.username_entry.delete("0","end")
        self.password_entry.delete("0","end")
    
if __name__ == "__main__":
    root = Tk()
    JenkinsBuildTrigger(root)
    root.mainloop()
