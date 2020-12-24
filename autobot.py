# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:32:10 2020

@author: Sen
"""
import tkinter as tk
from tkinter import ttk
import time
import sys
import os
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
import threading

mouse = MouseController()
Keys = {"ALT": Key.alt, "LALT":Key.alt_l, "RALT":Key.alt_r, "CAPSLOCK":Key.caps_lock, "BS":Key.backspace, "BACKSPACE": Key.backspace,
        "CMD":Key.cmd, "LCMD":Key.cmd_l, "RCMD": Key.cmd_r, "DELETE":Key.delete,"DEL":Key.delete, "END":Key.end, "ENTER": Key.enter, "F1": Key.f1,
        "F2": Key.f2,"F3": Key.f3,"F4": Key.f4,"F5": Key.f5,"F6": Key.f6,"F7": Key.f7,"F8": Key.f8,"F9": Key.f9,"F10": Key.f10,"F11": Key.f11,"F12": Key.f12,
        "LEFT":Key.left, "RIGHT": Key.right, "UP": Key.up, "DOWN": Key.down, "SHIFT":Key.shift, "LSHIFT":Key.shift_l, "RSHIFT":Key.shift_r, "SPACE":Key.space}
keyboard = Controller()
root = tk.Tk()
root.title("AutoBotV1")
varForeverKey = tk.IntVar()
varForKey = tk.IntVar()
mbvar=tk.IntVar()
#ELEMENTS ---------------------------------------------------------------------
butt=False
keySequence = []
buttonSequence = []
def stop():
    root.after(1000, stopa)

def stopa():
    global butt
    butt=True
    thread.join()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def errorcatch():
    global err
    err="error"
    inputtypes = {delay:"delay", typeinfo:"text input", setInterval:"interval", setReps:"repetitions"}
    for inputt in inputtypes:
        inpkey = inputtypes[inputt]
        try:
            inputt.get()
        except:
            msg="Enter a value for " + inpkey + "."
            tk.messagebox.showerror(title="Error", message=msg)
            return(err)
def click():
    catch = errorcatch()
    if catch == err:
        stop()
    typeEntry = typeinfo.get() 
    if varx.get() != "Keypress Menu":
        keyAdded = Keys[varx.get()]
        keySequence.append(typeEntry)
        keySequence.append(keyAdded)
    else:
        keySequence.append(typeEntry)
    delaytime = int(delay.get())
    time.sleep(delaytime)
    interval = int(setInterval.get())
    if varForKey.get() == 1 and varForeverKey.get() == 0:
        reps = int(setReps.get())
        for repetition in range(reps):
            time.sleep(interval)
            keyboard.type(keySequence[0])              
            keyboard.press(keySequence[1])
        stop()
    elif varForeverKey.get() == 1 and varForKey.get() == 0:
        while True:
            time.sleep(interval)
            if butt==True:
                break
            for key in keySequence:
                if isinstance(key, str):
                    keyboard.type(key)  
                else:
                    keyboard.press(key)
thread = threading.Thread(target=click)
thread.daemon=True
tabs = ttk.Notebook(root)
tabs.grid()
autotyper= tk.Frame(tabs, width=600, height=400, bg="white")
autoclicker= tk.Frame(tabs, width=300, height=200, bg="white")
autotyper.grid(row=0, column=0)
autoclicker.grid(row=0,column=1)
tabs.add(autotyper, text="AutoTyper")
tabs.add(autoclicker, text="AutoClicker")
typerinputs = tk.LabelFrame(autotyper, text="Input Settings", labelanchor='nw', bg='white')
typerinputs.place(x=200, y=0, width = 150, height=179) 
typeroptions = tk.LabelFrame(autotyper, text="Options", bg="white")
typeroptions.place(x=30, y=70)
autostart =tk.Button(autotyper, text="START AUTOTYPER", fg="black", font = "arial 12 bold", command=thread.start) 
setdelaylabel = tk.Label(typerinputs, text="Set Delay Until Start:", fg="black", bg="white", font = "arial 8")
tk.Label(typerinputs, text="Enter Text Here:", fg="black", bg="white",font = "arial 8") .grid(row=0, column=1)
typeinfo = tk.Entry(typerinputs, width=20, bg="white", font = "arial 8")
delay = tk.Entry(typerinputs, width=20, bg="white", font = "arial 8")
keypresscats = list(Keys.keys())
varx=tk.StringVar(autotyper)
varx.set("Keypress Menu")
keyPresses = tk.OptionMenu(typeroptions, varx, *keypresscats)
keyPresses.config(bg="WHITE")
setInterval = tk.Entry(typerinputs, width=20, bg="white", font = "arial 8")
setIntervalLabel = tk.Label(typerinputs, text="Enter Interval Here:",bg="white", font = "arial 8")
setReps = tk.Entry(typerinputs, width=20, bg="white", font="arial 8")
setRepLabel = tk.Label(typerinputs, text="Enter Repetitions Here:", bg="white",font = "arial 8") .grid(row=7, column=1)
runForever = tk.Checkbutton(typeroptions, text="Run Forever", variable=varForeverKey, bg="white",font = "arial 8") .grid(row=7, column=0,sticky=tk.W)
runFor = tk.Checkbutton(typeroptions, text="Run For:", variable=varForKey, bg="white",font = "arial 8") .grid(row=6, column=0, sticky=tk.W)
stopbutt = tk.Button(autotyper, text=" STOP AUTOTYPER ", command=stop, font = "arial 10").place(x=25, y=40)
tk.Label(typerinputs, text=" ", fg="white", bg="white") .grid(row=0, column=0)

#
##ELEMENTS ---------------------------------------------------------------------
forkey = tk.IntVar()
foreverkey = tk.IntVar()
emptyList=[]
def esc():
    root.destroy()
    exit(0)
def stop2():
    clickthread.join()
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def AddButt():
    sel=mbvar.get()
    print(sel)
    mbdic={0:Button.left, 1:Button.right, 2:"scroll"}
    buttonSequence.append(mbdic[sel])
def ClearButt():
    buttonSequence.clear()
def StartButt():
    intervalsmouse = int(interm.get())
    print(forkey.get())
    print(foreverkey.get())
    if forkey.get()==1 and foreverkey.get()==0:
        repsform = int(repsm.get())
        for repe in range(repsform):
            time.sleep(intervalsmouse)
            for button in buttonSequence:
                mouse.press(button)
                mouse.release(button)
    elif foreverkey.get()==1 and forkey.get()==0:
        while True:
            time.sleep(intervalsmouse)
            for button in buttonSequence:
                    mouse.press(button)
                    mouse.release(button)
clickthread = threading.Thread(target=StartButt)
clickthread.daemon = True
#ELEMENTS AUTOCLICKER ---------------------------------------------------------
mbframe = tk.LabelFrame(autoclicker, text="Select Mouse Buttons", bg="white")
mbframe.place(x=200,y=0)
mbinps = tk.LabelFrame(autoclicker, text="Input Settings", bg="white")
mbinps.place(x=10, y=90)
mbops = tk.LabelFrame(autoclicker, text="Options", bg="white")
mbops.place(x=200, y=100)
tk.Label(autoclicker, text="V1", font="arial 15 bold", bg="white") .place(x=310, y=102)
tk.Button(autoclicker, text="ESC", font="arial 13 bold", command=esc) .place(x=300, y=130)
tk.Radiobutton(mbframe, text="Left Click                    ", variable=mbvar, value=0, bg="white").grid(row=1, column=0, sticky=tk.W)
tk.Radiobutton(mbframe, text="Right Click                   ", variable=mbvar, value=1, bg="white").grid(row=2, column=0, sticky=tk.W)
tk.Button(mbframe, text="Append Seq.", command=AddButt,) .grid(row=3, column=0,sticky=tk.W)
tk.Button(mbframe, text="Clear Seq.", command=ClearButt) .grid(row=3, column=0, sticky=tk.E)
tk.Label(mbinps, text="   Repetitions:  ", bg="white") .grid(row=6, column=0, sticky=tk.W)
repsm = tk.Entry(mbinps, width=11)
repsm.grid(row=7, column=0)
tk.Label(mbinps, text="", bg="white") .grid(row=8,column=0)
tk.Button(autoclicker, text="START AUTOCLICKER", command=clickthread.start, font="arial 12 bold" ) .grid(row=0, column=0, padx=4, pady=8)
tk.Label(mbinps, text="        Intervals:        ", bg="white") .grid(row=6, column=1, sticky=tk.E)
interm = tk.Entry(mbinps, width=10)
interm.grid(row=7, column=1) 
runforms = tk.Checkbutton(mbops, text="Run For:", variable=forkey, bg="white") .grid(row=6, column=3,sticky=tk.W)
runforeverms = tk.Checkbutton(mbops, text="Run Forever", variable=foreverkey, bg="white") .grid(row=7, column=3, sticky=tk.W)
stopauto = tk.Button(autoclicker, text="STOP AUTOCLICKER", command=stop2, font="arial 10") .grid(row=2, column=0)
#ELEMENTS AUTOCLICKER ---------------------------------------------------------

#GRIDDING AUTOCLICKER----------------------------------------------------------

#GRIDDING AUTOCLICKER----------------------------------------------------------

#GRIDDING----------------------------------------------------------------------
autostart.place(x=10,y=4)
setdelaylabel.grid(row=3, column=1)
typeinfo.grid(row=2, column=1)
delay.grid(row=4, column=1)             
setIntervalLabel.grid(row=5, column=1)
setInterval.grid(row=6, column=1)
keyPresses.grid(row=2, column=0)
setReps.grid(row=8, column=1)
#GRIDDING----------------------------------------------------------------------


root.geometry('360x208')
root.iconbitmap(r"autoboticon_EPr_icon.ico")
root.configure(bg="white")
root.mainloop()
