from tkinter import *

# Window definition and formatting
win_login = Tk()
win_login.title("myFotos")
win_login_height = int(win_login.winfo_screenheight() - 120)
win_login_width = int(win_login.winfo_screenwidth() / 2.5)
win_login.geometry(f"{win_login_width}x{win_login_height}+{int((win_login.winfo_screenwidth() - win_login_width) / 2)}+{int((win_login.winfo_screenheight() - win_login_height) / 4)}")
win_login.resizable(0, 0)

# Frame definition and formatting for login widgets
fra_login_width = int(win_login_width / 2)
fra_login_height = int(win_login_height / 2)
fra_login = Frame(win_login, borderwidth=2, relief=RIDGE, width=fra_login_width, height=fra_login_height)
fra_login.place(x=int((win_login_width - fra_login_width) / 2), y=int((win_login_height - fra_login_height) / 2))

# Login label definition and formatting
lab_login = Label(fra_login, text="Login", font=("Arial", 32))
lab_login.place(x=fra_login_width / 3.5, y=20)

# Username label definition and formatting
lab_username = Label(fra_login, text="Username")
lab_username.place(x=10, y=110)

# Username entry definition and formatting
ent_username = Entry(fra_login, width=40)
ent_username.place(x=10, y=130)

# Password label definition and formatting
lab_password = Label(fra_login, text="Password")
lab_password.place(x=10, y=160)

# Password entry definition and formatting
ent_password = Entry(fra_login, width=40)
ent_password.place(x=10, y=180)

win_login.mainloop()
