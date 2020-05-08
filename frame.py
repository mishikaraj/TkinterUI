import tkinter as tk
from tkinter.ttk import *

'''root = Tk()
label = Label(root, text="Hello World")
label1= Label(root,text="ABC")
button=Button(root,text="click")
root.title("Courier Complaint System")
label.pack()
label1.pack()
button.pack()
root.mainloop()'''

'''class MyApplication(tk.Tk):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
            
if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()'''

import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
root.minsize(200,200)
root.geometry("600x500")
root.title("Courier Complaint System")
frame.pack()


button = tk.Button(frame, text="QUIT", fg="red",command=quit)
button.pack(side=tk.RIGHT)
slogan = tk.Button(frame,text="Hello",command=write_slogan)
slogan.pack(side=tk.RIGHT)

root.mainloop()