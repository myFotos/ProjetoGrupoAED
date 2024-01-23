import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import datetime

class FlickrApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flickr-like App")

        # Initialize data
        self.users = ["Admin", "User1", "User2"]
        self.categories = ["Nature", "Travel", "Food"]
        self.notifications = ["Daily Content", "Favorite Content"]
        self.contents = []

        # Content management section
        self.content_frame = ttk.LabelFrame(root, text="Manage Contents")
        self.content_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.content_listbox = tk.Listbox(self.content_frame, selectmode=tk.SINGLE, height=5)
        for content in self.contents:
            self.content_listbox.insert(tk.END, content['description'][:30])  # Display first 30 characters of description
        self.content_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.add_content_button = ttk.Button(self.content_frame, text="Add Content", command=self.add_content)
        self.add_content_button.grid(row=0, column=1, padx=10, pady=10)

        self.remove_content_button = ttk.Button(self.content_frame, text="Remove Content", command=self.remove_content)
        self.remove_content_button.grid(row=0, column=2, padx=10, pady=10)

        self.modify_content_button = ttk.Button(self.content_frame, text="Modify Content", command=self.modify_content)
        self.modify_content_button.grid(row=0, column=3, padx=10, pady=10)

    def add_content(self):
        # Sample content structure: {'description': 'Sample Description', 'date': '2024-01-21', 'category': 'Nature', 'image': 'sample.jpg'}
        new_content = {
            'description': 'Sample Description',
            'date': str(datetime.date.today()),
            'category': 'Nature',
            'image': 'sample.jpg'  # Default image file
        }

        # Open a file dialog to choose an image file
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Update the 'image' field with the selected file path
            new_content['image'] = file_path

            # Append the new content to the contents list
            self.contents.append(new_content)

            # Update the content listbox
            self.content_listbox.insert(tk.END, new_content['description'][:30])  # Display first 30 characters of description

    def remove_content(self):
        selected_content_index = self.content_listbox.curselection()
        if selected_content_index:
            # Remove the selected content from the contents list
            self.contents.pop(selected_content_index[0])

            # Update the content listbox
            self.content_listbox.delete(selected_content_index)

    def modify_content(self):
        selected_content_index = self.content_listbox.curselection()
        if selected_content_index:
            # Retrieve the selected content
            selected_content = self.contents[selected_content_index[0]]

            # Open a new window for modifying content
            modify_window = tk.Toplevel(self.root)
            modify_window.title("Modify Content")

            # Create entry widgets for modification
            tk.Label(modify_window, text="Description:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
            description_entry = tk.Entry(modify_window, width=50)
            description_entry.grid(row=0, column=1, padx=10, pady=10)
            description_entry.insert(0, selected_content['description'])

            tk.Label(modify_window, text="Category:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
            category_entry = tk.Entry(modify_window, width=50)
            category_entry.grid(row=1, column=1, padx=10, pady=10)
            category_entry.insert(0, selected_content['category'])

            # Function to update the content with modified values
            def update_content():
                selected_content['description'] = description_entry.get()
                selected_content['category'] = category_entry.get()

                # Update the content listbox
                self.content_listbox.delete(selected_content_index)
                self.content_listbox.insert(tk.END, selected_content['description'][:30])

                # Close the modification window
                modify_window.destroy()

            # Button to confirm modifications
            tk.Button(modify_window, text="Update Content", command=update_content).grid(row=2, column=1, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlickrApp(root)
    root.mainloop()
