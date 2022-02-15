from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox
db=Database("employee.db")
window=Tk()
window.title("Employee Management System")
window.geometry("500x500")
window.resizable(False,False)
window.config(bg="#2c3e58")
window.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

#entries frame
entries_frame=Frame(window,bg='#535c68')
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="EMPLOYEE MANAGEMENT SYSTEM",font=("Arial",16,'bold'),bg='#535c68',fg='white')
title.grid(row=0,columnspan=2,padx=10,pady=10,sticky='w')
#label for name
lblName=Label(entries_frame,text='Name',font=('arial',16),bg='#535c68',fg='white')
lblName.grid(row=1,column=0,padx=10,pady=10,sticky='w')
txtName=Entry(entries_frame,textvariable=name,font=('Arial',16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky='w')
#label for Age
lblAge=Label(entries_frame,text='Age',font=('arial',16),bg='#535c68',fg='white')
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky='w')
txtAge=Entry(entries_frame,textvariable=age,font=('Arial',16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky='w')
#label for Doj
lblDoj=Label(entries_frame,text='D.O.J',font=('arial',16),bg='#535c68',fg='white')
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky='w')
txtDoj=Entry(entries_frame,textvariable=doj,font=('Arial',16),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky='w')
#label for email
lblEmail=Label(entries_frame,text='Email',font=('arial',16),bg='#535c68',fg='white')
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky='w')
txtEmail=Entry(entries_frame,textvariable=email,font=('Arial',16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky='w')
#label for gender
lblGender=Label(entries_frame,text='Gender',font=('arial',16),bg='#535c68',fg='white')
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky='w')
comboGender=ttk.Combobox(entries_frame,font=('Arial',16),width=28,textvariable=gender,state='readonly')
comboGender['values']=['Male','Female']
comboGender.grid(row=3,column=1,padx=10,sticky='w')
#label for contact
lblContact=Label(entries_frame,text='Contact No',font=('arial',16),bg='#535c68',fg='white')
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky='w')
txtContact=Entry(entries_frame,textvariable=contact,font=('Arial',16),width=30)
txtContact.grid(row=3,column=3,padx=10,sticky='w')
#label for address
lblAddress=Label(entries_frame,text='Address',font=('arial',16),bg='#535c68',fg='white')
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky='w')
txtAddress=Text(entries_frame,font=('Arial',16),width=85,height=5)
txtAddress.grid(row=5,column=0,padx=10,columnspan=4,sticky='w')

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[4])
    contact.set(row[6])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END,row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error in Input","Please fill All details correctly")
        return
    db.insert(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()

def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error in Input","Please fill All details correctly")
        return
    db.insert(row[0],txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    messagebox.showinfo("Success","Record update")
    clearAll()
    displayAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg='#535c68')
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')
btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=('Arial',16,'bold'),fg='white',bg="blue",bd=0).grid(row=0,column=0)

btnEdit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=('Arial',16,'bold'),fg='white',bg="green",bd=0).grid(row=0,column=1,padx=10)

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=('Arial',16,'bold'),fg='white',bg="yellow",bd=0).grid(row=0,column=2,padx=10)

btnClear=Button(btn_frame,command=clearAll,text="clear Details",width=15,font=('Arial',16,'bold'),fg='white',bg="skyblue",bd=0).grid(row=0,column=3,padx=10)


#table frame
tree_frame=Frame(window,bg="red")
tree_frame.place(x=0,y=430,width=1500,height=400)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Arial',18),rowheight=50)#modify the font of the body
style.configure("mystyle.Treeview.Heading",font=('Arial',18))#modify the font of the headings

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading('1',text='ID')
tv.column('1',width=5)
tv.heading('2',text='Name')
#tv.column('2',width=5)
tv.heading('3',text='Age')
tv.column('3',width=5)
tv.heading('4',text='D.O.J')
tv.column('4',width=10)
tv.heading('5',text='Email')
#tv.column('5',width=5)
tv.heading('6',text='Gender')
tv.column('6',width=10)
tv.heading('7',text='contact')
#tv.column('7',width=5)
tv.heading('8',text='Address')
#tv.column('8',width=5)
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

displayAll()
displayAll()



window.mainloop()
