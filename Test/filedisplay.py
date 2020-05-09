import os

from tkinter import *
fields = "Vorname", "Nachname", "Beruf", "Wohnort"

def fetch(entries):
    with open("test.txt","w") as textfile:
        for entry in entries:
            field = entry[0]
            text  = entry[1].get()
            #textfile = open("abc.txt", "w")
            textfile.write('%s: "%s"' % (field, text))
        textfile.close() 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == "__main__":
   root = Tk()
   ents = makeform(root, fields)
   root.bind("<Return>", (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text="Drucken",
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text="Abbrechen", command=root.destroy)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()