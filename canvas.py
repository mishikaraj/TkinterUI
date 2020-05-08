import tkinter as tk
from tkinter.ttk import *

root=tk.Tk()

canvas1=tk.Canvas(root,width=400,height=300,relief='raised')
canvas1.pack()

label1=tk.Label(root,text='Calculate square root')
canvas1.create_window(200,25,window=label1)

label2=tk.Label(root,text='Type a number:')
canvas1.create_window(200,100,window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140,window=entry1)


def getSquareRoot ():  
    x1 = entry1.get()
    label3 = tk.Label(root, text= 'The Square Root of ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot,bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()


'''
Wrong syntax
root = tk.Tk()
c=Canvas(root, bg="red", width=400, height=400)
c.pack()
d=Label(c, text="Hello")
d.pack()
root.mainloop()'''