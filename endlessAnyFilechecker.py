import os
import re
import keyboard as key
import time
from datetime import datetime

print("*************************************************************")
print("1.Welcome user,this software design for find perticular extension  file  or files in given folder and sub folder")
print("2.Main motive behind this softaware is find perticular file or files as Fast Compare to as Your 'File Explorer' aplication")
print("3.this software find file by extension name also any word contain in file name")
print("4.This software can scan any extension files")
print("5.Our software Scan upto last folder that contain in parent folder (as hierarchical manner)")
print("*************************************************************")

def askusr(flds):
    print("Also We Create log file of your search on you provided path")
    chsc=input("Press f or F ,else press any key: ")
    if (chsc=="f" or chsc=="F"):
        os.system(flds)        
    print("\U0001F618",end="")
    print("Thank You For Using Our Software",end="")
    print("\U0001F917")
    print("1.Press q or Q for exit")
    print("2.Press y or Y for Search again")

def runme():
    flds="log"
    frc=input("## \t Enter file extension name(as like pdf,mp4,jpg,mp3,exe etc): ")
    fcrg='.*.'+frc
    
    dtnov=datetime.now()
    dtnov=dtnov.strftime("%H-%M-%S")
    flds=flds+"_"+frc+"_"+str(dtnov)+".txt"
    ar1=[]
    while True:
        dr=input("Provide full path , where your file or files have:")
        if os.path.isdir(dr):
            break
        else:
            print("#! Alert ,Try again ,your specified directory/folder location not found")
    flds=dr+"/"+flds
    flobj=open(flds,"w")
    print("****************************")
    for fo1,fo2,fo3 in os.walk(dr,topdown=True):
        ar2=[]
        ar2.append(fo1)
        for i in fo3:
            mh=re.match(fcrg,i)
            if "None" != str(mh):
                print(mh.group(),end="\n")
                ar2.append(mh.group())
        ar1.append(ar2)
    
    fcount=0
    while True:
        condc=False
        print("\n1.Search a file:")
        print("2.Exit")
        chs=input("\nEnter Your choice:")
        try:
            chs=int(chs)
            if(chs==1):
        
                nmof=input("Enter any keyword that contain in your file name ,from shown above list of files, for searching purpous of perticular file or files: ")         
                for i in ar1:
                    for j in range(0,len(i)):
                        if(j!=0):
                           nmof1=re.search(nmof,i[j])
                           if nmof1:
                               fpath=os.path.join(i[0],i[j])
                               fpaths=os.path.getsize(fpath)
                               path1=f"{i[j]} \t present in\t {i[0]} \t location and full path is\n {fpath} \n and Size is :{os.path.getsize(fpath)/(1024*1024)} MB" 
                               print(path1)
                               print("")
                               flobj.write(path1)
                               flobj.write("\n***************************************************************\n")
                               fcount+=1
                               condc=True
                if condc:
                    print(f"Total File Count is {fcount}")
                    break
                else:
                    print("\n::File not found , Try again::\n")  
            elif(chs==2):
                break
            else:
                print("\nWrong Choice Entred::\n")
                    
        except:
            print("\n::Please enter Integer choice::\n")
    flobj.close()
    time.sleep(0.5)
    askusr(flds)
runme()

while True:
    if (key.is_pressed("q") or key.is_pressed("Q")):
        break
    elif (key.is_pressed("y") or key.is_pressed("Y")):
        runme()
    time.sleep(0.1)