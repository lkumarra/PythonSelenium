'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import json
import os
currentdir = os.getcwd()
f = open(".Confing.json")
data = json.load(f)
print(data["browser"])
print(currentdir)
