from tkinter import *
from tkinter import messagebox
import tkinter
import string
import tkinter as tk
from tkinter import ttk

#global m_total
m_total=0

def button_CE_Clicked():
    equation.set("")

def button_1_clicked():
    #equation.set(equation.get()+"1")

    # Above and Below lines will show same result
    previous_value = equation.get()
    new_value = previous_value + "1"
    equation.set(new_value)
def button_MPLUS_Clicked():
    global m_total
    # equation.set(equation.get() + "2")
    eq_val = equation.get()
    if eq_val == "" :
        eq_val = "0"
    m_total=m_total+ int(eq_val)

    button_MC.config(state="normal")
    button_MR.config(state="normal")
def button_Minus_Clicked():
    global m_total
    eq_val = equation.get()
    if eq_val == "":
        eq_val = "0"
    m_total = m_total - int(eq_val)
    button_MC.config(state="normal")
    button_MR.config(state="normal")

def button_MR_clicked():
    global m_total
    # equation.set(equation.get() + "2")
    equation.set(m_total)
def button_Ms_Clicked():
    global m_total
    #m_total=eval(equation.get())
    eq_val = equation.get()
    if eq_val == "":
        eq_val = "0"
    m_total = eval(eq_val)

    button_MC.config(state="normal")
    button_MR.config(state="normal")




def button_2_Clicked():
    global m_total
    #equation.set(equation.get() + "2")

    previous_value = equation.get()
    new_value = previous_value + "2"
    equation.set(new_value)

def button_3_Clicked():
    equation.set(equation.get() + "3")
def button_4_Clicked():
    equation.set(equation.get() + "4")
def button_5_Clicked():
    equation.set(equation.get() + "5")
def button_6_Clicked():
    equation.set(equation.get() + "6")
def button_7_Clicked():
    equation.set(equation.get() + "7")
def button_8_Clicked():
    equation.set(equation.get() + "8")
def button_9_Clicked():
    equation.set(equation.get() + "9")
def button_0_Clicked():
    equation.set(equation.get() + "0")
def button_dot_Clicked():
    equation.set(equation.get() + ".")
def button_plus_Clicked():
    equation.set(equation.get() + "+")
def button_minus_Clicked():
    equation.set(equation.get() + "-")

def button_percent_clicked():
    equation.set(equation.get() + "%")
def button_divide_Clicked():
    equation.set(equation.get() + "/")
def button_multiply_Clicked():

    #equation.set(equation.get() + "*")

    # Above and Below lines will show same result
    previous_value = equation.get()
    new_value = previous_value + "*"
    equation.set(new_value)

def button_cancel_Clicked():
    #equation.set(equation.get() + "x")
    previous_value = equation.get()
    new_value = previous_value[0:previous_value.__len__()-1]
    #new_value =  LEFT(previous_value,(previous_value)-1)
    equation.set(new_value)
def button_ezequalto_Clicked():
    previous_value = equation.get()
    new_value = eval(previous_value)
    equation.set(new_value)
def button_C_Clicked():
    equation.set("")

def button_mc_clicked():
    #tkinter.messagebox.showinfo("Info","You clicked MC Button. Total="+ str(m_total))
    global m_total
    m_total=0
    button_MC.config(state="disabled")
    button_MR.config(state="disabled")


def button_minus1_Clicked():
    #equation.set(equation.get()+"1")

    # Above and Below lines will show same result
    previous_value = equation.get()
    new_value = previous_value + "-1"
    equation.set(new_value)
def button_minus2_Clicked():
    #equation.set(equation.get()+"1")

    # Above and Below lines will show same result
    previous_value = equation.get()
    new_value = previous_value + "-2"
    equation.set(new_value)


window = tkinter.Tk()
window.geometry("300x350")
window.title("Omer/Fakhar's Calculator")
window.background="yellow"
window.bg_pc=("pink")

equation = StringVar()
# input field for the expression
input_field = tkinter.Entry(window, textvariable=equation)
input_field.grid(columnspan=10, ipadx=60, ipady=2)
equation.set("")

