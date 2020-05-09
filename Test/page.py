import tkinter
import time
import base64
import imaplib
import smtplib
from imaplib import *
from tkinter import *
from tkinter.ttk import *


#Function
def display_frame(frame) :
    frame.pack_forget()#method to make the widgets invisible.'''
    frame.pack()

def back():
    frame.quit


def add():
    global frame,add_frame,root
    frame.pack_forget()#method to make the widgets invisible.
    frame.pack()
    add_frame=Frame(root)
    button=['Add Complaint Details','Go to Main Menu']
    function=[add_patient,back]
    for i in range(len(button)):
        Button(add_frame,text=button[i],command=add_patient,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(add_frame)

def search():
    global frame,add_frame,root,search_frame
    frame.pack_forget()
    search_frame=Frame(root)
    button=['Search by Complaint ID','Search by Name','Go to Main Menu']
    function=[search_by_name,back]
    for i in range(len(button)):
        Button(search_frame,text=button[i],command=search_by_name,width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(search_frame)

def delete():
    global frame,add_frame,root,delete_frame
    frame.pack_forget()
    delete_frame=Frame(root)
    button=['Delete Complaint Details','Go to Main Menu']
    function=[delete_patient,back]
    for i in range(len(button)):
        Button(search_frame,text=button[i],command=function[i],width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(search_frame)

def modify():
    global frame,root,add_frame,modify_frame
    frame.pack_forget()
    modify_frame=Frame(root)
    button=['Modify Complaint Details','Go to Main Menu']
    function=[modify_patient,back]
    for i in range(len(button)):
        Button(search_frame,text=button[i],command=function[i],width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(search_frame)

#add menu
def add_patient():
    global add_frame,root,add_patient_frame
    add_frame.pack_forget()
    add_patient_frame=Frame(root)
    label1=Label(add_patient_frame,text="Enter Compalint Id")
    label1.pack()
    v1=Entry(add_patient_frame)
    v1.pack()
    
    label2=Label(add_patient_frame,text="Enter the Complainee's Name.")
    label2.pack()
    v2=Entry(add_patient_frame)
    v2.pack()

    label3=Label(add_patient_frame,text="Complaint against")
    label3.pack()
    v3=Entry(add_patient_frame)
    v3.pack()

    label4=Label(add_patient_frame,text="Complaint Date")
    label4.pack()
    v4=Entry(add_patient_frame)
    v4.pack()

    label5=Label(add_patient_frame,text="Complain System")
    label5.pack()
    v5=Entry(add_patient_frame)
    v5.pack()

    label6=Label(add_patient_frame,text="Enter complaint description")
    label6.pack()
    v6=Entry(add_patient_frame)
    v6.pack()

    label7=Label(add_patient_frame,text="Enter the Complaint Status")
    label7.pack()
    v7=Entry(add_patient_frame)
    v7.pack()

    b1=Button(add_patient_frame,text="Enter")
    b1.pack(side='LEFT')

    b2=Button(add_patient_frame)
    b2.pack(side=RIGHT)

    display_frame(add_patient_frame)
    
#search by name
def search_by_name():
	global search_frame,root,search_patient_frame
	global vk1,vk2,vk3,vk4
	global lbl
	search_frame.pack_forget()
	search_patient_frame = Frame(root)
	
	lbl = Label(search_patient_frame, text='')
	lbl.pack()	

	
	key=Label(search_patient_frame,text="Enter Complainee's Name")
	key.pack()
	vk3=Entry(search_patient_frame)
	vk3.pack()

	'''b1=Button(search_patient_frame,text="Enter",command=get2)
	b1.pack(side=LEFT)

	b2=Button(search_patient_frame,text="Back",command=back)
	b2.pack(side = RIGHT)
	display_frame(search_patient_frame)'''






    



# Main Program
root = Tk()
s = Style()
s.configure('My.TFrame', background='brown')
root.minsize(200, 200)
root.geometry("600x500")
root.title("Courier Complaint System")
frame = add_frame=search_frame=modify_frame=delete_frame=Frame(root, height="400", width="200", style='My.TFrame')
frame.pack()


button = ['Add', 'Search', 'Delete', 'Modify']
function= [add,search,delete,modify]

for i in range(len(button)):
    Button(frame, text=button[i], command=function[i],width=20).pack(
        side=TOP, expand=YES, padx=20, pady=30)

'''button2=Button(frame,text='SEARCH',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='DELETE',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='MODIFY',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
'''
display_frame(frame)
root.mainloop()


