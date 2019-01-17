from tkinter import *

window = Tk()


def kg_to_other():
    grams = float(e2_value.get()) * 1000  # gets value in grams
    t1.insert(END, grams)
    lbs = float(e2_value.get()) * 2.205  # gets value in pounds
    t2.insert(END, lbs)
    ounces = float(e2_value.get()) * 35.274  # gets value in ounces
    t3.insert(END, ounces)


e1 = Label(window, text="Kilogram")
e1.grid(row=0, column=0)

b1 = Button(window, text="Convert", command=kg_to_other)
b1.grid(row=0, column=2)

e2_value = StringVar()  # entry box
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)  # entry box position

t1 = Text(window, height=1, width=15)
t1.grid(row=1, column=0)
t1Label = Label(window, text="grams")
t1Label.grid(row=1, column=1)

t2 = Text(window, height=1, width=15)
t2.grid(row=2, column=0)
t2Label = Label(window, text="pounds")
t2Label.grid(row=2, column=1)

t3 = Text(window, height=1, width=15)
t3.grid(row=3, column=0)
t3Label = Label(window, text="ounces")
t3Label.grid(row=3, column=1)

window.mainloop()
