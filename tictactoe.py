from tkinter import *
from tkinter import messagebox
import tkinter
import string

#print("We are going to make tic tac toe")

global_color = "Green"

window = tkinter.Tk()
window.geometry("300x350")
window.title("Omer/Fakhar's TicTacToe")

def Disable_all_buttons():
    button_1.config(state="disabled")
    button_2.config(state="disabled")
    button_3.config(state="disabled")
    button_4.config(state="disabled")
    button_5.config(state="disabled")
    button_6.config(state="disabled")
    button_7.config(state="disabled")
    button_8.config(state="disabled")
    button_9.config(state="disabled")


def WhoWin():
    global Info_Green
    global Info_Red
    Info_Green = "****PLAYER GREEN WON****"
    Info_Red = "****PLAYER RED WON****"

    if button_1["bg"] == "Red" and button_2["bg"] == "Red" and button_3["bg"] == "Red":

        Disable_all_buttons()
      #  exit(window)

        messagebox.showinfo("Info",Info_Red)
    elif button_4["bg"] == "Red" and button_5["bg"] == "Red" and button_6["bg"] == "Red":
        Disable_all_buttons()
    elif button_7["bg"] == "Red" and button_8["bg"] == "Red" and button_9["bg"] == "Red":
        messagebox.showinfo("Info", Info_Red)
        Disable_all_buttons()
    elif button_1["bg"] == "Red" and button_4["bg"] == "Red" and button_7["bg"] == "Red":
        messagebox.showinfo("Info", Info_Red)
        Disable_all_buttons()
    elif button_2["bg"] == "Red" and button_5["bg"] == "Red" and button_8["bg"] == "Red":
        messagebox.showinfo("Info", Info_Red)
        Disable_all_buttons()
    elif button_3["bg"] == "Red" and button_6["bg"] == "Red" and button_9["bg"] == "Red":
        messagebox.showinfo("Info", Info_Red)
        Disable_all_buttons()
    elif button_3["bg"] == "Red" and button_5["bg"] == "Red" and button_7["bg"] == "Red":
        messagebox.showinfo("Info", Info_Red)
        Disable_all_buttons()
    elif button_1["bg"] == "Red" and button_5["bg"] == "Red" and button_9["bg"] == "Red":
        messagebox.showinfo("Info", Info_Red)
        Disable_all_buttons()

    if button_1["bg"] == "Green" and button_2["bg"] == "Green" and button_3["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()
    elif button_4["bg"] == "Green" and button_5["bg"] == "Green" and button_6["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()

    elif button_7["bg"] ==     "Green" and button_8["bg"] == "Green" and button_9["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()
    elif button_1["bg"] == "Green" and button_4["bg"] == "Green" and button_7["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()

    elif button_2["bg"] == "Green" and button_5["bg"] == "Green" and button_8["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()
    elif button_3["bg"] == "Green" and button_6["bg"] == "Green" and button_9["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()
    elif button_3["bg"] == "Green" and button_5["bg"] == "Green" and button_7["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()
    elif button_1["bg"] == "Green" and button_5["bg"] == "Green" and button_9["bg"] == "Green":
        messagebox.showinfo("Info", Info_Green)
        Disable_all_buttons()

def SwitchColor(color):
    global global_color
    if color == 'Green':
        color='Red'
    else:
        color='Green'
        #color = 'Green'

    global_color = color
    return color

def button_1_Clicked():
   #button_1.config(state="normal", bg="Green")
    button_1.config(state="disabled")
    button_1["bg"] = SwitchColor(global_color)
    #if button_1["bg"] == "Red":
    #    print("ok")


    WhoWin()

def button_2_Clicked():
    button_2.config(state="disabled")
    button_2["bg"] = SwitchColor(global_color)
    WhoWin()


def button_3_Clicked():
    button_3.config(state="disabled")
    button_3["bg"] = SwitchColor(global_color)
    WhoWin()
def button_4_Clicked():
    button_4.config(state="disabled")
    button_4["bg"] = SwitchColor(global_color)
    WhoWin()

def button_5_Clicked():
    button_5.config(state="disabled")
    button_5["bg"] = SwitchColor(global_color)
    WhoWin()
 #   messagebox.showinfo("Omer","Fakhar un nisa")
  #  messagebox.showinfo("Fakhar un nisa", 'omer')

   # Disable_all_buttons()

def button_6_Clicked():
    button_6.config(state="disabled")
    button_6["bg"] = SwitchColor(global_color)
    WhoWin()

def button_7_Clicked():
    button_7.config(state="disabled")
    button_7["bg"] = SwitchColor(global_color)
    WhoWin()
def button_8_Clicked():
    button_8.config(state="disabled")
    button_8["bg"] = SwitchColor(global_color)
    WhoWin()
def button_9_Clicked():
    button_9.config(state="disabled")
    button_9["bg"] = SwitchColor(global_color)
    WhoWin()


    #WhoWin()


button_1 =  tkinter.Button (window,text="  ",width=7,height=3, command=button_1_Clicked)
#button_1 =  tkinter.Button(window)
#button_1.config(text="  ",width=7,height=3, bg="Red",command=button_green_Clicked)
button_1.grid(row=2,column=1)
#button_1["bg"] = "Black"

button_2 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_2_Clicked)
button_2.grid(row=2,column=2)

button_3 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_3_Clicked)
button_3.grid(row=2,column=3)

button_4 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_4_Clicked)
button_4.grid(row=3,column=1)

button_5 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_5_Clicked)
button_5.grid(row=3,column=2)

button_6 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_6_Clicked)
button_6.grid(row=3,column=3)

button_7 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_7_Clicked)
button_7.grid(row=4,column=1)

button_8 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_8_Clicked)
button_8.grid(row=4,column=2)

button_9 =  tkinter.Button (window,text="  ",width=7,height=3,command=button_9_Clicked)
button_9.grid(row=4,column=3)

window.mainloop()