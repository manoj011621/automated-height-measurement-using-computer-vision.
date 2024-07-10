""" import tkinter as tk
import subprocess
import sqlite3  # Import sqlite3 module

print(sqlite3)  # Check if sqlite3 module is imported successfully

def open_measurement():
    print("Measurement box opened")
    subprocess.Popen(["python", "height_measurement_from_seg.py"])

def open_database():
    print("Database box opened")
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM vehicle_data")
    data = c.fetchall()
    print("Database data:")
    for row in data:
        print(row)
    conn.close()

root = tk.Tk()
root.geometry("300x200")
root.title("Main Page")

measurement_button = tk.Button(root, text="Measurement", command=open_measurement)
measurement_button.pack(pady=20)

database_button = tk.Button(root, text="Database", command=open_database)
database_button.pack(pady=20)

root.mainloop()
 """

""" import tkinter as tk
import subprocess
import sqlite3

def open_measurement():
    print("Measurement box opened")
    subprocess.Popen(["python", "height_measurement_from_seg.py"])

def open_database():
    print("Database box opened")
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            print("Database data:")
            for row in data:
                print(row)
        else:
            print("Database is empty. Waiting for data...")
    except sqlite3.OperationalError:
        print("Table 'vehicle_data' does not exist yet. Waiting for data...")
    conn.close()

root = tk.Tk()
root.geometry("300x200")
root.title("Main Page")

measurement_button = tk.Button(root, text="Measurement", command=open_measurement)
measurement_button.pack(pady=20)

database_button = tk.Button(root, text="Database", command=open_database)
database_button.pack(pady=20)

root.mainloop()
 """

""" import tkinter as tk
import sqlite3

def open_measurement():
    print("Measurement box opened")
    subprocess.Popen(["python", "height_measurement_from_seg.py"])

def open_database():
    print("Database box opened")
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            display_database_data(data)
        else:
            print("Database is empty. No data to display.")
    except sqlite3.OperationalError:
        print("Table 'vehicle_data' does not exist yet. No data to display.")
    conn.close()

def display_database_data(data):
    database_window = tk.Toplevel(root)
    database_window.title("Database Data")
    
    listbox = tk.Listbox(database_window, width=50)
    listbox.pack(padx=10, pady=10)
    
    for row in data:
        listbox.insert(tk.END, row)

root = tk.Tk()
root.geometry("300x200")
root.title("Main Page")

measurement_button = tk.Button(root, text="Measurement", command=open_measurement)
measurement_button.pack(pady=20)

database_button = tk.Button(root, text="Database", command=open_database)
database_button.pack(pady=20)

root.mainloop() """

""" import tkinter as tk
import sqlite3
from tkinter import PhotoImage
import subprocess
from PIL import Image, ImageTk
def open_measurement():
    print("Measurement box opened")
    subprocess.Popen(["python", "height_measurement_from_seg.py"])

def open_database():
    print("Database box opened")
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            display_database_data(data)
        else:
            print("Database is empty. No data to display.")
    except sqlite3.OperationalError:
        print("Table 'vehicle_data' does not exist yet. No data to display.")
    conn.close()

def display_database_data(data):
    database_window = tk.Toplevel(root)
    database_window.title("Database Data")
    
    listbox = tk.Listbox(database_window, width=50)
    listbox.pack(padx=10, pady=10)
    
    for row in data:
        listbox.insert(tk.END, row)

# Create the main window
root = tk.Tk()
root.geometry("700x400")
root.title("Main Page")

# Create buttons
measurement_button = tk.Button(root, text="Measurement", command=open_measurement)
measurement_button.pack(pady=20)

# Load the background image
bg_image = PhotoImage(file='Picture1.jpg')  # Make sure to provide the correct path to your image file
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


database_button = tk.Button(root, text="Database", command=open_database)
database_button.pack(pady=20)

root.mainloop()

 """
