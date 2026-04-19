from tkinter import *
from tkinter import messagebox
import tkinter
#import ipykernel
import string
import ipywidgets as widgets
import pyodbc
from IPython.display import display
import ipython_genutils
import tkinter as tk
from tkinter import ttk
from functools import partial

w_notebook = tk.Tk()
#w_notebook.geometry('1320x1050')
w_notebook.state('zoomed')
w_notebook.title("Login")

# Create a notebook widget
notebook = ttk.Notebook(w_notebook)

# Create two frames as pages

page_Login = ttk.Frame(notebook)
page_Search = ttk.Frame(notebook)
page_NewEdit = ttk.Frame(notebook)
page_Result = ttk.Frame(notebook)
page_Result.grid(row=0, column=0, sticky="nsew")

# Add the pages to the notebook with their titles
notebook.add(page_Login, text="Login")
notebook.add(page_Search, text="Search")
notebook.add(page_NewEdit, text="New/Edit")
notebook.add(page_Result, text="Result")

# Add widgets to the pages
label1 = ttk.Label(page_Login, text="User")
label1.grid(padx=30, pady=8)

label2 = ttk.Label(page_Login, text="Password")
label2.grid(padx=0, pady=0)

# Pack the notebook widget
notebook.pack(fill="both", expand=True)

tb_user = StringVar()
input_field = tkinter.Entry(page_Login, textvariable=tb_user)
#input_field.grid(columnspan=10, ipadx=50, ipady=2)
input_field.place(x=100, y=6)
tb_user.set("admin")

tb_pwd = StringVar()
input_field = tkinter.Entry(page_Login, textvariable=tb_pwd)
#input_field.grid(columnspan=10, ipadx=50, ipady=2)
input_field.place(x=100, y=30)
tb_pwd.set("123456")

def open_link(event, name, row_data):
    #messagebox.showinfo("Search Result", f"You searched for '{name}'")
    #print(row_data)
    for col_idx, cell_data in enumerate(row_data):
        if col_idx == 0: # id
            tb_ID.set(cell_data)
        if col_idx == 1: # name
            tb_Name.set(cell_data)
        if col_idx == 4:  # FatherName
            tb_F_Name.set(cell_data)
        if col_idx == 2: # NIC
            NE_tb_NIC.set(cell_data)
        if col_idx == 6:  # Family no
            NE_tbFamlyno.set(cell_data)
        if col_idx == 5:  # Address
            NE_tbAddr.set(cell_data)
        if col_idx == 3:  # Phone
            tb_Phone.set(cell_data)
        if col_idx == 9:  # Packet
            tb_Packet.set(cell_data)

        tb_Sponsor.set(3)
        tb_Qty.set(1)
        #tb_Aid_id.set(3)
        tb_Amount.set(5000)
        #tb_Date.set(cell_data)
        notebook.select(page_NewEdit)

def open_or_not():
    global v_login
    v_login = '0'

    if tb_user.get()== "admin" and tb_pwd.get()=='123456':
        page_Login.destroy()
        #button_Login()
        #messagebox.showinfo('User', "valid Username!!")
        v_login='1'

    else:
        v_login = '0'
        messagebox.showinfo('Login','Invalid Credentials!!')
        w_notebook.destroy()
def button_Save():
    global cnxn
    cursor = cnxn.cursor()
    sql_parameters ='@Id='+tb_ID.get()+', @Name='+tb_Name.get()+',@NIC='+NE_tb_NIC.get()+',@FamilyId='+NE_tbFamlyno.get()+',@Address='+NE_tbAddr.get()+',@Phone='+tb_Phone.get()+',@Sponsor='+tb_Sponsor.get()+', @Date='+ tb_Aid_id.get()+',@Amount='+ tb_Amount.get()+',@Packet='+ tb_Packet.get() +', @Quantity=' + tb_Qty.get() +', @FatherName='+ tb_F_Name.get()+ ', @Gender='+ variable_gender.get()+ ', @Religion='+variable_religion.get()
    print(sql_parameters)
    storedProc = "exec [dbo].[New_Edit] @Id=? ,@Name=?, @NIC=?, @FamilyId=?, @Address=?, @Phone=?, @Sponsor=?, @Date=?, @Packet=?, @Quantity=?, @Amount=?,  @FatherName=?, @Religion=?, @Gender=?, @Aid_Id=?"
    params = (tb_ID.get(),tb_Name.get(),NE_tb_NIC.get(),NE_tbFamlyno.get(),NE_tbAddr.get(),tb_Phone.get(),tb_Sponsor.get(),tb_Aid_id.get(),tb_Packet.get(),tb_Qty.get(),tb_Amount.get(),tb_F_Name.get(),variable_religion.get(),variable_gender.get(),'3' )

    # Execute Stored Procedure With Parameters
    try:
        cursor.execute(storedProc, params)
        #cursor.execute('{call [dbo].[New_Edit] (?)}', var_name)
        #cursor.execute("exec [dbo].[New_Edit] @Name='ABC', @NIC='123', @FamilyId='D', @address='Lahore Cantt', @Phone='', @Sponsor='', @Date='', @Packet='', @Quantity='', @Amount='', @FatherName='', @Religion='Islam', @Gender='M'")
        cnxn.commit()
        messagebox.showinfo('Info','Saved Successfully!!')
        #cursor1 = cnxn.cursor()
        button_Search_result()
        notebook.select(page_Result)
    except:
        cnxn.rollback()
    finally:
        cursor.close()

    #Refresh_Grid()

