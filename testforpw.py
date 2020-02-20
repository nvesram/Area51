# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:51:26 2020

@author: 1184952
"""


import tkinter as tk
from tkinter import ttk
import subprocess,psutil
import shutil, os


def killer():
    subprocess.Popen(['powershell.exe',r'C:\Users\1184952\Documents\Python\TKINTER\BatchKiller.ps1'])
    amb = tk.Tk()
    tk.Label(amb,text = "Process killed").pack()
    tk.Button(amb,text = "OK", command = amb.destroy).pack()
    amb.mainloop()

def restart():
    subprocess.Popen(['powershell.exe',r'C:\Users\1184952\Documents\Python\TKINTER\Restarter.ps1'])
    rst = tk.Tk()
    tk.Label(rst,text = "Task have been enabled and started successfully").pack()
    tk.Button(rst,text = "OK", command = rst.destroy).pack()
    rst.mainloop()

def svc():
    serv = tk.Tk()
    s= psutil.win_service_get("AJRouter").as_dict()['status']
    tk.Label(serv, text = 'The AJRouter service is').pack()
    ttk.Label(serv, text = s).pack()
    tk.Button(serv,text = "OK", command = serv.destroy).pack()
    serv.mainloop()


def bat():
    bats = tk.Tk()
    rl = subprocess.Popen(['powershell.exe',r'C:\Users\1184952\Documents\Python\TKINTER\ServiceCheck.ps1'],stdout = subprocess.PIPE)
    result = rl.stdout.read()
    ttk.Label(bats, text = result).pack()
    tk.Button(bats,text = "OK", command = bats.destroy).pack()
    bats.mainloop()

def cop():
    try:
        src1 = r'C:\Users\1184952\Documents\Apps_Anark\Anark'
        src2 = r'C:\Users\1184952\Documents\Apps_Anark\AnarkCoreServerClientConnectorApplication\ACSCLI.exe.config'
        src3 = r'C:\Users\1184952\Documents\Apps_Anark\AnarkCoreServerClientConnectorApplication\ACSCLI.exe'
        src4 = r'C:\Users\1184952\Documents\Apps_Anark\Anark\Anark Core Server\CadTransformerWebInterface\bin\CoreNX11OpenTranslator.exe'
        src5 = r'C:\Users\1184952\Documents\Apps_Anark\Anark\Anark Core Server\CadTransformerWebInterface\bin\CoreNXOpenTranslator.exe'
        src6 = r'C:\Users\1184952\Documents\Apps_Anark\Anark\Anark Core Server\CadTransformerWebInterface\bin\Formats\NXAdvancedFormat.dll.config'
        src7 = r'C:\Users\1184952\Documents\Apps_Anark\Anark\Anark Core Server\CoreDaemon\Preferences\Prefs.xml'
        os.chdir("C:\\Users\\1184952\\Documents\\")
        os.mkdir(r'Anark_Backup')
        des1 = r'C:\Users\1184952\Documents\Anark_Backup\Anark'
        des2 = r'C:\Users\1184952\Documents\Anark_Backup\ACSCLI.exe.config'
        des3 = r'C:\Users\1184952\Documents\Anark_Backup\ACSCLI.exe'
        des4 = r'C:\Users\1184952\Documents\Anark_Backup\CoreNX11OpenTranslator.exe'
        des5 = r'C:\Users\1184952\Documents\Anark_Backup\CoreNXOpenTranslator.exe'
        des6 = r'C:\Users\1184952\Documents\Anark_Backup\NXAdvancedFormat.dll.config'
        des7 = r'C:\Users\1184952\Documents\Anark_Backup\Prefs.xml'
        shutil.copytree(src1,des1)
        shutil.copyfile(src2,des2)
        shutil.copyfile(src3,des3)
        shutil.copyfile(src4,des4)
        shutil.copyfile(src5,des5)
        shutil.copyfile(src6,des6)
        shutil.copyfile(src7,des7)
        cp = tk.Tk()
        ttk.Label(cp, text = "Files backup completed").pack()
        tk.Button(cp,text = "OK", command = cp.destroy).pack()
        cp.mainloop() 
    except PermissionError:
        cp = tk.Tk()
        ttk.Label(cp, text = "No Permission to copy").pack()
        tk.Button(cp,text = "OK", command = cp.destroy).pack()
        cp.mainloop()  
    except :
        cp = tk.Tk()
        ttk.Label(cp, text = "Files not copied").pack()
        tk.Button(cp,text = "OK", command = cp.destroy).pack()
        cp.mainloop()
            
root = tk.Tk()
ttk.Button(root,text = "Batch Status", command = bat).pack()
ttk.Button(root,text = "Core Service Status", command = svc).pack()
ttk.Button(root,text= "Enable and RESTART", command = restart).pack()
ttk.Button(root,text= "Disable and KILL", command = killer).pack()
ttk.Button(root,text = "Backup", command = cop).pack()
ttk.Button(root,text = "EXIT", command = root.destroy).pack()

root.mainloop()
