from tkinter import *

'''def toggle():
    if label.winfo_ismapped():
        button['text']='unmap'
        label.pack_forget()
    else:
        button['text']='map'
        label.pack()

root = Tk()
button = Button(text="Push me", command=toggle)
button.pack()
labelFrame = Frame()
labelFrame.pack()
label = Label(labelFrame, text="Hello Big Big World")
label.pack()
root.wait_window()'''

def toggle():
    if label.winfo_ismapped():
        button['text']='unmap'
        label.pack_forget()
    else:
        button['text']='map'
        label.pack()
root = Tk()
button = Button(text="Push me", command=toggle)
button.pack()
label = Label(text="Hello")
label.pack()
root.wait_window()
 