def button_Cancel():
    print("Cancel")


def delete_rows():
    global old_rows
    # Get the parent widget that contains the grid layout
    parent_widget = table.winfo_children()[0]

    # Get the number of rows to delete
    num_rows_to_delete = old_rows


    # Delete the specified number of rows
    for i in (num_rows_to_delete):
        # Get the last row index
        last_row_index = parent_widget.grid_size()[1] - 1

        # Remove widgets and grid configuration from the last row
        for child in parent_widget.grid_slaves(row=last_row_index):
            child.grid_forget()

        # Update the grid layout to reflect the changes
        parent_widget.grid_rowconfigure(last_row_index, weight=0)

def button_Search_result():
    global cnxn
    global old_rows

    cursor = cnxn.cursor()
    #for col in cursor:
    #    print ('id: ',col[0], ' nic' ': ',col[3],'Family id :',col[6]);

    sql_parameters ='@StartDate='+tb_SDate.get()+', @EndDate='+tb_EDate.get()+',@NIC='+Searchtb_NIC.get()+',@Familynum='+Search_tbFamlyno.get()+',@Name='+tb_Name.get()+',@Address='+Search_tbAddr.get()
    print(sql_parameters)
    storedProc = "exec [dbo].[Search] @StartDate=? ,@EndDate=?, @NIC=?, @Familynum=?, @Name=?, @Address=?"
    params = (tb_SDate.get(),tb_EDate.get(),Searchtb_NIC.get(),Search_tbFamlyno.get(),tb_Name.get(),Search_tbAddr.get())

    cursor.execute(storedProc, params)

    rows = cursor.fetchall()

    header_labels = ['ID', 'Name', 'Father Name', 'NIC', 'Phone no', 'Address', 'Family no', 'Religion', 'Gender',
                     'Sponsor']
    for col, header in enumerate(header_labels):
        tk.Label(table, text=header, width=15).grid(row=0, column=col)

    #table.deletecommand()
    #table.destroy()

    old_rows.pop()

    #delete_rows()

    for rowno, row in reversed(list(enumerate(old_rows))):
        #if row[0].val.get() == 1:
        #    for i in row:
        #        i.destroy()
        old_rows.pop(rowno)

    for row_idx, row_data in enumerate(rows, start=1):
        for col_idx, cell_data in enumerate(row_data):
            tk.Label(table, text=cell_data, width=15).grid(row=row_idx, column=col_idx)

    for row_idx, row_data in enumerate(rows, start=1):
        for col_idx, cell_data in enumerate(row_data):
            if col_idx == 0:  # Name column
                label = tk.Label(table, text=cell_data, width=10, fg="red", cursor="hand2")
                label.bind("<Button-1>", partial(open_link, name=cell_data, row_data=row_data))
                label.grid(row=row_idx, column=col_idx, padx=1, pady=1)
            else:
                tk.Label(table, text=cell_data, width=10).grid(row=row_idx, column=col_idx, padx=1, pady=1)
    old_rows = rows

    #cursor.close()

notebook.select(page_Login)

def Switch_Grid(event):
    search_table = tk.Frame(page_Result)
    search_table.grid(row=0, column=0, sticky="nsew")
    search_table.grid()

    display_width = 1500
    display_height = 500
    # Bind the function to the frame resizing event
    search_table.bind("<Configure>", Switch_Grid)

    # Add the frame to the canvas

    cursor = cnxn.cursor()
    cursor.execute("select Nom.id, Nom.name, Nom.FatherName, Nom.NIC, Nom.phone, Nom.Address, Nom.FamilyId, Nom.Religion, Nom.Gender,'self' as SponsorName from [dbo].[Search]")
    old_rows = cursor.fetchall()

    search_tablecanvas = tk.Canvas(search_table, width=display_width, height=display_height)
    search_tablecanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    search_tablecanvas.grid(row=0, column=0, sticky="nsew")

    search_table = tk.Frame(table_canvas)
    search_tablecanvas.create_window((0, 0), window=table, anchor=tk.NW)
    table.grid(row=0, column=0, sticky="nsew")

    table.grid_forget()  # Remove the existing grid
    search_table.grid(row=0, column=0)  # Display the new grid

    table.grid_forget()  # Remove the existing grid
    search_table.grid(row=0, column=0)  # Display the new grid

    button_Search_result()

