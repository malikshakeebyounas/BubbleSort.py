from tkinter import *
from tkinter import messagebox
import tkinter
import string

size_window =Tk()
def button_1_Clicked():
    str = ''
    for row in range(int(variable1.get())):
        str = ''
        for col in range(int(variable2.get())):
            str = str + ' *'
        if  row%2!=0:
           print(''+str)
        else:
            print(str)

num=['1','2','3','4','5','6','7','8','9','10']
variable1=StringVar(size_window)
drop1 =OptionMenu(size_window, variable1,  *num)
drop1.pack()
size_window.geometry("330x360")
size_window.title("Game Size")

num=['1','2','3','4','5','6','7','8','9','10']
variable2=StringVar(size_window)
drop2 =OptionMenu(size_window, variable2,  *num)
drop2.pack()
size_window.geometry("330x360")
size_window.title("Game Size")


button_1 =  tkinter.Button (size_window,text="OK",width=6,height=1, command=button_1_Clicked)
button_1.pack()
"""

str = ''
for row in range(0,4):
    for col in range(row,row+1):
        str = str + '*'
    print(str)
"""
'''
rpos=20
cpos=20
for row in range(0,4):
    #print(row)
    str = ''
    for col in range(row+1):
        str = str + '*'
    print(str.rjust(rpos))
    rpos=rpos-1


for row in reversed(range(0,4)):
  0  #print(row)
    str = ''
    rpos = rpos + 1
    for col in range(row):
        str = str + '*'
    print(str.rjust(rpos))
'''

'''for row in range(0,6):
    str = ''
    for col in range(0,4):
        str = str + ' *'
    if  row%2!=0:
        print(' '+str)
    else:
        print(str)'''

even=[0,2,4,6,8,10,12,14,16,18,20]
odd=[1,3,5,7,9,11,15,17,19]

'''for n in range(22):
    if n % 2 != 0:
        print(n)'''

str1 = ' '
for row in range(16):
    if row % 2 != 0:
        str1 = str1+' '+ str(row)
print(str1)


str1 = ' '
for row in range(5):
    if row % 2 == 0:
        str1 = str1+' '+ str(row)
print(str1)
'''
for n in range(1,6):
    print('2x'+str(n)+'='+str(n*2))

for n in range(1,6):
    print('3x'+str(n)+'='+str(n*3))

for n in range(1,6):
    print('4x'+str(n)+'='+str(n*4))
'''
for table in range(2,5):
    print('------------')
    for n in range(1,6):
        print(str(table)+'x'+str(n)+'='+str(n*table))

"""
rpos=20
rjust=20
for row in range(0,4):
    #print(row)
    str = ''
    for col in range(row+1):
        str = str + '*'
    print(str.rjust(rpos))
    rpos=rpos-1


rpos=20
rjust=20

for row in range(0,4):
    str = ''
    rjust = rjust + 1
    for col in range(row):
        str = str + '*'
    print(str.rjust(rpos))
    rjust=rjust-1

size_window.mainloop()
"""

rpos=20
rjust=20

str = ''
for row in range(0,5):
    if row % 2 != 0:
        print(row)
    rpos = rpos + 1
    for col in range(row):
        str = str + '*'
    print(str.rjust(rpos))