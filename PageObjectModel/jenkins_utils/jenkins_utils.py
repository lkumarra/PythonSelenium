"""
Created on 28-May-2020
@author: Lavendra rajput
"""
import jenkins
import time

JENKINS_URL = "http://localhost:8080/"
JENKINS_USERNAME = "lavendra"
JENKINS_PASSWORD = "Lav123456@"

class DevOpsJenkins:
    def __init__(self):
        self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        user = self.jenkins_server.get_whoami()
        version = self.jenkins_server.get_version()
        print ("Jenkins Version: {}".format(version))
        print ("Jenkins User: {}".format(user['id']))

    def build_job(self, name, parameters=None, token=None):
        next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        self.jenkins_server.build_job(name, parameters=parameters, token=token)
        time.sleep(10)
        build_info = self.jenkins_server.get_build_info(name, next_build_number)
        return build_info
    
    def build_stop(self,name):
        self.jenkins_server.stop_build(name, self.jenkins_server.get_job_info(name)['nextBuildNumber']-1)
        
    def get_console_output(self, name):
        return self.jenkins_server.get_build_console_output(name,  self.jenkins_server.get_job_info(name)['nextBuildNumber']-1)

if __name__ == "__main__":
    NAME_OF_JOB = "Python_Automation_Framework"
    TOKEN_NAME = "python_automation_framework"
    # Example Parameter
    PARAMETERS = None
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    print ("Jenkins Build URL: {}".format(output['url']))