def button_Login():
        open_or_not()
        global cnxn
        try:
            cnxn = pyodbc.connect(driver='{SQL Server}', host='localhost', database='Trust',
                              trusted_connection='no', user='sa', password='sa123')
            print('Connection Succeeded!!')
            #messagebox.showinfo('Login',"Connection Succeeded!!")
        except:
            print('Connection Failed')
            messagebox.showinfo("Connection Failed")
        cursor = cnxn.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        #page_Login.destroy()


button_Login = tkinter.Button(page_Login, text="Login", width=5, height=1, command=button_Login)
button_Login.place(x=120, y=74)

button_Search = tkinter.Button(page_Search, text="Search", width=5, height=1, command=button_Search_result)
button_Search.place(x=125, y=220)

button_Save = tkinter.Button(page_NewEdit, text="Save", width=7, height=1, command=button_Save)
button_Save.place(x=45, y=480)

button_Cancel = tkinter.Button(page_NewEdit, text="Cancel", width=7, height=1, command=button_Cancel)
button_Cancel.place(x=190, y=479)



labelSDate = ttk.Label(page_Search, text="Start Date : ")
labelSDate.grid(padx=30, pady=8)

tb_SDate = StringVar()
input_field = tkinter.Entry(page_Search, textvariable=tb_SDate)
input_field.place(x=100, y=6)
tb_SDate.set("")

labelEDate = ttk.Label(page_Search, text="End Date : ")
labelEDate.grid(padx=30, pady=5)

tb_EDate = StringVar()
input_field= tkinter.Entry(page_Search, textvariable=tb_EDate)
input_field.place(x=100, y=38)
tb_EDate.set("")


labelNIC = ttk.Label(page_Search, text="NIC : ")
labelNIC.grid(padx=0, pady=7)

Searchtb_NIC = StringVar()
input_field = tkinter.Entry(page_Search, textvariable=Searchtb_NIC)
input_field.place(x=100, y=70)
Searchtb_NIC.set("")


labelFamlyNo = ttk.Label(page_Search, text="Family Num : ")
labelFamlyNo.grid(padx=0, pady=7)

Search_tbFamlyno = StringVar()
input_field = tkinter.Entry(page_Search, textvariable=Search_tbFamlyno)
input_field.place(x=100, y=100)
Search_tbFamlyno.set("")


labelName = ttk.Label(page_Search, text="Name : ")
labelName.grid(padx=0, pady=7)

tb_Name = StringVar()
input_field = tkinter.Entry(page_Search, textvariable=tb_Name)
input_field.place(x=100, y=135)
tb_Name.set("")


labelAddr = ttk.Label(page_Search, text="Address : ")
labelAddr.grid(padx=0, pady=7)

Search_tbAddr = StringVar()
input_field = tkinter.Entry(page_Search, textvariable=Search_tbAddr)
input_field.place(x=100, y=170)
Search_tbAddr.set("")

labelID = ttk.Label(page_NewEdit, text="ID : ")
labelID.place(x=290,y=6)

tb_ID = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_ID,state='disabled')
input_field.place(x=315, y=6)
tb_ID.set("")

labelName1 = ttk.Label(page_NewEdit, text="Name : ")
labelName1.grid(padx=30, pady=8)

tb_Name1 = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_Name)
input_field.place(x=100, y=8)
tb_Name1.set("")

labelF_Name = ttk.Label(page_NewEdit, text="Father Name : ")
labelF_Name.grid(padx=10, pady=8)

tb_F_Name = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_F_Name)
input_field.place(x=100, y=38)
tb_F_Name.set("")

labelNIC = ttk.Label(page_NewEdit, text="NIC : ")
labelNIC.grid(padx=30, pady=4)

NE_tb_NIC = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=NE_tb_NIC)
input_field.place(x=100, y=70)
NE_tb_NIC.set("")

labelFamlyNo = ttk.Label(page_NewEdit, text="Family Num : ")
labelFamlyNo.grid(padx=0, pady=7)

