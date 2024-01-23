from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

file = open("./app_data/current_user.txt", "r")
current_user = file.read()
file.close()
file = open("./app_data/current_user.txt", "w")
file.write("")
file.close()
if current_user == "":
    exit()

# Window definition and formatting
win_mainpage = Tk()
win_mainpage.title("myFotos")
win_mainpage_height = int(win_mainpage.winfo_screenheight() - 120)
win_mainpage_width = int(win_mainpage.winfo_screenwidth() / 1.5)
icon = Image.open("./Assets/TAKOC.png")
icon = icon.resize((50, 50))
icon = ImageTk.PhotoImage(icon)
win_mainpage.iconphoto(True, icon)
win_mainpage.geometry(f"{win_mainpage_width}x{win_mainpage_height}+{int((win_mainpage.winfo_screenwidth() - win_mainpage_width) / 2)}+{int((win_mainpage.winfo_screenheight() - win_mainpage_height) / 4)}")
win_mainpage.resizable(0, 0)


class Photo:
    def __init__(self, data_string: str = "20000101|empty|0|#empty|./Assets/TAKOC.png"):
        self.data_string = data_string
        data = data_string.split("|")
        self.date = f"{data[0][6:]}/{data[0][4:6]}/{data[0][:4]}"
        self.publisher = data[1]
        self.likes = data[2]
        self.tags = data[3].split("#")
        self.file = data[4]
        self.img = None
        self.likes_img = None
        self.liked = False

    def make_fit(self):
        img = Image.open(self.file)
        if (img.width >= win_mainpage_width - 140) and (img.width / img.height >= (win_mainpage_width - 140) / 400):
            img = img.resize((win_mainpage_width - 140, int((win_mainpage_width - 140) * img.height) / img.width))
        elif img.height >= 400 and (img.width / img.height <= (win_mainpage_width - 140) / 400):
            img = img.resize((int(img.width * 400 / img.height), 400))
        self.img = ImageTk.PhotoImage(img)

        # Create a smaller image for likes label
        if self.liked:
            likes_img = Image.open("./Assets/heart.png")
            likes_img = likes_img.resize((40, 40))
            self.likes_img = ImageTk.PhotoImage(likes_img)
        else:
            likes_img = Image.open("./Assets/no heart.png")
            likes_img = likes_img.resize((40, 40))
            self.likes_img = ImageTk.PhotoImage(likes_img)
        return self.img

def like(img: Photo, likes_label: Label):
    # Update the like status and the number of likes
    if not img.liked:
        img.likes = str(int(img.likes) + 1)
        img.liked = True
    else:
        img.likes = str(int(img.likes) - 1)
        img.liked = False

    # Update the likes label text
    likes_label.config(text=img.likes)
    
    
    with open("./app_data/images_data.txt", "r") as file:
        data = file.readlines()

    # Update the likes information in the data based on the file path
    for i in range(len(data)):
        if img.file in data[i]:
            data[i] = data[i].split("|")
            data[i][2] = img.likes
            data[i] = "|".join(data[i])

    # Write the modified data back to the file
    with open("./app_data/images_data.txt", "w") as file:
        file.writelines(data)


def go_home():
    file = open("./app_data/current_user.txt", "w")
    file.write(current_user)
    file.close()
    os.startfile("main.pyw")
    win_mainpage.destroy()

def search(tags: str = "#"):
    global images, fra_image, can_scroll, v_scrollbar, fra_canvas_scroll

    go_home()
    can_scroll.destroy()
    v_scrollbar.destroy()
    fra_image.destroy()
    can_scroll = Canvas(fra_canvas_scroll)
    v_scrollbar = Scrollbar(fra_canvas_scroll, orient="vertical", command=can_scroll.yview)
    v_scrollbar.pack(side="right", fill="y")
    can_scroll.configure(yscrollcommand=v_scrollbar.set)
    can_scroll.pack(side="left", fill=BOTH, expand=True)
    fra_image = Frame(can_scroll, padx=50, bg="#aaaaaa")
    can_scroll.create_window((0, 0), window=fra_image, anchor=NW)

    win_mainpage.focus()
    file = open("./app_data/images_data.txt", "r")
    images_data = file.read().split("\n")
    file.close()

    images = []
    if tags.split("#") == [tags]:
        for image_info in images_data:
            if tags in image_info.split("|")[1]:
                images.append(Photo(image_info))
    else:
        for x in tags.split("#")[1:]:
            for image_info in images_data:
                if f"#{x}" in image_info.split("|")[3]:
                    images.append(Photo(image_info))

    display_images_in_grid()

fra_canvas_scroll = Frame(win_mainpage, relief=RIDGE, borderwidth=2, 
                          width=win_mainpage_width, height=win_mainpage_height - 70)
fra_canvas_scroll.place(x=0, y=70)
fra_canvas_scroll.pack_propagate(False)
can_scroll = Canvas(fra_canvas_scroll)
v_scrollbar = Scrollbar(fra_canvas_scroll, orient="vertical", command=can_scroll.yview)
v_scrollbar.pack(side="right", fill="y")
can_scroll.configure(yscrollcommand=v_scrollbar.set)
can_scroll.pack(side="left", fill=BOTH, expand=True)
fra_image = Frame(can_scroll, padx=50, bg="#aaaaaa")
can_scroll.create_window((0, 0), window=fra_image, anchor=NW)

