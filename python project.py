from tkinter import *
import os
import ctypes
from tkinter import messagebox

root = Tk()
root.geometry("325x200")
root.title("PC Shutdown, Restart, Logout")
root.config(bg='#E6E6FA')
f = ('Bell MT', 15, 'bold')
def shutdown():
     if messagebox.askyesno("Confirm Logout", "Are you sure you want to Shutdown?"):
        os.system("shutdown /s /t 0")
def restart():
     if messagebox.askyesno("Confirm Logout", "Are you sure you want to Restart?"):
        os.system("shutdown /r /t 0")
def logout():
    if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?"):
        os.system("shutdown /l")

lb1 = Label(root, text='Shutdown, Restart or Logout', font=f, bg='#E6E6FA', fg='#303030')
lb1.pack(pady=5)

Button(root, text='Shutdown', font=f, bg='#333333', fg='white', command=shutdown).pack(pady=5)
Button(root, text='Restart', font=f, bg='#333333', fg='white', command=restart).pack(pady=5)
Button(root, text='Logout', font=f, bg='#333333', fg='white', command=logout).pack(pady=5)

root.mainloop()
