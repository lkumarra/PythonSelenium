from tkinter import *
import subprocess
import shlex
import signal
import threading

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

class ScriptRunner:
    
    def __init__(self, obj):
        self.root = obj
        self.root.title("Guru99Bank Script Runnner")
        self.root.geometry("1000x600")
        self.pm = PanedWindow(self.root, orient = VERTICAL, sashpad = 4, sashrelief = 'raised', sashwidth = 6)
        self.console_frame = Frame(self.root, padx = 3, pady = 3)
        self.console_frame.rowconfigure(0, weight = 1)
        self.console_frame.columnconfigure(0, weight = 1)
        self.pm.add(self.console_frame)
        self.pm.paneconfigure(self.console_frame, minsize=135)
        self.label_frame = LabelFrame(self.console_frame, text = "Console", padx = 5, pady = 5, font = "TkHeadingFont", background = "white smoke", borderwidth = 4,foreground = "gray1")
        self.select_frame = LabelFrame(self.console_frame, text = "Script", padx = 5, pady = 5, font = "TkMenuFont", background = "white smoke", borderwidth = 4, foreground = "Red")
        self.my_menu = Menu(self.root)
        self.selectscript_button = Button(self.select_frame, text = "Select Script", padx = 5, pady =5, height=1, width=8,highlightthickness=4,background = "white")
        self.runallscript_button = Button(self.select_frame, text = "Run all Script", padx = 5, pady =5, height=1, width=8,highlightthickness=4,background = "white", command = self.start_execution)
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
        self.label_frame.grid(row = 1, column = 0, sticky = E+W+N+S)
        self.selectscript_button.grid(row = 0, column = 0)
        self.runallscript_button.grid(row = 0, column = 1)
        self.select_frame.grid(row =0, column = 0, sticky = E+W+N+S)
        self.scrolled_text.tag_config("DEBUG", foreground ="RoyalBlue1")
        self.scrolled_text.tag_config("DEFAULT", foreground ="snow")
        self.scrolled_text.tag_config("STOP", foreground = "Red", font = "bold")
        self.scrolled_text.tag_config("RUNNINGIT", foreground ="cyan")
        self.scrolled_text.tag_config("RUNNINGTEST", foreground ="slate blue")
        self.scrolled_text.tag_config("SUCCESS", foreground ="SpringGreen2")
        self.scrolled_text.tag_config("FAILED", foreground ="Red2")
        self.scrolled_text.tag_config("PASSED", foreground = "SpringGreen2")
        self.scrolled_text.tag_config("FAILURES", foreground = "Red2", font="bold")
        self.root.config(menu = self.my_menu)
        self.file_menu =Menu(self.my_menu)
        self.my_menu.add_cascade(label = "Script", menu = self.file_menu)
        self.file_menu.add_command(label = "Select Script", command = "")
        self.pm.pack(fill = BOTH, expand = 1)
        self.process = None
        
    @start_thraed()
    def start_execution(self):
        '''Send a coommand to start execution and send output to console'''
        self.process = subprocess.Popen(shlex.split("cd test_case & py.test --html=../test_report/report.html -v -s --junitxml='../test_report/report.xml' --alluredir=../test_report/allure_results"), stdout=subprocess.PIPE, shell=True)
        while True:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                string_output = str(output.strip())
                if "DEBUG" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "DEBUG")
                elif "Running IT" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "RUNNINGIT")
                elif "Running test:" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "RUNNINGTEST")
                elif "SUCCESS" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "SUCCESS")
                elif "FAILED" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILED")
                elif "Failures" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILURES")
                elif "Failed" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILED")
                elif '32m' in string_output:
                    self.scrolled_text.insert(END, output.strip(), "PASSED")
                elif '31m' in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILED")
                else:
                    self.scrolled_text.insert(END, output.strip(), "DEFAULT")
                self.scrolled_text.insert(END, "\n", "DEBUG")
    
    @start_thraed()
    def install_library(self):
        '''Send a command to install all dependencies and send output to console'''
        install_process = subprocess.Popen(shlex.split("npm install"), stdout=subprocess.PIPE, shell=True)
        while True:
            output = install_process.stdout.readline()
            if output == '' and install_process.poll() is not None:
                break
            if output:
                self.scrolled_text.insert(END, output.strip(), "DEFAULT")
                self.scrolled_text.insert(END, "\n", "DEBUG")

    @start_thraed()
    def webdriver_update(self):
        '''Send a command to Update Webdriver and send output to console'''
        update_process = subprocess.Popen(shlex.split("npm run webdrivermanager:update"), stdout=subprocess.PIPE, shell=True)
        while True:
            output = update_process.stdout.readline()
            if output == '' and update_process.poll() is not None:
                break
            if output:
                self.scrolled_text.insert(END, output.strip(), "DEFAULT")
                self.scrolled_text.insert(END, "\n", "DEBUG")

    @start_thraed()
    def stop_execution(self):
        '''Send a command to stop execution'''
        self.process.send_signal(signal.CTRL_BREAK_EVENT)


if __name__ == "__main__":
    root = Tk()
    ScriptRunner(root)
    root.mainloop()
    