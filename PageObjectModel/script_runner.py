from tkinter import *
import subprocess
import shlex
import signal
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

class ScriptRunner():
    
    def __init__(self, obj):
        self.root = obj
        self.root.title("Guru99Bank Script Runnner")
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
        self.selectscript_button = Button(self.select_frame, text = "Select Script", padx = 5, pady =5, width=9,highlightthickness=2,background = "gray89", foreground = "gray1",command = self.select_script_window, borderwidth =3)
        self.runallscript_button = Button(self.select_frame, text = "Run all Script", padx = 5, pady =5,  width=9,highlightthickness=2,background = "gray89", foreground = "gray1", command = self.start_execution, borderwidth =3)
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
        self.selectscript_button.pack(side = LEFT, padx = 5, pady = 5)
        self.runallscript_button.pack(side = RIGHT, padx = 5, pady = 5)  
        self.select_frame.grid(row =0, column = 0, sticky = E+W+N+S, padx = 5, pady = 5)
        self.scrolled_text.tag_config("DEBUG", foreground ="RoyalBlue1")
        self.scrolled_text.tag_config("DEFAULT", foreground ="snow")
        self.scrolled_text.tag_config("STOP", foreground = "Red", font = "bold")
        self.scrolled_text.tag_config("FAILED", foreground ="Red2")
        self.scrolled_text.tag_config("PASSED", foreground = "SpringGreen2")
        self.scrolled_text.tag_config("FAILURES", foreground = "Red2", font="bold")
        self.scrolled_text.tag_config("WARNING", foreground = "yellow")
        self.pm.pack(fill = BOTH, expand = 1)
        self.process = None
    
    @start_thraed()
    def select_script_window(self):
        self.selectscript_button.configure(state = DISABLED)
        self.select_script = Toplevel(self.root)
        self.select_script.title("Select Script")
        self.select_script.focus_force()
        self.select_script.geometry("600x800")
        self.select_script.minsize(width=500, height=700)
        top_frame = LabelFrame(self.select_script, text = "Select Script", padx = 5, pady = 5, font = "TkHeadingFont", background = "light grey", borderwidth = 8,foreground = "gray1")
        bottom_frame = LabelFrame(self.select_script, text = "Buttons", padx = 5, pady = 5, font = "TkHeadingFont", background = "light grey", borderwidth = 8,foreground = "gray1")
        scrollbar = Scrollbar(top_frame)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.view = CheckboxTreeview(master=top_frame, yscrollcommand = scrollbar.set)
        self.view.heading("#0", text = "Guru99Bank")
        scrollbar.config(command = self.view.yview)
        self.view.pack(side = TOP, fill = 'both', expand = 'yes')
        self.get_script()
        top_frame.pack(side=TOP, fill = "both", expand = "yes", padx = 5, pady=5)
        ok_button = Button(bottom_frame, text = "OK", width = 10, background = "gray89", foreground = "gray1",command = lambda:self.on_ok())
        ok_button.pack(side = LEFT, padx = 5, pady=5)
        cancel_button = Button(bottom_frame, text = "Close", width = 10,background = "gray89", foreground = "gray1", command = lambda:self.on_close())
        cancel_button.pack(side = RIGHT, padx = 5, pady=5)
        bottom_frame.pack(side=BOTTOM, fill = "both",padx = 5, pady=5)

    @start_thraed()
    def on_ok(self):
        script = self.view.get_checked()[0]
        self.selectscript_button.configure(state = ACTIVE)
        _destroy_widget(self, "select_script")
        self.insert_output("cd test_case & py.test "+script+" --html=../test_report/report.html -v -s --junitxml='../test_report/report.xml' --alluredir=../test_report/allure_results")
        
    def on_close(self):
        self.selectscript_button.configure(state = ACTIVE)
        _destroy_widget(self, "select_script")
    
    @start_thraed()
    def get_script(self):
        import glob, os
        os.chdir(r"C:\Users\Lavendra rajput\git\PythonSelenium\PageObjectModel\test_case")
        for file in glob.glob("test_*.py"):
            self.view.insert('', 'end', file, text = file)
        
    @start_thraed()
    def start_execution(self):
        '''Send a coommand to start execution and send output to console'''
        self.insert_output("cd test_case & py.test --html=../test_report/report.html -v -s --junitxml='../test_report/report.xml' --alluredir=../test_report/allure_results")
                
    def insert_output(self, command):
        self.process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, shell=True)
        while True:
            output = self.process.stdout.readline()
            if output == '' and self.process.poll() is not None:
                break
            if output:
                string_output = str(output.strip())
                if "DEBUG" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "DEBUG")
                elif "FAILED" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILED")
                elif "FAILURES" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILURES")
                elif "Failed" in string_output:
                    self.scrolled_text.insert(END, output.strip(), "FAILED")
                elif 'PASSED' in string_output:
                    self.scrolled_text.insert(END, output.strip(), "PASSED")
                elif 'passed' in string_output:
                    self.scrolled_text.insert(END, output.strip(), "PASSED")
                elif 'warnings summary' in string_output:
                    self.scrolled_text.insert(END, output.strip(), "WARNING")
                else:
                    self.scrolled_text.insert(END, output.strip(), "DEFAULT")
                self.scrolled_text.insert(END, "\n", "DEFAULT")
    
    @start_thraed()
    def stop_execution(self):
        '''Send a command to stop execution'''
        self.process.send_signal(signal.CTRL_BREAK_EVENT)


if __name__ == "__main__":
    root = Tk()
    ScriptRunner(root)
    root.mainloop()
    