# This script is able to create an interactive Tkinter interface in which users can convert their videos to the desired
# codecs (VP8, VP9, h265 and AV1).

import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mg

## ============= INITIALIZE MASTER =============

# Initialize the master root as a Tkinter interface
master = tk.Tk()
master.title("Video converter")

# Set the size of the window
master.geometry("770x200")  # Minimum window size
master.resizable(False, False)

## CONFIGURE THE INTERFACE

# Background color
master.configure(bg='#2e2e2e')

# Video Converter Label
master.label = tk.Label(master, text="Video Converter", font=('Roboto', 25), fg='white', width=15, height=2)
master.label.configure(bg='#2e2e2e')
master.label.place(x=0, y=0)

# Label of the filepath for the video file
master.filelocation = tk.Entry(master, width=55, font="Arial 16")  # TEXTBOX TO PRINT PATH OF THE SOUND FILE
master.filelocation.insert(0, 'Path to the input video file')
master.filelocation.configure(state='disabled', borderwidth=0)
master.filelocation.place(x=20, y=80)

# Button to browse the input file
master.open_file = tk.Button(master, text="Import", width=3, borderwidth=0, command=lambda: browse_file(master))
master.open_file.configure(bg="#1c94cf")
master.open_file.place(x=700, y=80)


def browse_file(master):
    master.filename = fd.askopenfilename(title="Please Select a File")
    master.filelocation.configure(state='normal')
    master.filelocation.delete(0, 'end')  # Insert the file location of the audio in the label
    master.filelocation.insert(0, master.filename)
    master.filelocation.configure(state='disabled')


# Button to convert to VP8
master.open_file = tk.Button(master, text="VP8", width=5, borderwidth=0, command=lambda: convert_to_vp8(master))
master.open_file.configure(bg="#1c94cf")
master.open_file.place(x=170, y=135)

# Video Converter Label
master.label_charge = tk.Label(master, font=('Roboto', 15), fg='#2e2e2e', width=10, height=0)
master.label_charge.configure(bg='#2e2e2e')
master.label_charge.place(x=530, y=135)

def convert_to_vp8(master):
    master.label_charge.configure(text="Processing...", fg="white")
    master.update()

    if os.path.exists("output_VP8.webm"):
        os.remove("output_VP8.webm")
    try:
        command_line = 'ffmpeg -i ' + str(master.filename) + ' -c:v libvpx -b:v 1M output_VP8.webm'
        os.system(command_line)
        master.label_charge.configure(text = "Done!\u2713",fg="white")
        master.update()
    except AttributeError:
        mg.showerror('Python Error', 'Load a file please!')


# Button to convert to VP9
master.open_file = tk.Button(master, text="VP9", width=5, borderwidth=0, command=lambda: convert_to_vp9(master))
master.open_file.configure(bg="#1c94cf")
master.open_file.place(x=260, y=135)


def convert_to_vp9(master):
    master.label_charge.configure(text="Processing...", fg="white")
    master.update()

    if os.path.exists("output_VP9.webm"):
        os.remove("output_VP9.webm")
    try:
        command_line = 'ffmpeg -i ' + str(master.filename) + ' -c:v libvpx-vp9 -b:v 1M output_VP9.webm'
        os.system(command_line)
        master.label_charge.configure(text="Done!\u2713", fg="white")
        master.update()
    except AttributeError:
        mg.showerror('Python Error', 'Load a file please!')


# Button to convert to h265
master.open_file = tk.Button(master, text="h265", width=5, borderwidth=0, command=lambda: convert_to_h265(master))
master.open_file.configure(bg="#1c94cf")
master.open_file.place(x=350, y=135)


def convert_to_h265(master):
    master.label_charge.configure(text="Processing...", fg="white")
    master.update()

    if os.path.exists("output_h265.mp4"):
        os.remove("output_h265.mp4")
    try:
        command_line = 'ffmpeg -i ' + str(master.filename) + ' -c:v libx265 -b:v 1M output_h265.mp4'
        os.system(command_line)
        master.label_charge.configure(text="Done!\u2713", fg="white")
        master.update()
    except AttributeError:
        mg.showerror('Python Error', 'Load a file please!')


# Button to convert to AV1
master.open_file = tk.Button(master, text="AV1", width=5, borderwidth=0, command=lambda: convert_to_av1(master))
master.open_file.configure(bg="#1c94cf")
master.open_file.place(x=440, y=135)


def convert_to_av1(master):
    master.label_charge.configure(text="Processing...", fg="white")
    master.update()

    if os.path.exists("output_av1.mkv"):
        os.remove("output_av1.mkv")
    try:
        command_line = 'ffmpeg -i ' + str(master.filename) + ' -c:v libaom-av1 -b:v 1M output_av1.mkv'
        os.system(command_line)
        master.label_charge.configure(text="Done!\u2713", fg="white")
        master.update()
    except AttributeError:
        mg.showerror('Python Error', 'Load a file please!')


# Main loop of the root tkinter window
master.mainloop()
