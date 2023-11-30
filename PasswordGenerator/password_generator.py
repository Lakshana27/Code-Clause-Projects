# importing library
import random
import string

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

# Colors ---------------
co0 = "#444466"  # Black
co1 = "#20B2AA"  # Green
co2 = "#6f9fbd"  # Blue
co3 = "#FFB6C1"  # pink

back_colour = co1

root = Tk()
root.title('')
root.geometry('370x360')
root.configure(bg=back_colour)

# creating frames ----------------

frame_main = Frame(root, width=300, height=110, bg=back_colour)
frame_main.grid(row=0, column=0)

frame_box = Frame(root, width=300, height=220, bg=back_colour)
frame_box.grid(row=1, column=0)


# working on frame main ---------------

# define image
img = Image.open('logo.png')
img = img.resize((35,35))
img = ImageTk.PhotoImage(img)

app_img = Label(frame_main, height=60, image=img, compound=LEFT, padx=10, anchor="nw", font=('Ivy 16 bold'), bg=co1, fg=co3)
app_img.place(x=2, y=0)

app_name = Label(frame_main, text='PASSWORD GENERATOR' , width=20, height=1, padx=0, anchor="nw", font=('Ivy 14 bold'), bg=co1, fg=co0)
app_name.place(x=40, y=5)

app_line = Label(frame_main, width=800, height=1, padx=4, anchor="nw", font=('Arial 1'), bg=co3, fg=co1)
app_line.place(x=1, y=35)


# function to generate password
def generate_password():
	lowercase_alphabet = string.ascii_lowercase
	uppercase_letters = string.ascii_uppercase
	number  = '123456789'
	symbols = "{}[]()*;/,_-"

	global combine

	# Uppercase letters condition
	if state_1.get() == uppercase_letters:
		combine = uppercase_letters
	else:
		pass

	# Lowercase letters condition
	if state_2.get() == lowercase_alphabet:
		combine += lowercase_alphabet
	else:
		pass

	# Numbers condition
	if state_3.get() == number:
		combine += number
	else:
		pass

	# Symbols condition
	if state_4.get() == symbols:
		combine += symbols
	else:
		pass

	# password length
	length = int(spin.get())

	# password
	password = "".join(random.sample(combine, length))

	app_password['text'] = password

	# Function to copy the password
	def copy_password():
		info = password
		frame_box.clipboard_clear()
		frame_box.clipboard_append(info)
		messagebox.showinfo("Success", "The password has been copied successfully")

	b_copy = Button(frame_box, command=copy_password, text='Copy', width=7, overrelief=SOLID, bg=co1, fg=co0, font=('Ivy 10 bold'), anchor="center", relief=RAISED )
	b_copy.grid(row=1, column=2, sticky=NSEW, pady=10)


# defining variables

lowercase_alphabet = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
number  = '123456789'
symbols = "{}[]()*;/,_-"

var = IntVar()
var.set(8)
app_info = Label(frame_main, text='Total number of characters in the password', height=1, padx=0, anchor="nw", font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.place(x=15, y=60)
spin = Spinbox(frame_main, width=5, from_=0, to=20, textvariable=var)
spin.place(x=20, y=90)


# working on frame box -----------

app_password = Label(frame_box, text='- - -' , width=20, height=2, relief='solid', padx=0, anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
app_password.grid(row=0, column=0, columnspan=4, sticky=NSEW, pady=10, padx=2)


# Uppercase letters
app_info = Label(frame_box, text='ABC Uppercase letters' , height=1, padx=0, anchor="nw", justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=2, column=1, sticky=NSEW, pady=5, padx=2)

state_1 = StringVar()
state_1.set(False) # Set check state

chek_1 = Checkbutton(frame_box, width=1, var=state_1, onvalue=uppercase_letters, offvalue='off', bg=back_colour)
chek_1.grid(row=2, column=0, sticky=NSEW, pady=5, padx=2)

# Lowercase letters
app_info = Label(frame_box, text='abc lowercase letters' , height=1, padx=0, anchor="nw", justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=2, column=3, sticky=NSEW, pady=5, padx=2)

state_2 = StringVar()
state_2.set(False) # Set check state

chek_2 = Checkbutton(frame_box, width=1, var=state_2, onvalue=lowercase_alphabet, offvalue='off', bg=back_colour)
chek_2.grid(row=2, column=2, sticky=NSEW, pady=5, padx=2)

# Numbers
app_info = Label(frame_box, text='123 Numbers' , height=1, padx=0, anchor="nw", justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=3, column=1, sticky=NSEW, pady=5, padx=2)

state_3 = StringVar()
state_3.set(False) # Set check state

chek_3 = Checkbutton(frame_box, width=1, var=state_3, onvalue=number, offvalue='off', bg=back_colour)
chek_3.grid(row=3, column=0, sticky=NSEW, pady=5, padx=2)


# Symbols
app_info = Label(frame_box, text='!@# Symbols' , height=1, padx=0, anchor="nw", justify='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_info.grid(row=3, column=3, sticky=NSEW, pady=5, padx=2)

state_4 = StringVar()
state_4.set(False) # Set check state

chek_4 = Checkbutton(frame_box, width=1, var=state_4, onvalue=symbols, offvalue='off', bg=back_colour)
chek_4.grid(row=3, column=2, sticky=NSEW, pady=5, padx=2)


# Generate password button
b_generate_password = Button(frame_box, command=generate_password, text='Generate password', width=32, overrelief=SOLID, bg=co3, fg=co1, font=('Ivy 10 bold'), anchor="center", relief=FLAT )
b_generate_password.grid(row=5, column=0, sticky=NSEW, pady=20, padx=0, columnspan=5)

root.mainloop()
