""" Password Manager GUI"""
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.config(padx=100, pady=50)

pwd_canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file=r"C:\Users\Olalekan\Desktop\Python\Angela_Yu\day29_gui_passwd_manager\logo.png")
pwd_canvas.create_image(100, 100, image=password_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
pwd_canvas.pack()


window.mainloop()
