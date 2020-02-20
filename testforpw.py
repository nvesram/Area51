# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:51:26 2020

@author: 1184952
"""


import tkinter as tk
from tkinter import ttk
import subprocess,psutil


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


root = tk.Tk()
ttk.Button(root,text = "Batch Status", command = bat).pack()
ttk.Button(root,text = "Core Service Status", command = svc).pack()
ttk.Button(root,text= "Enable and RESTART", command = restart).pack()
ttk.Button(root,text= "Disable and KILL", command = killer).pack()
ttk.Button(root,text = "EXIT", command = root.destroy).pack()

root.mainloop()