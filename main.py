import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)  # update every 1 second

# Main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)

# Clock Label
label = tk.Label(root, font=("Arial", 40), bg="black", fg="lime")
label.pack(expand=True, fill="both")

update_time()
root.mainloop()