NE_tbFamlyno = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=NE_tbFamlyno)
input_field.place(x=100, y=103)
NE_tbFamlyno.set("")

labelAddr = ttk.Label(page_NewEdit, text="Address : ")
labelAddr.grid(padx=0, pady=7)

NE_tbAddr = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=NE_tbAddr)
input_field.place(x=100, y=135)
NE_tbAddr.set("")

labelPhone = ttk.Label(page_NewEdit, text="Phone : ")
labelPhone.grid(padx=0, pady=7)

tb_Phone = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_Phone)
input_field.place(x=100, y=168)
tb_Phone.set("")

labelSponsor = ttk.Label(page_NewEdit, text="Sponsor : ")
labelSponsor.grid(padx=0, pady=7)

tb_Sponsor = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_Sponsor)
input_field.place(x=100, y=200)
tb_Sponsor.set("")

labelPacket = ttk.Label(page_NewEdit, text="Packet : ")
labelPacket.grid(padx=0, pady=7)

tb_Packet = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_Packet)
input_field.place(x=100, y=233)
tb_Packet.set("")

labelQty = ttk.Label(page_NewEdit, text="Quantity : ")
labelQty.grid(padx=0, pady=7)

tb_Qty = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_Qty)
input_field.place(x=100, y=267)
tb_Qty.set("")

labelAmount = ttk.Label(page_NewEdit, text="Amount : ")
labelAmount.grid(padx=0, pady=7)

tb_Amount = StringVar()
input_field = tkinter.Entry(page_NewEdit, textvariable=tb_Amount)
input_field.place(x=100, y=300)
tb_Amount.set("")

labelGender = ttk.Label(page_NewEdit, text="Gender : ")
labelGender.grid(padx=0, pady=8)

num=['F','M']
variable_gender=StringVar(page_NewEdit)
drop_gender = OptionMenu(page_NewEdit, variable_gender,  *num)
drop_gender.place(x=100,y=365)

labelGender = ttk.Label(page_NewEdit, text="Religion : ")
labelGender.grid(padx=0, pady=8)

num=['Islam','Christianity']
variable_religion=StringVar(page_NewEdit)
drop_religion = OptionMenu(page_NewEdit, variable_religion,  *num)
drop_religion.place(x=100,y=400)

# Create widgets for the grid cells
widget1 = widgets.Button(description='Cell 1')
widget2 = widgets.Button(description='Cell 2')
widget3 = widgets.Button(description='Cell 3')
widget4 = widgets.Button(description='Cell 4')
widget5 = widgets.Button(description='Cell 5')
widget6 = widgets.Button(description='Cell 6')
widget7 = widgets.Button(description='Cell 7')

# Create a grid layout using the GridBox widget
grid = widgets.GridBox([widget1, widget2, widget3, widget4,widget5,widget6,widget7 ], layout=widgets.Layout(grid_template_columns='repeat(1, 300px)'))
display(grid)
# Display the grid

cnxn = pyodbc.connect(driver='{SQL Server}', host='localhost', database='Trust',
                             trusted_connection='no', user='sa', password='sa123')

table = tk.Frame(page_Result)
table.grid(row=0, column=0, sticky="nsew")
table.pack()

display_width = 1500
display_height = 500
def Table_Grid(event):
    table_canvas.configure(scrollregion=table_canvas.bbox("all"))

# Bind the function to the frame resizing event
table.bind("<Configure>", Table_Grid)

# Add the frame to the canvas

table_canvas = tk.Canvas(table, width=display_width, height=display_height)
table_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
table_canvas.grid(row=0, column=0, sticky="nsew")

table = tk.Frame(table_canvas)
table_canvas.create_window((0, 0), window=table, anchor=tk.NW)
table.grid(row=0, column=0, sticky="nsew")
cursor = cnxn.cursor()
cursor.execute("select Nom.id, Nom.name, Nom.FatherName, Nom.NIC, Nom.phone, Nom.Address, Nom.FamilyId, Nom.Religion, Nom.Gender,'self' as SponsorName from [dbo].[Nominee] Nom")
old_rows = cursor.fetchall()
button_Search_result()

'''
scrollbar_y = ttk.Scrollbar(table, orient=tk.VERTICAL, command=table_canvas.yview)
scrollbar_y.grid(row=0, column=1, sticky="ns",padx=1,pady=1)
table_canvas.configure(yscrollcommand=scrollbar_y.set)
'''

# Configure the canvas to scroll with the scrollbar
table_canvas.configure(scrollregion=table_canvas.bbox("all"))
table_canvas.create_window((0, 0), window=table, anchor="nw")

w_notebook.mainloop()
#w_login.mainloop()
