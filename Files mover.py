import tkinter as tk
import tkinter.filedialog as filedialog
import os
import shutil


def input_source():     # the input path
    input_path = tk.filedialog.askdirectory()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'


def output():   # the output path
    output_path = tk.filedialog.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, output_path)  # Insert the 'path'


def clear_placeholder(event, extensionentry):   # clear the place holder in the extension entry
    extensionentry.delete(0, tk.END)


""" Popup windows under developement 

def popupmsg():
    popup = tk.Tk()
    popup.wm_title("")
    popup.iconbitmap(r"Directory from Files Mover icon\folder_icon.ico")
    label = tk.Label(popup, text="Files successfully moved")
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(popup, text="Okay", command=popup.destroy)
    button.pack()
    popup.mainloop()


def warn_popupmsg():
    popup = tk.Tk()
    popup.wm_title("")
    popup.iconbitmap(r"Directory from Files Mover icon\folder_icon.ico")
    label = tk.Label(popup, text="Not correct extension or directory, provide the extension without a dot")
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(popup, text="Okay", command=popup.destroy)
    button.pack()
    popup.mainloop()
"""


def move():     # Move files function
    sourcepath = input_entry.get()
    outpath = output_entry.get()
    extentry = extensionentry.get()

    files = os.listdir(sourcepath)
    for file in files:  # for every file in the source directory
        file_name, extension = os.path.splitext(file)  # lets split the name of the file and its extension
        if extension == f".{extentry}":  # knowing what type of extension or type of file, lets just move
            # those files to the new directory
            shutil.move(f"{sourcepath}/{file}", outpath)
            # popupmsg()

        else:  # if there are any files with that extension, lets just pass\skip\terminate the process
            pass


master = tk.Tk()

master.iconbitmap(r'Directory from Files Mover icon\folder_icon.ico')
master.title("Move Files by its type")


top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

# input path
input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input_source)

# output path
output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)


# File extension
extension_label = tk.Label(bottom_frame, text="File type:")
extensionentry = tk.Entry(bottom_frame, text="", width=40)
extensionentry.insert(0, 'Type file extension: .')
extensionentry.bind("<Button-1>", lambda event: clear_placeholder(event, extensionentry))

# Move button
move = tk.Button(bottom_frame, text='Move!', command=move)

# frames pack
top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

# Input pack
input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

# output pack
output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

# extension pack
extension_label.pack(pady=5)
extensionentry.pack(pady=5)

# move pack
move.pack(pady=20, fill=tk.X)

# main loop
master.mainloop()
