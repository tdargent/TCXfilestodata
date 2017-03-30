# -*- coding: utf-8 -*-

import os,tcxparser
import numpy as np

cd = os.path.dirname(os.path.abspath(__file__)) #use to browse tcx files at the correct location
file_list=os.listdir(os.getcwd())
b=[]

for a in file_list:
    if a == "result.txt": 
        print()     #Quick and dirty...
    elif a== "readTCXFiles.py":
        print()     #Quick and dirty...
    else:    
        tcx=tcxparser.TCXParser(cd+'/'+a) #see https://github.com/vkurup/python-tcxparser/ for details
        if tcx.activity_type == 'biking'  :  #To select only my biking session (could be change to 'hiking', 'running' etc.)
            b.append((tcx.completed_at,tcx.distance,tcx.duration))
         

