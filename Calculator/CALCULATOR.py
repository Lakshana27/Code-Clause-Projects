from tkinter import *

root = Tk()
root.title("Calculator")

# Entry field for calculations
calculate = Entry(root, width=70)
calculate.grid(row=0, column=0, columnspan=4, padx=15, pady=15)


# Function to handle number button clicks
def click(num):
    current = calculate.get()
    calculate.delete(0, END)
    calculate.insert(0, str(current) + str(num))


# Functions for arithmetic operations
def add():
    current = calculate.get()
    global math
    math = "ADD"
    global fnum
    fnum = int(current)
    calculate.delete(0, END)


def sub():
    current = calculate.get()
    global math
    math = "SUB"
    global fnum
    fnum = int(current)
    calculate.delete(0, END)


def mul():
    current = calculate.get()
    global math
    math = "MUL"
    global fnum
    fnum = int(current)
    calculate.delete(0, END)


def divi():
    current = calculate.get()
    global math
    math = "DIVI"
    global fnum
    fnum = int(current)
    calculate.delete(0, END)


# Function to clear the entry field
def clear():
    calculate.delete(0, END)


# Function to perform calculations
def equal():
    current = calculate.get()
    snum = int(current)
    calculate.delete(0, END)
    if math == "ADD":
        calculate.insert(0, str(fnum + snum))
    elif math == "SUB":
        calculate.insert(0, str(fnum - snum))
    elif math == "MUL":
        calculate.insert(0, str(fnum * snum))
    elif math == "DIVI":
        calculate.insert(0, str(fnum / snum))


# Creating buttons for numbers, arithmetic operations, clear, and equal
button_1 = Button(root, text="1", padx=50, pady=25, command=lambda: click(1))
button_2 = Button(root, text="2", padx=50, pady=25, command=lambda: click(2))
button_3 = Button(root, text="3", padx=50, pady=25, command=lambda: click(3))
button_4 = Button(root, text="4", padx=50, pady=25, command=lambda: click(4))
button_5 = Button(root, text="5", padx=50, pady=25, command=lambda: click(5))
button_6 = Button(root, text="6", padx=50, pady=25, command=lambda: click(6))
button_7 = Button(root, text="7", padx=50, pady=25, command=lambda: click(7))
button_8 = Button(root, text="8", padx=50, pady=25, command=lambda: click(8))
button_9 = Button(root, text="9", padx=50, pady=25, command=lambda: click(9))
button_0 = Button(root, text="0", padx=50, pady=25, command=lambda: click(0))
button_add = Button(root, text="+", padx=50, pady=25, command=add)
button_sub= Button(root, text="-", padx=50, pady=25, command=sub)
button_mul = Button(root, text="*", padx=50, pady=25, command=mul)
button_divi = Button(root, text="/", padx=50, pady=25, command=divi)

button_clear = Button(root, text="CLR", padx=43, pady=25,command=clear)
button_equal = Button(root, text="=", padx=50, pady=25, command=equal)

# Placing buttons on the grid
# (Rows and columns placement for each button)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divi.grid(row=1, column=3)


button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# Start the main event loop
root.mainloop()
