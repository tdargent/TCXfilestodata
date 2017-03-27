# -*- coding: utf-8 -*-

import os,tcxparser

cd = os.path.dirname(os.path.abspath(__file__)) #retourne le dossier dans lequel est enregistre ce code python"
print(cd) 

path=os.getcwd() #retourne le dossier dans lequel est enregistre ce code python"
print(path)

file_list=os.listdir(os.getcwd())

f=open("result.txt","a")
f.write("date (ISO UTC Format)"+'\t'+"Distance [m]"+'\t'+"Duration [s]"+'\n')
for a in file_list:
    if a == "result.txt": 
        print()
    elif a== "readTCXFiles.py":
        print()
    else:    
        tcx=tcxparser.TCXParser(cd+'/'+a)
        if tcx.activity_type == 'biking'  :  
            #print(tcx.completed_at,tcx.distance,tcx.duration)
            #f=open("result.txt","a")
            f.write(str(tcx.completed_at)+'\t'+str(tcx.distance)+'\t'+str(tcx.duration)+'\n')

f.close			
print("Done.")
