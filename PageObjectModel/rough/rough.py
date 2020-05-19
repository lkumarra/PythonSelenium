'''
Created on 27-Apr-2020

@author: Lavendra rajput
'''
import json
import os
currentdir = os.getcwd()
fileName = "../Config/Confing.json"
f = open(fileName)
data = json.load(f)
print(data["browser"])
print(currentdir)