file = open("./app_data/images_data.txt", "r")
images_data = file.read().split("\n")
file.close()

dict_likes = {}
profile_pic = 0


def find_profile_pic(user, scale: tuple = (40, 40)):
    global profile_pic
    file = open("./app_data/users_interactions.txt", "r")
    data = file.read().split("\n")
    file.close()
    if user == current_user:
        for x in range(len(data)):
            if current_user in data[x]:
                profile_pic = Image.open(data[x].split("|")[1])
                profile_pic = profile_pic.resize(scale)
                profile_pic = ImageTk.PhotoImage(profile_pic)
    else:
        for x in range(len(data)):
            if user.publisher in data[x]:
                profile_pic = Image.open(data[x].split("|")[1])
                profile_pic = profile_pic.resize((40, 40))
                profile_pic = ImageTk.PhotoImage(profile_pic)
    return profile_pic


def upload():
    # Open a file dialog to choose an image file
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])


def display_images_in_grid():
    global dict_likes

    lab_profile_pic = Label(fra_image, image=find_profile_pic(current_user, (200, 200)))
    lab_profile_pic.grid(row=0, column=1, columnspan=2, pady=40, sticky=W)

    but_upload = Button(fra_image, text="Fazer upload", command=lambda: upload())
    but_upload.grid(row=0, column=10, columnspan=3, sticky=W)

    if len(images) == 0:
        label = Label(fra_image, text="Ainda não fez upload de nenhuma imagem", width=110, height=18, relief=RIDGE, justify="center")
        label.pack_propagate(False)
        label.grid(row=2, column=1, padx=5, pady=5, columnspan=20)

    # Display images in a grid inside the image frame
    for i in range(len(images)):
        label = Label(fra_image, image=images[i].make_fit(), width=win_mainpage_width - 140, height=400, relief=RIDGE)
        label.pack_propagate(False)
        label.grid(row=i * 5 + 2, column=1, padx=5, pady=5, columnspan=20)
        lab_date = Label(fra_image, text=images[i].date, font=("Arial", 20))
        lab_date.grid(row=i * 5 + 1, column=20, pady=5, sticky=W)

        # Create a button for likes and a label for the number of likes
        dict_likes[f"lab_likes{i}"] = Label(fra_image, text=images[i].likes, font=("Arial", 20))
        dict_likes[f"lab_likes{i}"].grid(row=i * 5 + 3, column=2, pady=5, sticky=W)

        dict_likes[f"but_likes{i}"] = Button(fra_image, image=images[i].likes_img)
        dict_likes[f"but_likes{i}"].grid(row=i * 5 + 3, column=1, pady=5)

        space = Label(fra_image, text = " ", bg="#aaaaaa")
        space.grid(row=i * 5 + 4, column=1)

    # Update the canvas scroll region
    fra_image.update_idletasks()
    can_scroll.configure(scrollregion=can_scroll.bbox("all"))

def on_canvas_configure():
    # Update the canvas scroll region when the size changes
    can_scroll.configure(scrollregion=can_scroll.bbox("all"))

def on_mouse_wheel(event):
    # Handle mouse wheel scrolling
    if event.delta:
        can_scroll.yview_scroll(-1 * (event.delta // 120), "units")

can_scroll.destroy()
v_scrollbar.destroy()
fra_image.destroy()
can_scroll = Canvas(fra_canvas_scroll)
v_scrollbar = Scrollbar(fra_canvas_scroll, orient="vertical", command=can_scroll.yview)
v_scrollbar.pack(side="right", fill="y")
can_scroll.configure(yscrollcommand=v_scrollbar.set)
can_scroll.pack(side="left", fill=BOTH, expand=True)
fra_image = Frame(can_scroll, padx=50, bg="#aaaaaa")
can_scroll.create_window((0, 0), window=fra_image, anchor=NW)
win_mainpage.focus()
file = open("./app_data/images_data.txt", "r")
images_data = file.read().split("\n")
file.close()
images = []
for image_info in images_data:
    if current_user == image_info.split("|")[1]:
        images.append(Photo(image_info))
display_images_in_grid()

# Bind the canvas to the mouse wheel for scrolling
can_scroll.bind("<Configure>", lambda e: on_canvas_configure())
can_scroll.bind_all("<MouseWheel>", on_mouse_wheel)

# Navbar definition and formatting
fra_navbar = Frame(win_mainpage, width=win_mainpage_width, height=70, borderwidth=0, bg="#656565")
fra_navbar.place(x=0, y=0)

# Logo definition and formatting
but_logo = Button(fra_navbar, image=icon, border=0, width=50, height=50, command=go_home)
but_logo.place(x=5, y=9)

# Profile definition and formatting
but_profile = Button(fra_navbar, image=find_profile_pic(current_user), border=0, width=40, height=40)
but_profile.place(x=win_mainpage_width - 50, y=14)

win_mainpage.mainloop()
