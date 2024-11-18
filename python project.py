from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # For loading the background image
import os

root = Tk()
root.geometry("500x500")
root.title("PC Operations")
f = ('Bell MT', 15, 'bold')

# Function to resize the background image to fit the window
def resize_bg_image(event):
    new_width = event.width
    new_height = event.height
    bg_image_resized = bg_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    bg_photo_resized = ImageTk.PhotoImage(bg_image_resized)
    canvas.itemconfig(bg_image_id, image=bg_photo_resized)
    canvas.bg_photo_resized = bg_photo_resized  # Keep reference to avoid garbage collection

# Load the background image
bg_image = Image.open("lap.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas to place the background image
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill="both", expand=True)
bg_image_id = canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Bind the canvas resizing event to resize the background image accordingly
canvas.bind("<Configure>", resize_bg_image)

# PC Operations Functions
def shutdown():
    if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown?"):
        os.system("shutdown /s /t 0")

def restart():
    if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart?"):
        os.system("shutdown /r /t 0")

def logout():
    if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?"):
        os.system("shutdown /l")

def sleep():
    if messagebox.askyesno("Confirm Sleep", "Are you sure you want to put the system to sleep?"):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def lock_system():
    if messagebox.askyesno("Confirm Lock", "Are you sure you want to lock your system?"):
        os.system("rundll32.exe user32.dll,LockWorkStation")

def open_task_manager():
    if messagebox.askyesno("Open Task Manager", "Do you want to open the Task Manager?"):
        os.system("start taskmgr")

# Common button size and styling
button_width = 25
button_height = 2

# Frame to hold the content (label and buttons)
frame = Frame(root, bg='#E6E6FA')
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create label and place it at the top of the frame
lb1 = Label(frame, text='PC Operations', font=f, bg='#E6E6FA', fg='black')
lb1.grid(row=0, column=0, pady=20)  # pady to add some space between label and buttons

# List of buttons and their commands
buttons = [
    ("Shutdown", shutdown),
    ("Restart", restart),
    ("Logout", logout),
    ("Sleep", sleep),
    ("Lock System", lock_system),
    ("Task Manager", open_task_manager),
]

# Add buttons to the frame and center them
for i, (text, command) in enumerate(buttons):
    button = Button(frame, text=text, font=f, bg='#333333', fg='white', width=button_width, height=button_height, command=command)
    button.grid(row=i+1, column=0, pady=5)  # The i+1 places the buttons below the label

root.mainloop()
