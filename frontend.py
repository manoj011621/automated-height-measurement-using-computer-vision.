""" import customtkinter as ctk
from PIL import Image
import sqlite3
import subprocess
import os
from datetime import datetime
import io


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
    folder_path = 'snapshots_videos_images'
    if os.path.exists(folder_path):
        if os.name == 'nt':
            os.startfile(folder_path)
    else:
        print("Folder does not exist")

def display_database_data(data):
    database_window = ctk.CTkToplevel(app)
    database_window.title("Database Data")
    
    scrollbar = ctk.CTkScrollbar(database_window)
    scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
    
    listbox = ctk.CTkListbox(database_window, yscrollcommand=scrollbar.set)
    listbox.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    for row in data:
        listbox.insert(ctk.END, row)
    refresh_database_display(listbox, database_window)

def refresh_database_display(listbox, window):
    conn = sqlite3.connect('vehicle_data.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vehicle_data")
        data = c.fetchall()
        if data:
            listbox.delete(0, ctk.END)
            for row in data:
                listbox.insert(ctk.END, row)
    finally:
        conn.close()
    window.after(1000, lambda: refresh_database_display(listbox, window))

def update_clock():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    clock_label.configure(text=now)
    app.after(1000, update_clock)

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
    height_label.configure(text=f"{new_height:.2f} cm",font=('Arial', 150, 'bold'))
    app.after(1000, update_vehicle_height_display)


def load_ctk_image(file_path, width=None, height=None):
    pil_image = Image.open(file_path)
    if width is not None and height is not None:
        # Resize the image only if both width and height are provided
        pil_image = pil_image.resize((width, height), Image.LANCZOS)  # Using LANCZOS for high-quality resizing
    return ctk.CTkImage(pil_image)

app = ctk.CTk()
app.geometry("1315x800")
app.title("Main Page")


try:
    bg_image = load_ctk_image('volvopic.png',1300,800)
    bg_label = ctk.CTkLabel(app, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    print("Background set successfully.")
except Exception as e:
    print(f"Error setting background: {e}")

clock_label = ctk.CTkLabel(app, font=('Arial', 30), bg_color='GREEN')
clock_label.place(relx=1, rely=0.1, anchor='e')
update_clock()


icon_width = 25
icon_height = 25
camera_iconcam = load_ctk_image("camera.png", icon_width, icon_height)
camera_iconDB = load_ctk_image("Databaseimg.png", icon_width, icon_height)
camera_iconVcam = load_ctk_image("vcam.png", icon_width, icon_height)
camera_iconfolder = load_ctk_image("folder.png", icon_width, icon_height)



height_title_label = ctk.CTkLabel(app, text="Measured Height", bg_color='lightblue')
height_title_label.place(relx=0.8, rely=0.58, anchor='center')

height_label = ctk.CTkLabel(app, text="Waiting for data...", width=400, height=200, bg_color='yellow')
height_label.place(relx=0.8, rely=0.8, anchor='center')

update_vehicle_height_display()


# Define button configuration for uniform styling without padding arguments
button_config = {
    'font': ('Arial', 40)  # Only include supported arguments
}

# Create buttons and arrange them at the bottom with improved layout
button_frame = ctk.CTkFrame(app)
button_frame.pack(side=ctk.BOTTOM, fill=ctk.X)

measurement_button = ctk.CTkButton(button_frame, text="Start Measurement", image=camera_iconcam, compound="left", command=open_measurement, **button_config)
measurement_button.pack(side=ctk.LEFT, expand=True, padx=10, pady=10)  # Apply padding here

measurement_button1 = ctk.CTkButton(button_frame, text="Run on Videos", image=camera_iconVcam, compound="left", command=open_measurement1, **button_config)
measurement_button1.pack(side=ctk.LEFT, expand=True, padx=10, pady=10)

database_button = ctk.CTkButton(button_frame, text="Database", image=camera_iconDB, compound="left", command=open_database, **button_config)
database_button.pack(side=ctk.LEFT, expand=True, padx=10, pady=10)

open_folder_button = ctk.CTkButton(button_frame, text="Saved Images", image=camera_iconfolder, compound="left", command=open_folder, **button_config)
open_folder_button.pack(side=ctk.LEFT, expand=True, padx=10, pady=10)




app.mainloop()
 """



import tkinter as tk
from tkinter import PhotoImage
import sqlite3
import subprocess
from PIL import Image, ImageTk  # Import from Pillow
import os
from datetime import datetime
from customtkinter import *


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



def open_height_display():
    height_window = tk.Toplevel(root)
    height_window.title("Height Measurement Display")
    height_window.geometry("500x500")

    current_height = fetch_latest_height()
    height_display_label = tk.Label(height_window, text=f"{current_height:.2f} cm", font=('Arial', 80, 'bold'), bg='yellow')
    height_display_label.pack(expand=True)

    def update_height_display():
        new_height = fetch_latest_height()
        height_display_label.config(text=f"{new_height:.2f} cm")
        height_window.after(1000, update_height_display)

    update_height_display()
      
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
database_button.grid(row=0, column=2, padx=20, pady=20)
measurement_button.image = camera_iconDB



open_folder_button = tk.Button(button_frame, text="SAVED IMAGES",image=camera_iconfolder, compound="left", command=open_folder, font=button_font)
open_folder_button.grid(row=0, column=3, padx=20, pady=20)
measurement_button.image = camera_iconfolder


open_height_display_button = tk.Button(root, text="Open Height Display",image=camera_iconfolder, compound="left", command=open_height_display, font=button_font)
open_height_display_button.grid(row=1, column=4, padx=20, pady=20)
root.mainloop()
