'''
Created on 27-Sep-2020

@author: Lavendra rajput
'''

from jenkins import *;

class JenkinsUtils:
    
    def __init__(self, jenkins_url, username, password):
        self.jenkins_url = jenkins_url
        self.username = username
        self.password = password
        self.jenkins_server = Jenkins(self.jenkins_url, username=self.username, password=self.password)
        print(self.jenkins_server.get_version())
        
        
    def get_jenkins_version(self):
        return self.jenkins_server.get_version();
    
    def build_job(self, name):
        self.jenkins_server.build_job(name, None, None)
    
    def build_stop(self, name):
        self.jenkins_server.stop_build(name, self.jenkins_server.get_job_info(name)["currentBuildNumber"])
    
    def get_console_output(self, name):
        pass        