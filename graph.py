import tkinter as tk
from tkinter import messagebox

def handle_button_click(action):
    messagebox.showinfo("Button Clicked", f"{action} button clicked!")

# Create the main window
root = tk.Tk()
root.title("Hashing and Indexing")

# Configure the window size and position
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Configure window background color
root.configure(bg="#F0F0F0")

# Create and configure the buttons with updated styles
hashing_button = tk.Button(root, text="Hashing", command=lambda: handle_button_click("Hashing"), font=("Arial", 18, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white")
indexing_button = tk.Button(root, text="Indexing", command=lambda: handle_button_click("Indexing"), font=("Arial", 18, "bold"), padx=20, pady=10, bg="#2196F3", fg="white")

# Pack the buttons into the window
hashing_button.pack(side=tk.LEFT, padx=20)
indexing_button.pack(side=tk.RIGHT, padx=20)

# Start the main event loop
root.mainloop()
