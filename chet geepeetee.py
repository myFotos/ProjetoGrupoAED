import tkinter as tk
from tkinter import ttk

class FlickrApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flickr-like App")

        # Initialize user data (for demonstration purposes)
        self.users = ["Admin", "User1", "User2"]
        self.categories = ["Nature", "Travel", "Food"]
        self.notifications = ["Daily Content", "Favorite Content"]

        # User management section
        self.user_frame = ttk.LabelFrame(root, text="Manage Users")
        self.user_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.user_listbox = tk.Listbox(self.user_frame, selectmode=tk.SINGLE, height=5)
        for user in self.users:
            self.user_listbox.insert(tk.END, user)
        self.user_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.remove_user_button = ttk.Button(self.user_frame, text="Remove User", command=self.remove_user)
        self.remove_user_button.grid(row=0, column=1, padx=10, pady=10)

        # Category management section
        self.category_frame = ttk.LabelFrame(root, text="Manage Categories")
        self.category_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.category_listbox = tk.Listbox(self.category_frame, selectmode=tk.SINGLE, height=5)
        for category in self.categories:
            self.category_listbox.insert(tk.END, category)
        self.category_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.remove_category_button = ttk.Button(self.category_frame, text="Remove Category", command=self.remove_category)
        self.remove_category_button.grid(row=0, column=1, padx=10, pady=10)

        # Notification configuration section
        self.notification_frame = ttk.LabelFrame(root, text="Configure Notifications")
        self.notification_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.notification_listbox = tk.Listbox(self.notification_frame, selectmode=tk.MULTIPLE, height=5)
        for notification in self.notifications:
            self.notification_listbox.insert(tk.END, notification)
        self.notification_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.configure_notifications_button = ttk.Button(self.notification_frame, text="Configure Notifications", command=self.configure_notifications)
        self.configure_notifications_button.grid(row=0, column=1, padx=10, pady=10)

    def remove_user(self):
        selected_user_index = self.user_listbox.curselection()
        if selected_user_index:
            self.user_listbox.delete(selected_user_index)

    def remove_category(self):
        selected_category_index = self.category_listbox.curselection()
        if selected_category_index:
            self.category_listbox.delete(selected_category_index)

    def configure_notifications(self):
        selected_notifications = [self.notification_listbox.get(index) for index in self.notification_listbox.curselection()]
        print("Configured Notifications:", selected_notifications)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlickrApp(root)
    root.mainloop()
