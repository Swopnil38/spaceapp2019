from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to fire alert")
window.geometry('400x400')

z= Label(window ,text = "Fire Alert").grid(row = 0,column = 0)
a = Label(window ,text = "First Name").grid(row = 2,column = 0)
b = Label(window ,text = "Last Name").grid(row = 3,column = 0)
c= Label(window ,text = "Country:").grid(row = 7,column = 0)
e= Label(window ,text = "City:").grid(row = 8,column = 0)
f= Label(window ,text = "Street:").grid(row = 9,column = 0)

d = Label(window ,text = "Contact Number").grid(row =11,column = 0)
a1 = Entry(window).grid(row = 2,column = 1)
b1 = Entry(window).grid(row = 3,column = 1)
c1 = Entry(window).grid(row = 7,column = 1)
d1 = Entry(window).grid(row = 11,column = 1)
e1 = Entry(window).grid(row = 8,column = 1)
f1 = Entry(window).grid(row = 9,column = 1)


def clicked():
   res = "Welcome to " + txt.get()
   lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=13,column=0)
window.mainloop()

