import tkinter as tk

def show_hashing_interface():
    hashing_frame.pack_forget()
    indexing_frame.pack_forget()

    # Execute the code from hachinter.py
    with open("hachage.py", "r") as file:
        code = file.read()
        exec(code)

# Create the main window
root = tk.Tk()
root.title("Hashing and Indexing")

# Frames for Hashing and Indexing interfaces
hashing_frame = tk.Frame(root)
indexing_frame = tk.Frame(root)

# Contents of Indexing Interface
indexing_label = tk.Label(indexing_frame, text="Indexing Interface")
indexing_label.pack()

# Buttons for Hashing and Indexing
hashing_button = tk.Button(root, text="Hashing", command=show_hashing_interface, font=("Arial", 18, "bold"), padx=20, pady=10, bg="#4CAF50", fg="white")
indexing_button = tk.Button(root, text="Indexing", command=lambda: indexing_frame.pack_forget(), font=("Arial", 18, "bold"), padx=20, pady=10, bg="#2196F3", fg="white")

# Pack the buttons into the main window
hashing_button.pack(side=tk.LEFT, padx=20)
indexing_button.pack(side=tk.RIGHT, padx=20)

# Start the main event loop
root.mainloop()
