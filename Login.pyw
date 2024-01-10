from tkinter import *
# Window definition and formatting
win_login = Tk()
win_login.title("myFotos")
win_login_height = int(win_login.winfo_screenheight() - 120)
win_login_width = int(win_login.winfo_screenwidth() / 2.5)
win_login.geometry(f"{win_login_width}x{win_login_height}+{int((win_login.winfo_screenwidth() - win_login_width) / 2)}+{int((win_login.winfo_screenheight() - win_login_height) / 4)}")
win_login.resizable(0, 0)

# Function definitions
def log_in(username: str, password: str):
    if username == "" or password == "":
        print("That username does not exist!!!")
    else:
        file = open("./app_data/users_credentials.txt", "r")
        users_credentials = file.read().split("\n")
        valid_user = False
        valid_pass = False
        for user in range(len(users_credentials)):
            users_credentials[user].split(";")
            if username in users_credentials[user]:
                valid_user = True
                if password in users_credentials[user]:
                    valid_pass = True
                    break

        if valid_user:
            if valid_pass:
                print("Fez login com sucesso")
            else:
                print("Password incorreta")
        else:
            print("Username não existe")
        file.close()


def switch_sign_log():
    global mode
    if mode == "log":
        mode = "sign"
        lab_login.config(text="Sign in")
        lab_login.place(x=65, y=20)
        but_login.config(text="Registar", command=lambda: sign_in(ent_username.get(), ent_password.get()), 
                           height=2,  width=20, bg="#ffffff")
        lab_signin.config(text="")
        but_signin.config(text="Voltar ao login")
        but_signin.place()
    else:
        mode = "log"
        lab_login.config(text="Login")
        lab_login.place(x=75, y=20)
        but_login.config(text="Login", command=lambda: log_in(ent_username.get(), ent_password.get()), 
                           height=2,  width=20, bg="#ffffff")
        lab_signin.config(text="Ainda não tem conta? Clique ")
        but_signin.config(text="aqui")
        but_signin.place(x=170, y=278)


def sign_in(username: str, password: str):
    if username == "" or password == "":
        print("Este username é não é válido")
    else:
        file = open("./app_data/users_credentials.txt", "r+")
        users_credentials = file.read().split("\n")
        valid_user = True
        valid_pass = True
        for user in range(len(users_credentials)):
            users_credentials[user].split(";")
            if username in users_credentials[user]:
                valid_user = False
                break
        if len(password) < 7:
            valid_pass = False

        if valid_user:
            if valid_pass:
                file.write(f"\n{username};{password}")
                print("Registou-se com sucesso")
            else:
                print("Password tem menos de 7 carateres")
        else:
            print("Username ocupado")
        file.close()


# Canvas definition and formatting for background image
canvas = Canvas(win_login, width=win_login_width, height=win_login_height)
background_image = PhotoImage(file="./Assets/login background.png")
canvas.place(x=-2, y=-2)
canvas.create_image(win_login_width / 2, win_login_height / 2, image=background_image)

# Frame definition and formatting for login widgets
fra_login_width = 273
fra_login_height = 324
fra_login = Frame(win_login, borderwidth=2, relief=RIDGE, width=fra_login_width, height=fra_login_height)
fra_login.place(x=int((win_login_width - fra_login_width) / 2), y=int((win_login_height - fra_login_height) / 2))

# Login label definition and formatting
lab_login = Label(fra_login, text="Login", font=("Arial", 32))
lab_login.place(x=75, y=20)

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

# Login button definition and formatting
but_login = Button(fra_login, text="Login", command=lambda: log_in(ent_username.get(), ent_password.get()), 
                   height=2,  width=20, bg="#ffffff")
but_login.place(x=55, y=220)

# Sign in label definition and formatting
lab_signin = Label(fra_login, text="Ainda não tem conta? Clique ")
lab_signin.place(x=10, y=280)

# Sign in button definition and formatting
mode = "log" # Variable to decide if you are signing or logging in
but_signin = Button(fra_login, text="aqui", command=lambda: switch_sign_log(), fg="#0000aa")
but_signin.place(x=170, y=278)

win_login.mainloop()
