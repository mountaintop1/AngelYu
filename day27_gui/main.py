"""Create a GUI with tkinter module """
from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=700)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked, font=("Arial", 24, "bold"))
button.grid(column=1, row=1)


button1 = Button(text="New text", command=button_clicked, font=("Arial", 24, "bold"))
button1.grid(column=7, row=3)
# Entry
input = Entry(width=20)
input.grid(column=3, row=2)


window.mainloop()

# def add(*args):
#     """Add all the numbers in the list"""
#     total = 0
#     for n in args:
#         total += n
#     return total
# addition = add(3, 5, 6, 7, 9, 45, 28, 18)
# print(addition)