### ok but not good####################################
""" import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import subprocess
from PIL import Image, ImageTk  # Import from Pillow

def open_measurement():
    print("Measurement box opened")
    subprocess.Popen(["python", "jik.py"])
def open_measurement1():
    print("Measurement box opened")
    subprocess.Popen(["python", "detection_on_video.py"])
def open_measurement2():
    print("Measurement box opened")
    subprocess.Popen(["python", ""])
def open_measurement3():
    print("Measurement box opened")
    subprocess.Popen(["python", ""])
def open_database():
    print("Database box opened")
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            display_database_data(data)
        else:
            print("Database is empty. No data to display.")
    except sqlite3.OperationalError:
        print("Table 'vehicle_data' does not exist yet. No data to display.")
    conn.close()

def display_database_data(data):
    database_window = tk.Toplevel(root)
    database_window.title("Database Data")
    
    listbox = tk.Listbox(database_window, width=50)
    listbox.pack(padx=10, pady=10)
    
    for row in data:
        listbox.insert(tk.END, row)

# Create the main window
root = tk.Tk()
root.geometry("1300x800")
root.title("Main Page")

# Load the background image using Pillow
image = Image.open('gui/volvopic.png')  # Make sure to provide the correct path to your image file
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Font and padding for button
button_font = ('Arial', 18) 

# Create buttons
measurement_button = tk.Button(root, text="Live Cam measurement", command=open_measurement, font=button_font, padx=20, pady=10)
measurement_button.pack(padx=20, pady=20)

measurement_button1 = tk.Button(root, text="Measurement from videos", command=open_measurement1, font=button_font, padx=40, pady=10)
measurement_button1.pack(padx=40, pady=20)

measurement_button2 = tk.Button(root, text="Capture images", command=open_measurement2, font=button_font, padx=40, pady=10)
measurement_button2.pack(padx=60, pady=20)

measurement_button3 = tk.Button(root, text="capture video", command=open_measurement3, font=button_font, padx=20, pady=10)
measurement_button3.pack(padx=200, pady=100) 

database_button = tk.Button(root, text="Database", command=open_database, font=button_font, padx=60, pady=10)
database_button.pack(pady=20)  # Adjusted for a more balanced appearance 
root.mainloop()
 """

##### looks good###########################
import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import subprocess
from PIL import Image, ImageTk  # Import from Pillow
import os


def open_measurement():
    print("Measurement box opened")
    subprocess.Popen(["python", "jik.py"])

def open_measurement1():
    print("Measurement box opened")
    subprocess.Popen(["python", "detection_on_video.py"])

def open_measurement2():
    print("Measurement box opened")
    subprocess.Popen(["python", ""])

def open_measurement3():
    print("Measurement box opened")
    subprocess.Popen(["python", ""])

def open_database():
    print("Database box opened")
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            display_database_data(data)
        else:
            print("Database is empty. No data to display.")
    except sqlite3.OperationalError:
        print("Table 'vehicle_data' does not exist yet. No data to display.")
    conn.close()

def open_folder():
    folder_path = 'snapshots_videos_images'  # Update this to your actual folder path
    if os.path.exists(folder_path):
        if os.name == 'nt':  # for Windows
            os.startfile(folder_path)
    else:
        print("Folder does not exist")

def display_database_data(data):
    database_window = tk.Toplevel(root)
    database_window.title("Database Data")
    
    # Creating a scrollbar
    scrollbar = tk.Scrollbar(database_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Creating a Listbox with the scrollbar
    listbox = tk.Listbox(database_window, width=50,height=20, yscrollcommand=scrollbar.set)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    # Inserting data into the Listbox
    for row in data:
        listbox.insert(tk.END, row)


# Create the main window
root = tk.Tk()
root.geometry("1300x800")
root.title("Main Page")

# Load the background image using Pillow
image = Image.open('OneDrive_1_5-13-2024/volvopic.png')  # Make sure to provide the correct path to your image file
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

""" ######## Font and padding for button
button_font = ('Arial', 18) 

# Create buttons and pack them at the bottom of the window
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

measurement_button = tk.Button(button_frame, text="Live Cam measurement", command=open_measurement, font=button_font, padx=20, pady=10)
measurement_button.pack(side=tk.LEFT, padx=20, pady=20)

measurement_button1 = tk.Button(button_frame, text="Measurement from videos", command=open_measurement1, font=button_font, padx=40, pady=10)
measurement_button1.pack(side=tk.LEFT, padx=20, pady=20)

measurement_button2 = tk.Button(button_frame, text="Capture images", command=open_measurement2, font=button_font, padx=40, pady=10)
measurement_button2.pack(side=tk.LEFT, padx=20, pady=20)

database_button = tk.Button(button_frame, text="Database", command=open_database, font=button_font, padx=60, pady=10)
database_button.pack(side=tk.LEFT, pady=20) 

root.mainloop() """
##########################
# Font and padding for button
button_font = ('Arial', 18) 

# Create buttons and grid them at the bottom of the window
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky='ew')
root.grid_rowconfigure(0, weight=1)  # This makes the frame stretch to fill the grid cell.
root.grid_columnconfigure(0, weight=1)

measurement_button = tk.Button(button_frame, text="Live Cam measurement", command=open_measurement, font=button_font)
measurement_button.grid(row=0, column=0, padx=20, pady=20)

measurement_button1 = tk.Button(button_frame, text="Measurement from videos", command=open_measurement1, font=button_font)
measurement_button1.grid(row=0, column=1, padx=20, pady=20)

measurement_button2 = tk.Button(button_frame, text="Capture images", command=open_measurement2, font=button_font)
measurement_button2.grid(row=0, column=2, padx=20, pady=20)

database_button = tk.Button(button_frame, text="Database", command=open_database, font=button_font)
database_button.grid(row=0, column=3, padx=20, pady=20)

open_folder_button = tk.Button(button_frame, text="Open Pictures Folder", command=open_folder, font=button_font)
open_folder_button.grid(row=0, column=4, padx=20, pady=20)

root.mainloop()


