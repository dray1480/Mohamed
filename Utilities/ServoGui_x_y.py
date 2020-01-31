
#       Last Edit:      12:25
#            Type:      Hybrid functional + OS terminal commands.           
#        Function:      Tkinter GUI with silders for Tilt and Rotational control of two 9g servos
#    maintainance:      High (but self contained)
#
#
#
#!/usr/bin/python3
#from subprocess import call           # import os system call directive
from tkinter import *                 # imports the Tkinter lib
import time                           # import time lib

call(["gpio","-g","mode","18","pwm"])
call(["gpio","pwm-ms"])
call(["gpio","pwmc","192"])
call(["gpio","pwmr","2000"])
call(["gpio","-g","pwm","18","116"])

call(["gpio","-g","mode","13","pwm"])
call(["gpio","pwm-ms"])
call(["gpio","pwmc","192"])
call(["gpio","pwmr","2000"])
call(["gpio","-g","pwm","13","125"])


root = Tk()                  # create the root object
root.wm_title("GUI")                 # sets title of the window
root.configure(bg="#99B898")             # change the background color

root.attributes("-fullscreen", False) # set to fullscreen by default

# we can exit when we press the escape key
def end_fullscreen(event):
    root.attributes("-fullscreen", False)

def btnExit():
    root.destroy()
    call(["gpio","-g","mode","13","in"])
    call(["gpio","-g","mode","18","in"])

def update0(angle):
    call(["gpio","-g","pwm","18", str(angle)])
    print(angle)
def update1(angle):
    call(["gpio","-g","pwm","13", str(angle)])
    print(angle)

exitButton = Button(root, text="Exit", background = "#C06C84",
      command=btnExit, height=10, width=10, font = "Arial 16 bold", activebackground = "red")

ServoC0= Scale(root, from_=50, to=230,
     orient=HORIZONTAL, command=update0, background = "#C06C84",
     width =80, label = "ServoMotorAngleController",length = 150,  activebackground = "#C06C84",font = "Arial 16 bold")

ServoC1= Scale(root, from_=60, to=180,
     orient=HORIZONTAL, command=update1, background = "#C06C84",
     width =80, label = "ServoMotorAngleController1",length = 150,  activebackground = "#C06C84",font = "Arial 16 bold")

ServoC0.grid(row=0 , column = 0)
ServoC1.grid(row=1 , column = 0)
exitButton.grid(row = 2 ,column = 0)

root.bind("<Escape>", end_fullscreen)
root.mainloop()             # starts the GUI loop