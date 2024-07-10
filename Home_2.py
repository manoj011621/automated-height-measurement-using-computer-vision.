""" import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import subprocess
from PIL import Image, ImageTk  # Import from Pillow
import os
from datetime import datetime




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
    listbox = tk.Listbox(database_window, width=50, height=20, yscrollcommand=scrollbar.set)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    # Inserting data into the Listbox
    for row in data:
        listbox.insert(tk.END, row)

def update_clock():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.geometry("1315x800")
root.title("Main Page")

# Load the background image using Pillow
image = Image.open('volvopic.png')  # Make sure to provide the correct path to your image file
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Clock display
clock_label = tk.Label(root, font=('Arial', 30), bg='GREEN')
clock_label.place(relx=1, rely=0.1, anchor='e')
update_clock()

#load button icon
original_image = Image.open("camera.png")
camera_iconcam = ImageTk.PhotoImage(original_image)

#load button icon
original_image = Image.open("Databaseimg.png")
camera_iconDB = ImageTk.PhotoImage(original_image)

#load button icon
original_image = Image.open("vcam.png")
camera_iconVcam = ImageTk.PhotoImage(original_image)

#load button icon
original_image = Image.open("folder.png")
camera_iconfolder = ImageTk.PhotoImage(original_image)


# Font and padding for button
button_font = ('Arial', 18) 

# Create buttons and grid them at the bottom of the window
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky='ew')
root.grid_rowconfigure(0, weight=1)  # This makes the frame stretch to fill the grid cell.
root.grid_columnconfigure(0, weight=1)

measurement_button = tk.Button(button_frame, text="START MEASUREMENT", image=camera_iconcam, compound="left", command=open_measurement, font=button_font)
#measurement_button = tk.Button(button_frame, text="Live Cam measurement", command=open_measurement, font=button_font)
measurement_button.grid(row=0, column=0, padx=20, pady=20)
measurement_button.image = camera_iconcam


measurement_button1 = tk.Button(button_frame, text="RUN ON VIDEOS",image=camera_iconVcam, compound="left", command=open_measurement1, font=button_font)
measurement_button1.grid(row=0, column=1, padx=20, pady=20)
measurement_button.image = camera_iconVcam


database_button = tk.Button(button_frame, text="DATABASE",image=camera_iconDB, compound="left", command=open_database, font=button_font)
database_button.grid(row=0, column=3, padx=20, pady=20)
measurement_button.image = camera_iconDB



open_folder_button = tk.Button(button_frame, text="SAVED IMAGES",image=camera_iconfolder, compound="left", command=open_folder, font=button_font)
open_folder_button.grid(row=0, column=4, padx=20, pady=20)
measurement_button.image = camera_iconfolder
root.mainloop()
  """


import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import subprocess
from PIL import Image, ImageTk  # Import from Pillow
import os
from datetime import datetime



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
    listbox = tk.Listbox(database_window, width=50, height=20, yscrollcommand=scrollbar.set)
    listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    # Inserting data into the Listbox
    for row in data:
        listbox.insert(tk.END, row)
        # Start refreshing the Listbox content periodically
    refresh_database_display(listbox, database_window)

def refresh_database_display(listbox, window):
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            listbox.delete(0, tk.END)  # Clear existing data
            for row in data:
                listbox.insert(tk.END, row)  # Insert new data
    finally:
        conn.close()
    window.after(1000, lambda: refresh_database_display(listbox, window))
    
def update_clock():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

def fetch_latest_height():
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT vehicle_height FROM vehicle_data ORDER BY time_detected DESC LIMIT 1")
        height = c.fetchone()
        return height[0] if height else "No data"
    finally:
        conn.close()

def update_vehicle_height_display():
    new_height = fetch_latest_height()
    height_label.config(text=f"{new_height:.2f} cm", font=('Arial', 50, 'bold'))
    root.after(1000, update_vehicle_height_display)  # Update every second

# Create the main window
root = tk.Tk()
root.geometry("1315x800")
root.title("Main Page")

# Load the background image using Pillow
image = Image.open('OneDrive_1_5-13-2024/volvopic.png')  # Make sure to provide the correct path to your image file
bg_image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Clock display
clock_label = tk.Label(root, font=('Arial', 30), bg='GREEN')
clock_label.place(relx=1, rely=0.1, anchor='e')
update_clock()

#load button icon
original_image = Image.open("OneDrive_1_5-13-2024/camera.png")
camera_iconcam = ImageTk.PhotoImage(original_image)

#load button icon
original_image = Image.open("OneDrive_1_5-13-2024/Databaseimg.png")
camera_iconDB = ImageTk.PhotoImage(original_image)

#load button icon
original_image = Image.open("OneDrive_1_5-13-2024/vcam.png")
camera_iconVcam = ImageTk.PhotoImage(original_image)

#load button icon
original_image = Image.open("OneDrive_1_5-13-2024/folder.png")
camera_iconfolder = ImageTk.PhotoImage(original_image)

# Height display title
height_title_label = tk.Label(root, text="Measured Height", bg='lightblue', font=('Arial', 20, 'bold'))
height_title_label.place(relx=0.8, rely=0.58, anchor='center')  # Position the title above the height display

custom_font = ("Arial", 5, "bold")
# Height display setup
height_label = tk.Label(root, text="Waiting for data...", bg='yellow', width=20, height=7,font=custom_font)
height_label.place(relx=0.8, rely=0.8, anchor='center')  # Center position

update_vehicle_height_display() 
# Font and padding for button
button_font = ('Arial', 18) 

# Create buttons and grid them at the bottom of the window
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky='ew')
root.grid_rowconfigure(0, weight=1)  # This makes the frame stretch to fill the grid cell.
root.grid_columnconfigure(0, weight=1)

measurement_button = tk.Button(button_frame, text="START MEASUREMENT", image=camera_iconcam, compound="left", command=open_measurement, font=button_font)
#measurement_button = tk.Button(button_frame, text="Live Cam measurement", command=open_measurement, font=button_font)
measurement_button.grid(row=0, column=0, padx=20, pady=20)
measurement_button.image = camera_iconcam


measurement_button1 = tk.Button(button_frame, text="RUN ON VIDEOS",image=camera_iconVcam, compound="left", command=open_measurement1, font=button_font)
measurement_button1.grid(row=0, column=1, padx=20, pady=20)
measurement_button.image = camera_iconVcam


database_button = tk.Button(button_frame, text="DATABASE",image=camera_iconDB, compound="left", command=open_database, font=button_font)
database_button.grid(row=0, column=3, padx=20, pady=20)
measurement_button.image = camera_iconDB



open_folder_button = tk.Button(button_frame, text="SAVED IMAGES",image=camera_iconfolder, compound="left", command=open_folder, font=button_font)
open_folder_button.grid(row=0, column=4, padx=20, pady=20)
measurement_button.image = camera_iconfolder
root.mainloop()



