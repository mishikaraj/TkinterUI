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
	frame.pack()

def Add():
    frame.pack_forget()#closes the current frame
    add_frame=Frame(root)
    button=['Add Complaint Details','Go to Main Menu']
    for i in range(len(button)):
        Button(add_frame,text=button[i],width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(add_frame)

def Search():
    frame.pack_forget()
    search_frame=Frame(root)
    button=['Search by Complaint ID','Search by Name','Go to Main Menu']
    for i in range(len(button)):
        Button(search_frame,text=button[i],width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(search_frame)

def Delete():
    frame.pack_forget()
    search_frame=Frame(root)
    button=['Delete Complaint Details','Go to Main Menu']
    for i in range(len(button)):
        Button(search_frame,text=button[i],width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(search_frame)

def Modify():
    frame.pack_forget()
    search_frame=Frame(root)
    button=['Modify Complaint Details','Go to Main Menu']
    for i in range(len(button)):
        Button(search_frame,text=button[i],width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
    display_frame(search_frame)


# Main Program
root = Tk()
s = Style()
s.configure('My.TFrame', background='brown')
root.minsize(200, 200)
root.geometry("600x500")
root.title("Courier Complaint System")
frame = Frame(root, height="400", width="200", style='My.TFrame')
frame.pack()


button = ['Add', 'Search', 'Delete', 'Modify']
function= [Add,Search,Delete,Modify]

for i in range(len(button)):
    Button(frame, text=button[i], command=function[i],width=20).pack(
        side=TOP, expand=YES, padx=20, pady=30)
'''button2=Button(frame,text='SEARCH',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='DELETE',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='MODIFY',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
'''
frame.pack()
root.mainloop()