button_MC =  tkinter.Button (window,text="MC",state="disabled",width=5,height=2,command=button_mc_clicked)
button_MC.grid(row=1,column=0)

button_MR =  tkinter.Button (window,text="  MR",state="disabled",width=5,height=2,command=button_MR_clicked)
button_MR.grid(row=1,column=1)

button_MP=  tkinter.Button (window,text="  M +  ",width=5,height=2,command=button_MPLUS_Clicked).grid(row=1,column=2)

button_MM=  tkinter.Button (window,text="  M -  ",width=5,height=2,command=button_Minus_Clicked).grid(row=1,column=3)
button_Ms=  tkinter.Button (window,text="  MS   ",width=5,height=2,command=button_Ms_Clicked).grid(row=1,column=4)
button_Mh=  tkinter.Button (window,text="  M^   ",width=5,height=2).grid(row=1,column=5)
button_percent =  tkinter.Button (window,text="   %   ",width=5,height=2,command=button_percent_clicked).grid(row=2,column=0)
button_CE =  tkinter.Button (window,text="  CE  ",width=5,height=2,command=button_CE_Clicked).grid(row=3,column=0)
button_7 =  tkinter.Button (window,text="   7   ",width=5,height=2,command=button_7_Clicked).grid(row=4,column=0)
button_4 =  tkinter.Button (window,text="   4   ",width=5,height=2,command=button_4_Clicked).grid(row=5,column=0)
button_1 =  tkinter.Button (window,text="   1   ",width=5,height=2,command=button_1_clicked).grid(row=6,column=0)
button_DIVIDE =  tkinter.Button (window,text="   /   ",width=5,height=2).grid(row=2,column=1)
button_X2 =  tkinter.Button (window,text="  x2  ",width=5,height=2).grid(row=2,column=2)
button_1DIVIDEDX =  tkinter.Button (window,text="  1/x ",width=5,height=2).grid(row=2,column=3)
button_C =  tkinter.Button (window,text="   C   ",width=5,height=2,command=button_C_Clicked).grid(row=3,column=1)
button_CANCEL =  tkinter.Button (window,text="   x   ",width=5,height=2,command=button_cancel_Clicked).grid(row=3,column=2)
button_DIVIDE =  tkinter.Button (window,text="   /   ",width=5,height=2 ,command=button_divide_Clicked).grid(row=3,column=3)
button_8 =  tkinter.Button (window,text="   8   ",width=5,height=2  ,command=button_8_Clicked).grid(row=4,column=1)
button_9 =  tkinter.Button (window,text="   9   ",width=5,height=2 ,command=button_9_Clicked) .grid(row=4,column=2)
button_MULTIPLY =  tkinter.Button (window,text="   *   ",width=5,height=2  ,command=button_multiply_Clicked) .grid(row=4,column=3)

button_5 =  tkinter.Button (window,text="   5   ",width=5,height=2,command=button_5_Clicked).grid(row=5,column=1)
button_6 =  tkinter.Button (window,text="   6   ",width=5,height=2,command=button_6_Clicked).grid(row=5,column=2)
button_minus =  tkinter.Button (window,text="   -   ",width=5,height=2,command=button_minus_Clicked).grid(row=5,column=3)
button_2 =  tkinter.Button (window,text="   2   ",width=5,height=2,command=button_2_Clicked).grid(row=6,column=1)
button_3 =  tkinter.Button (window,text="   3   ",width=5,height=2,command=button_3_Clicked).grid(row=6,column=2)
button_PLUS =  tkinter.Button (window,text="   +   ",width=5,height=2,command=button_plus_Clicked).grid(row=6,column=3)


button_DECIMAL =  tkinter.Button (window,text="   .   ",width=5,height=2,command=button_dot_Clicked).grid(row=7,column=2)
button_ezequalto =  tkinter.Button (window,text="   =   ",width=5,height=2,command=button_ezequalto_Clicked).grid(row=7,column=3)
#button_ =  tkinter.Button (window,text="   =   ",width=5,height=2).grid(row=7,column=3)
button_0 =  tkinter.Button (window,text="   0   ",width=5,height=2,command=button_0_Clicked).grid(row=7,column=1)

window.mainloop()
