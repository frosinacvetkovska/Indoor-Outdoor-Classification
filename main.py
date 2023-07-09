import tkinter as tk
# from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import ttkbootstrap as ttk


def upload_picture():
    file_types = [('Jpg Files', '*.jpg'),
                  ('PNG Files', '*.png'),
                  ('Jpeg Files', '*.jpeg')]
    image_path = filedialog.askopenfilename(filetypes=file_types)
    if image_path:
        display_results(image_path)


def display_results(image_path):
    reset()

    image_entry.pack_forget()
    uploadButton.pack_forget()
    title_label.pack_forget()
    description_label.pack_forget()

    image = Image.open(image_path)
    image = image.resize((400, 400))
    photo = ImageTk.PhotoImage(image)

    # Create and pack the image label
    image_label = tk.Label(window, image=photo)
    image_label.image = photo
    image_label.pack()

    # creating Go Back button
    go_back_button = ttk.Button(window, text="Try again?", command=reset, bootstyle='info')
    go_back_button.pack(pady='30')


def reset():
    for widget in window.winfo_children():
        widget.pack_forget()
    title_label.pack()
    description_label.pack()
    uploadButton.pack()


# window
window = ttk.Window(themename='cyborg')

window.title('Indoor and Outdoor Classifier')
window.geometry('700x600')

# Create and pack the image entry widget
image_entry = tk.Entry(window, width=50)

# label
title_label = ttk.Label(master=window, text='Indoor and Outdoor check', font='Calibri 24 bold', padding='30')
title_label.pack()
description_label = ttk.Label(master=window,
                              text='GUI for detecting indoor and outdoor characteristics of an image.\n '
                                   'You can insert the image using the "Upload a image" button and get results '
                                   'about the picture!',
                              font='Calibri 12', justify='center', padding='0,20,0,0')
description_label.pack()


# upload button
uploadButton = ttk.Button(window, text='Upload a image', command=upload_picture, bootstyle='info')
uploadButton.pack(pady='30')

window.mainloop()
