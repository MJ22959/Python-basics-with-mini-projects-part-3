import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox

win = Tk()

#def calc():
 #   print("Hello")

#def tata():
 #   print("Good Bye!")   
win.geometry("500x500")

#Button
"""
b1 = Button(win, text = 'Click me 1')
b1.pack()
b2 = Button(win, text = 'Click me 2')
b2.pack()
b3 = Button(win, text = 'Click me 3')
b3.grid(row =1, column = 1)
b4 = Button(win, text = 'Click me 4')
b4.grid(row=2,column=1)
b5 = Button(win, text = 'Click me 5', command = calc, padx = 5, pady = 5, activeforeground = 'Green',activebackground = 'Black')
b5.place(x=100,y=200)
b6 = Button(win, text = 'Click me 6', command = tata, padx = 5, pady = 5, activeforeground = 'Red', activebackground = 'Black')
b6.place(x=300,y=200)
"""
#canvas
"""
c = Canvas(win, height=500, width=500, bg='Blue')
coord= 35,150,240,300
arc = c.create_arc(coord, start=0, extent=240, fill='Purple' )
oval = c.create_oval(10, 90, 210, 300, fill='grey')
oval = c.create_oval(40, 85, 250, 135, fill='Black')
c.pack()
"""

#check button
"""
c1 = IntVar()
c2 = IntVar()
cb = Checkbutton(win, text='Music', offvalue=0, onvalue=1, height=5, width=10, variable=c1)
cb.pack()
cb2 = Checkbutton(win, text='Video', offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb2.pack()
"""

# radio button
"""
var = IntVar()
r1 = Radiobutton(win, text = 'Choice 1', variable = var, value = 1)
r1.pack()
r2 = Radiobutton(win, text = 'Choice 2', variable = var, value = 2)
r2.pack()
r3 = Radiobutton(win, text = 'Choice 3', variable = var, value = 3)
r3.pack()
"""

#Content widget
"""
def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text = 'Sum is : %d' %sum)
    return

l1 = Label(win,text='First no.')
l1.grid(row=1, column=0)
l2 = Label(win,text='Second no.')
l2.grid(row=2, column=0)
label = Label(win)
label.grid(row=6, column=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win, textvariable=x1)
e1.grid(row=1, column=2)
e2 = Entry(win, textvariable=x2)
e2.grid(row=2, column=2)
sum = partial(sum, label, x1, x2)
button = Button(win, text='Calculate', command=sum)
button.grid(row=3, column=0)
"""

# Window configuration widget

#Frame
"""
frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

rb = Button(frame, text='button 1', fg='red')
rb.pack(side=LEFT)
bb = Button(frame, text='button 2', fg='blue')
bb.pack(side=LEFT)
b = Button(frame, text='button 3', fg='black')
b.pack(side=LEFT)

gb = Button(frame2, text='button 4', fg='yellow')
gb.pack(side=BOTTOM)
"""
#ListBox
"""
lb = Listbox(win)
lb.insert(1, 'Python')
lb.insert(2, 'java')
lb.insert(3, 'Git')
lb.insert(4, 'Linux')
lb.insert(5, 'Ruby')
lb.insert(6, 'HTML')

lb.pack()
"""

#Toplevel
"""
win.title('First')
top = Toplevel()
top.title('Second')
top.geometry("500x500")
"""

# Messagebox
"""
def hello():
    messagebox.showinfo('From Computer','Have a Good Day!')
b = Button(win, text='popup',command=hello) 
b.pack()
"""

# Menu and Menubutton
"""
def nothing():
    file = Toplevel(win)
    button = Button(file,text='Do Nothing')
    button.pack()

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label='New Window', command=nothing)
filemenu.add_command(label='New File', command=nothing)
filemenu.add_command(label='Open File', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Save', command=nothing)
filemenu.add_command(label='Save as', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Close', command=win.quit)
filemenu.add_separator()

menubar.add_cascade(label='File', menu = filemenu)

win.config(menu = menubar)
"""

# Paned window
"""
pw = PanedWindow()
pw.pack(fill=BOTH, expand=1)

left = Entry(pw, bd = 5)
pw.add(left)

pw2 = PanedWindow(pw, orient=VERTICAL)
pw.add(pw2)

top = Scale(pw2, orient = HORIZONTAL)
pw2.add(top)
button = Button(pw2, text = 'OK')
pw2.add(button)

mainloop()
"""
#Place method

l1 = Label(win,text='Maths')
l1.place(x=10, y=10)
e1 = Entry(win,bd=5)
e1.place(x=60, y=10)
l2 = Label(win,text='Science')
l2.place(x=10, y=60)
e2 = Entry(win,bd=5)
e2.place(x=60, y=60)

b = Button(win, text = 'Submit')
b.place(x=100, y=100)

win.mainloop()

