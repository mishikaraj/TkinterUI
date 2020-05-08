import tkinter, time, base64, imaplib, smtplib
from imaplib import *
from tkinter import *
from tkinter.ttk import * 

root=Tk()
s= Style()
s.configure('My.TFrame', background='blue')
root.minsize(200,200)
root.geometry("600x500")
root.title("Courier Complaint System")
frame=Frame(root, height="400", width="200",style='My.TFrame')
frame.pack()

button1=Button(frame,text='ADD',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='SEARCH',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='DELETE',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)
button2=Button(frame,text='MODIFY',width=20).pack(side=TOP, expand=YES ,padx=20, pady=30)

root.mainloop()
