import tkinter as tk
import time

def clock():
    current_time = time.strftime('%H:%M:%S')  
    label.config(text=current_time)
    label.after(1000, clock)  

root = tk.Tk()
root.title("Digital Clock")
root.configure(background='black')

label = tk.Label(root, font=('Helvetica', 80), background='black', foreground='cyan')
label.pack(padx=20, pady=20)

def toggle_color():
    current_color = label['foreground']
    new_color = 'cyan' if current_color == 'white' else 'white'
    label.config(foreground=new_color)
    label.after(500, toggle_color)  

clock()

toggle_color()

root.mainloop()