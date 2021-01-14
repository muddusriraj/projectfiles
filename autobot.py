# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 21:32:10 2020

@author: Sriraj
"""
import tkinter as tk
from tkinter import ttk
import time
import sys
import os
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController
import threading
##CLASSES AND PREREQS
exitval = 0
butt=False
keySequence = []
buttonSequence = []
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
class AutoTyperFunc:
    def stop(self):
        root.after(1000, AutoTyperFunc.stopA)
    def stopA():
        if threading.get_ident() != None:
            root.destroy()
            python = sys.executable
            os.execl(python, python, *sys.argv)
    def errCatch(self):
        inputtypes = {delay:"delay", typeinfo:"text input", setInterval:"interval", setReps:"repetitions"}
        inputt = list(inputtypes.keys())[0]
        inpkey = inputtypes[inputt]
        try:
            int(inputt.get())
        except:
            msg="Enter a value for " + inpkey + "."
            tk.messagebox.showerror(title="Error", message=msg)
            return
        inputt = list(inputtypes.keys())[2]
        inpkey = inputtypes[inputt]
        try:
            int(inputt.get())
        except:
            msg="Enter a value for " + inpkey + "."
            tk.messagebox.showerror(title="Error", message=msg)
            return
        inputt = list(inputtypes.keys())[3]
        inpkey = inputtypes[inputt]
        if varForKey.get() == 1:
            try:
                int(inputt.get())
            except:
                msg="Enter a value for " + inpkey + "."
                tk.messagebox.showerror(title="Error", message=msg)
                return
        if varForKey.get() == 0 and varForeverKey.get() == 0:
            tk.messagebox.showerror(title="Error", message="Select either Run For: or Run Forever")
            return
        thread.start()
    def click(self):
        typeEntry = typeinfo.get() 
        if varx.get() != "Keypress Menu":
            keymenu = True
            keyAdded = Keys[varx.get()]
            keySequence.append(typeEntry)
            keySequence.append(keyAdded)
        else:
            keySequence.append(typeEntry)
            keymenu = False
        delaytime = int(delay.get())
        time.sleep(delaytime)
        interval = int(setInterval.get())
        if varForKey.get() == 1 and varForeverKey.get() == 0:
            reps = int(setReps.get())
            if keymenu==True:
                for repetition in range(reps):
                    time.sleep(interval)
                    keyboard.type(keySequence[0])              
                    keyboard.press(keySequence[1])
            elif keymenu==False:
                for repetition in range(reps):
                    time.sleep(interval)
                    keyboard.type(keySequence[0])
            AutoTyperFunc.stop(self)
        elif varForeverKey.get() == 1 and varForKey.get() == 0:
            while True:
                time.sleep(interval)
                for key in keySequence:
                    if isinstance(key, str):
                        keyboard.type(key)  
                    else:
                        keyboard.press(key)
forkey = tk.IntVar()
foreverkey = tk.IntVar()
emptyList=[] 
class AutoClickerFunc:
    def esc(self):
        root.destroy()
        sys.exit()
    def stop(self):
        root.after(1000, AutoClickerFunc.stopA)
    def stopA():
        if threading.get_ident() != None:
            root.destroy()
            python = sys.executable
            os.execl(python, python, *sys.argv)
    def AddButt(self):
        global buttonSequence
        sel=mbvar.get()
        mbdic={0:Button.left, 1:Button.right}
        buttonSequence.append(mbdic[sel])
    def errCatch(self):
        AutoClickerFunc.AddButt(self)
        try:
            int(interm.get())
        except:
            tk.messagebox.showerror(title="Error", message="Type an interval")
            return
        if forkey.get()==1 and foreverkey.get()==0:
            try:
                int(repsm.get())
            except:
                tk.messagebox.showerror(title="Error", message="Type the amount of repetitions you want or check Run Forever instead of Run For:")
                return
        if buttonSequence == emptyList:
            tk.messagebox.showerror(title="Error", message="Select Left or Right Click")
            return
        if foreverkey.get()==0 and forkey.get()==0:
            tk.messagebox.showerror(title="Error", message="Select either Run For: or Run Forever!")
            return
        clickthread.start()
    def StartButt(self):
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
            acf.stop()
        elif foreverkey.get()==1 and forkey.get()==0:
            while True:
                time.sleep(intervalsmouse)
                for button in buttonSequence:
                        mouse.press(button)
                        mouse.release(button)
##FUNCTIONS END

#ELEMENTS ---------------------------------------------------------------------

atf = AutoTyperFunc()
thread = threading.Thread(target=atf.click)
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
autostart =tk.Button(autotyper, text="START AUTOTYPER", fg="black", font = "arial 12 bold", command=atf.errCatch) 
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
stopbutt = tk.Button(autotyper, text=" STOP AUTOTYPER ", command=atf.stop, font = "arial 10").place(x=25, y=40)
tk.Label(typerinputs, text=" ", fg="white", bg="white") .grid(row=0, column=0)
#
##ELEMENTS ---------------------------------------------------------------------
acf = AutoClickerFunc()
clickthread = threading.Thread(target=acf.StartButt)
clickthread.daemon = True
#ELEMENTS AUTOCLICKER ---------------------------------------------------------
mbframe = tk.LabelFrame(autoclicker, text="Select Mouse Buttons", bg="white")
mbframe.place(x=200,y=0)
mbinps = tk.LabelFrame(autoclicker, text="Input Settings", bg="white")
mbinps.place(x=10, y=90)
mbops = tk.LabelFrame(autoclicker, text="Options", bg="white")
mbops.place(x=200, y=100)
tk.Label(autoclicker, text="V1", font="arial 15 bold", bg="white") .place(x=310, y=102)
tk.Button(autoclicker, text="ESC", font="arial 13 bold", command=acf.esc) .place(x=300, y=130)
tk.Radiobutton(mbframe, text="Left Click                    ", variable=mbvar, value=0, bg="white").grid(row=1, column=0, sticky=tk.W)
tk.Radiobutton(mbframe, text="Right Click                   ", variable=mbvar, value=1, bg="white").grid(row=2, column=0, sticky=tk.W)
tk.Label(mbinps, text="   Repetitions:  ", bg="white") .grid(row=6, column=0, sticky=tk.W)
repsm = tk.Entry(mbinps, width=11)
repsm.grid(row=7, column=0)
tk.Label(mbinps, text="", bg="white") .grid(row=8,column=0)
tk.Button(autoclicker, text="START AUTOCLICKER", command=acf.errCatch, font="arial 12 bold" ) .grid(row=0, column=0, padx=4, pady=8)
tk.Label(mbinps, text="        Intervals:        ", bg="white") .grid(row=6, column=1, sticky=tk.E)
interm = tk.Entry(mbinps, width=10)
interm.grid(row=7, column=1) 
runforms = tk.Checkbutton(mbops, text="Run For:", variable=forkey, bg="white") .grid(row=6, column=3,sticky=tk.W)
runforeverms = tk.Checkbutton(mbops, text="Run Forever", variable=foreverkey, bg="white") .grid(row=7, column=3, sticky=tk.W)
stopauto = tk.Button(autoclicker, text="STOP AUTOCLICKER", command=acf.stop, font="arial 10") .grid(row=2, column=0)
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
root.iconbitmap(r"autoboticon_EPr_icon-5.icns")
root.configure(bg="white")
root.mainloop()
