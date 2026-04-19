import tkinter
from tkinter import *
from tkinter import messagebox

size_window =Tk()

num=['3x3','4x4','5x5','6x6','7x7','8x8','9x9','10x10']
variable=StringVar(size_window)
drop1 =OptionMenu(size_window, variable,  *num)
drop1.pack()
size_window.geometry("330x360")
size_window.title("Game Size")

global row_max
global column_max

def swapbuttons(buttons_array,loop,row,column,equation):
    for r in range(0, loop):
        for c in range(0, loop):
            if  buttons_array[r][c]["bg"]=="Black":
                buttons_array[r][c]["bg"]= "light gray"
                buttons_array[r][c]["text"] = buttons_array[row][column]["text"]
                buttons_array[r][c].config(state="normal")

                buttons_array[row][column]["bg"]= "Black"
                buttons_array[row][column]["text"] = ""
                buttons_array[row][column].config(state="disabled")
                equation.set(int(equation.get()) + 1)


#def button_0_Clicked(buttons_array,event):
def button_0_Clicked(buttons_array,loop,row,column, row_max, column_max,equation):
    global size_window

    for r in range(0, loop):
        for c in range(0, loop):
            if r==row and c==column:
                #messagebox.showinfo("Info", buttons_array[r][c]["text"])
                if r==0 and c==0 and (buttons_array[r+1][c]["bg"] == "Black" or buttons_array[r][c+1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r==row_max and c==column_max and (buttons_array[r-1][c]["bg"] == "Black" or buttons_array[r][c-1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r==row_max and c==0 and (buttons_array[r-1][c]["bg"] == "Black" or buttons_array[r][c+1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r == 0 and c == column_max and ( buttons_array[r + 1][c]["bg"] == "Black" or buttons_array[r][c - 1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r == row_max and c != column_max and c != 0 and ( buttons_array[r - 1][c]["bg"] == "Black" or buttons_array[r][c - 1]["bg"] == "Black" or buttons_array[r][c + 1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r == 0 and c != column_max and c != 0 and ( buttons_array[r + 1][c]["bg"] == "Black" or buttons_array[r][c - 1]["bg"] == "Black" or buttons_array[r][c + 1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r!=0 and r!= row_max and c == 0 and ( buttons_array[r + 1][c]["bg"] == "Black" or buttons_array[r-1][c]["bg"] == "Black" or buttons_array[r][c + 1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif r != row_max and r!= 0 and c == column_max and ( buttons_array[r + 1][c]["bg"] == "Black" or buttons_array[r-1][c]["bg"] == "Black" or buttons_array[r][c - 1]["bg"] == "Black"):
                    swapbuttons(buttons_array, loop, row, column,equation)
                elif ( buttons_array[r + 1][c]["bg"] == "Black" or buttons_array[r-1][c]["bg"] == "Black" or buttons_array[r][c + 1]["bg"] == "Black" or buttons_array[r][c - 1]["bg"] == "Black"):
                     swapbuttons(buttons_array, loop, row, column,equation)


                #buttons_array[r][c]["bg"]="Black"

    #messagebox.showinfo("Info", event)
    #global button_0
    #for button in buttons_array:
     #   messagebox.showinfo("Info", type(button))
      #  messagebox.showinfo("Info", button["text"])
        #messagebox.showinfo("Info", button.cget("text"))


def button_1_Clicked():
    global size_window
    buttons_window = Tk()
    buttons_window.geometry("650x650")
    buttons_window.title("Slide Puzzle")

    equation = StringVar()
    # input field for the expression
    input_field = tkinter.Entry(buttons_window, textvariable=equation)
    input_field.grid(columnspan=10, ipadx=10, ipady=1)
    equation.set(0)

    loop=3
    row_max=2
    column_max=2
    if variable.get() == "3x3":
        loop=3
        row_max=2
        column_max=2
    elif variable.get() == "4x4":
        loop = 4
        row_max=3
        column_max=3
    elif variable.get() == "5x5":
        loop = 5
        row_max=4
        column_max=4
    elif variable.get() == "6x6":
        loop = 6
        row_max=5
        column_max=5
    elif variable.get() == "7x7":
        loop = 7
        row_max=6
        column_max=6
    elif variable.get() == "8x8":
        loop = 8
        row_max=7
        column_max=7
    elif variable.get() == "9x9":
        loop = 9
        row_max=8
        column_max=8
    elif variable.get() == "10x10":
        loop = 10
        row_max=9
        column_max=9


    count=0
    buttons_array = [[]]
    for r in range(0, loop):
        buttons_array.insert(r,[])
        for c in range(0, loop):
            count=count+1
            #button_0 = tkinter.Button(buttons_window, text=count, width=7, height=3, command=button_0_Clicked)
            button_0 = tkinter.Button(buttons_window, text=count, width=7, height=3, command = lambda row=r,column=c: button_0_Clicked(buttons_array,loop, row,column,row_max,column_max,equation))
            #button_0.pack()
            button_0.grid(row=r+1,column=c+1)
            #buttons_array.append(button_0)
            buttons_array[r].append(button_0)
            #messagebox.showinfo("Info",buttons_array[count-1]["text"] )
        #messagebox.showinfo("Info", buttons_array[r][c]["text"])
            #button_0.place(relx=1, x=r, y=c)
            #button_0.bind("<Button-1>",button_0_Clicked)
    print(buttons_array)
    button_0["bg"]="Black"
    button_0["text"]=""
    button_0.config(state="disabled")

    buttons_window.mainloop()
    exit(size_window)

button_1 =  tkinter.Button (size_window,text="OK",width=6,height=1, command=button_1_Clicked)
button_1.pack()
#button_1.grid(row=4,column=2)


size_window.mainloop()

