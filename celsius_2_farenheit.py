from tkinter import *

root = Tk()

c_entry = Entry(root, width=4)
c_entry.pack(side='left')
Cunit_label = Label(root, text='Celsius')
Cunit_label.pack(side='left')

def compute():
    C = float(c_entry.get())
    F = (9./5)*C + 32
    F_label.configure(text='%g' % F)

compute = Button(root, text=' is ',command=compute)
compute.pack(side='left', padx=4)

F_label = Label(root, width=4)
F_label.pack(side="left")
Funit_label = Label(root, text="Fahrenheit")
Funit_label.pack(side="left")

root.mainloop()
