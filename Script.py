### sample Script ####
from tkinter import *
import os
import sys

# import Math
import requests
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

from functions import (
    display_logo,
    display_textbox,
    extract_images,
    display_icon,
    resize_image,
    display_images,
)

# from functions import display_logo
# from functions import display_icon
# from functions import display_textbox
# # from functions import extract_images

page_Contents = []
all_images = []
img_idx = [0]


def copy_text(content):
    root.clipboard_clear()
    root.clipboard_append(content[-1])


def save_all(images):
    counter = 1
    for i in images:
        if i.mode != "RGB":  # convert images to RGB befor saving them
            i = i.convert("RGB")
        i.save("img" + str(counter) + ".png", format="png")
        counter += 1


def save_image(i):
    if i.mode != "RGB":  # convert images to RGB befor saving them
        i = i.convert("RGB")
    i.save("img.png", format="png")


root = tk.Tk()

root.geometry("+%d+%d" % (350, 10))  # place GUI at x=350, y=10

# header area - logo & browse button
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)


# main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)


# logo
# logo = Image.open("logo.png")
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1, row=0)

#
# instructions
instructions = tk.Label(
    root,
    text="Select a PDF file",
    font="Raleway",
)
instructions.grid(columnspan=3, column=0, row=1)


#########################


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # page_content = page_content.encode('cp1252')
        page_content = page_content.replace("\u2122", "'")
        page_Contents.append(page_content)

        images = extract_images(page)

        for i in images:
            all_images.append(i)

        img = images[img_idx[-1]]

        display_images(img)

        # show text box on row 4 col 0
        display_textbox(page_content, 4, 0, root)

        # reset the button text back to Browse
        browse_text.set("Browse")

        img_menu = Frame(
            root,
            width=800,
            height=60,
        )

        img_menu.grid(columnspan=3, rowspan=1, row=2)

        what_image = Label(root, text="imaga 1 of 5", font=("shanti", 10))
        what_image.grid(row=2, column=1)

        display_icon("arrow_l.png", 2, 0, E)
        display_icon("arrow_r.png", 2, 2, W)

        save_img = Frame(root, width=800, height=60, bg="#c8c8c8")
        save_img.grid(columnspan=3, rowspan=1, row=3)

        copyText_btn = Button(
            root,
            text="copy text",
            command=lambda: copy_text(page_Contents),
            font=("shanti", 10),
            height=1,
            width=15,
        )
        saveAll_btn = Button(
            root,
            text="save all images",
            command=lambda: save_all(all_images),
            font=("shanti", 10),
            height=1,
            width=15,
        )
        save_btn = Button(
            root,
            text="save images",
            command=lambda: save_image(all_images[img_idx[-1]]),
            font=("shanti", 10),
            height=1,
            width=15,
        )

        copyText_btn.grid(row=3, column=0)
        saveAll_btn.grid(row=3, column=1)
        save_btn.grid(row=3, column=2)


########################
# def open_file():
#     browse_text.set("loading...")
#     file = askopenfile(
#         parent=root, mode="rb", title="Choose a file", filetype=[("Pdf file", "*.pdf")]
#     )
#     if file:
#         read_pdf = PyPDF2.PdfFileReader(file)
#         page = read_pdf.getPage(0)
#         page_content = page.extractText()
#         # page_content = page_content.encode('cp1252')
#         page_content = page_content.replace("\u2122", "'")

#         # show text box on row 4 col 0
#         display_textbox(page_content, 4, 0, root)

#     browse_text.set("Browse")


# # browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(
    root,
    textvariable=browse_text,
    command=lambda: open_file(),
    font="Raleway",
    bg="#20bebe",
    fg="white",
    height=2,
    width=15,
)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(
    columnspan=3,
)


####

root.mainloop()
