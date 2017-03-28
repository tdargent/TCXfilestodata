# -*- coding: utf-8 -*-

import os,tcxparser

file_list=os.listdir(os.getcwd())

f=open("result.txt","a")
f.write("date (ISO UTC Format)"+'\t'+"Distance [m]"+'\t'+"Duration [s]"+'\n')
for a in file_list:
    if a == "result.txt": 
        print()     #Quick and dirty...
    elif a== "readTCXFiles.py":
        print()     #Quick and dirty...
    else:    
        tcx=tcxparser.TCXParser(cd+'/'+a) #see https://github.com/vkurup/python-tcxparser/ for details
        if tcx.activity_type == 'biking'  :  #To select only my biking session (could be change to 'hiking', 'running' etc.)
            f=open("result.txt","a")
            f.write(str(tcx.completed_at)+'\t'+str(tcx.distance)+'\t'+str(tcx.duration)+'\n')

f.close
