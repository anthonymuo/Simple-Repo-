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
    display_images,
    resize_image,
)


# #global parameters, updating dynamically
# all_content = []
# all_images = []
# img_idx = [0]
# displayed_img = []


page_Contents = []
all_images = []
img_idx = [0]
displayed_img = []

# initiallize a Tkinter root object
root = tk.Tk()

root.geometry("+%d+%d" % (350, 10))  # place GUI at x=350, y=10

# ARROW BUTTONS FUNCTIONALITY
# right arrow

################################################


# ARROW BUTTONS FUNCTIONALITY
# right arrow
def right_arrow(all_images, selected_img, what_text):
    # restrict button actions to the number of avialable images
    if img_idx[-1] < len(all_images) - 1:
        # change to the following index
        new_idx = img_idx[-1] + 1
        img_idx.pop()
        img_idx.append(new_idx)
        # remove displayed image if exists
        if displayed_img:
            displayed_img[-1].grid_forget()
            displayed_img.pop()
        # create a new image in the new index & display it
        new_img = all_images[img_idx[-1]]
        selected_img = display_images(new_img)
        displayed_img.append(selected_img)
        # update the new index on the interface
        what_text.set(
            "image " + str(img_idx[-1] + 1) + " out of " + str(len(all_images))
        )


# left arrow
def left_arrow(all_images, selected_img, what_text):
    # restrict button actions to indices greater than 1
    if img_idx[-1] >= 1:
        # change to the previous index
        new_idx = img_idx[-1] - 1
        img_idx.pop()
        img_idx.append(new_idx)
        # remove displayed image if exists
        if displayed_img:
            displayed_img[-1].grid_forget()
            displayed_img.pop()
        # create a new image in the new index & display it
        new_img = all_images[img_idx[-1]]
        selected_img = display_images(new_img)
        displayed_img.append(selected_img)
        # update the new index on the interface
        what_text.set(
            "image " + str(img_idx[-1] + 1) + " out of " + str(len(all_images))
        )


################################################################################

# #ARROW BUTTONS FUNCTIONALITY
# #right Arrow
# def right_arrow(all_images, current_img, what_text):

#     # restrict button actions to the number of avialable images
#     if img_idx[-1] >= 1:
#         new_idx = img_idx[-1] + 1
#         img_idx.pop()
#         img_idx.append(new_idx)

#         if displayed_images:
#             displayed_img[-1].grid_forget()
#             displayed_img.pop()
#             new_img = all_images[img_idx[-1]]
#             current_img = display_images(new_img)
#             displayed_img.append(current_img)
#             what_text.set(
#                 "image" + str(img_idx[-1] + 1) + " out of " + str(len(all_images))
#             )
#         elif img_idx == len(all_images) - 1:  # from here
#             print("index out of range")
#             if displayed_img:
#                 displayed_img[-1].grid_forget()
#                 displayed_img.pop()


# def left_arrow(all_images, current_img, what_text):
#     if img_idx[-1] >= 1:
#         new_idx = img_idx[-1] - 1
#         img_idx.pop()
#         img_idx.append(new_idx)
#         if display_images:
#             displayed_img[-1].grid_forget()
#             displayed_img.pop()
#             new_img = all_images[img_idx[-1]]
#             current_img = display_images(new_img)
#             displayed_img.append(current_img)
#             what_text.set(
#                 "image" + str(img_idx[-1] + 1) + " out of " + str(len(all_images))
#             )
#         elif img_idx == -1:  # from here
#             print("index out of range")
#             if displayed_img:
#                 displayed_img[-1].grid_forget()
#                 displayed_img.pop()


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

    for i in img_idx:
        img_idx.pop()
        img_idx.append(0)

    browse_text.set("loading...")
    file = askopenfile(parent=root, mode="rb", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # page_content = page_content.encode('cp1252')
        page_content = page_content.replace("\u2122", "'")
        page_Contents.append(page_content)

        if displayed_img:
            displayed_img[-1].grid_forget()
            displayed_img.pop

            for i in range(0, len(all_images)):
                all_images.pop()

        images = extract_images(page)

        for i in images:
            all_images.append(i)

        img = images[img_idx[-1]]

        current_image = display_images(img)
        displayed_img.append(current_image)

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

        what_text = StringVar()
        what_image = Label(root, textvariable=what_text, font=("shanti", 10))
        what_text.set(
            "image" + str(img_idx[-1] + 1) + " out of " + str(len(all_images))
        )
        what_image.grid(row=2, column=1)

        display_icon(
            "arrow_l.png",
            2,
            0,
            E,
            lambda: left_arrow(all_images, current_image, what_text),
        )
        display_icon(
            "arrow_r.png",
            2,
            2,
            W,
            lambda: right_arrow(all_images, current_image, what_text),
        )

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

        # reset the button text back to Browse
        browse_text.set("Browse")  ####...................................


display_logo("logo.png", 0, 0)


# browse button
browse_text = StringVar()
browse_btn = Button(
    root,
    textvariable=browse_text,
    command=lambda: open_file(),
    font=("Raleway", 12),
    bg="#20bebe",
    fg="white",
    height=1,
    width=15,
)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)


# instructions
instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)


####

root.mainloop()
