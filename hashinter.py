import tkinter as tk
from tkinter import messagebox
from functools import partial

class HashTable:
    def __init__(self):
        self.hash_dictionary = {}

    def hash_div(self, x, N):
        return x % N

    def static_hashing_algorithm(self, value):
        key = self.hash_div(value, len(self.hash_dictionary) + 1)
        if key not in self.hash_dictionary:
            self.hash_dictionary[key] = value
            messagebox.showinfo("Operation Successful", f"Value '{value}' inserted into the hash table.")
        else:
            messagebox.showinfo("Collision", f"Collision occurred for value '{value}'. Choose a different value.")

    def dynamic_hashing_algorithm(self, value):
        key = self.hash_div(value, len(self.hash_dictionary) + 1)
        if key not in self.hash_dictionary:
            self.hash_dictionary[key] = value
            messagebox.showinfo("Operation Successful", f"Value '{value}' inserted into the hash table.")
        else:
            messagebox.showinfo("Collision", f"Collision occurred for value '{value}'. Choose a different value.")

    def delete_value(self, value):
        key = self.hash_div(value, len(self.hash_dictionary) + 1)
        if key in self.hash_dictionary:
            del self.hash_dictionary[key]
            messagebox.showinfo("Operation Successful", f"Cell with value '{value}' deleted from the hash table.")
        else:
            messagebox.showinfo("Key not found", f"Value '{value}' not found in the hash table.")

    def search_value(self, value):
        key = self.hash_div(value, len(self.hash_dictionary) + 1)
        if key in self.hash_dictionary:
            messagebox.showinfo("Value Found", f"Value '{value}' found in the hash table with key: {key}.")
        else:
            messagebox.showinfo("Value Not Found", f"Value '{value}' not found in the hash table.")

# Create the main window
window = tk.Tk()
window.title("Hashing Algorithms")

# Create an instance of the HashTable class
hash_table = HashTable()

# Function to choose static hashing
def on_static_button_click():
    algorithm_label.config(text="Selected Algorithm: Static Hashing")
    insert_button.config(command=partial(hash_table.static_hashing_algorithm, int(value_entry.get())))
    search_button.config(command=partial(hash_table.search_value, int(value_entry.get())))
    delete_button.config(command=partial(hash_table.delete_value, int(value_entry.get())))

# Function to choose dynamic hashing
def on_dynamic_button_click():
    algorithm_label.config(text="Selected Algorithm: Dynamic Hashing")
    insert_button.config(command=partial(hash_table.dynamic_hashing_algorithm, int(value_entry.get())))
    search_button.config(command=partial(hash_table.search_value, int(value_entry.get())))
    delete_button.config(command=partial(hash_table.delete_value, int(value_entry.get())))

# Rest of your code remains the same...


# Function to display the dictionary
def display_dictionary():
    dictionary_window = tk.Toplevel(window)
    dictionary_window.title("Hash Dictionary")

    text_widget = tk.Text(dictionary_window)
    text_widget.insert(tk.END, "Dictionary:\n")
    for key, value in hash_table.hash_dictionary.items():
        text_widget.insert(tk.END, f"Key: {key}, Value: {value}\n")

    text_widget.pack(padx=10, pady=10)

# Label to display the selected algorithm
algorithm_label = tk.Label(window, text="Selected Algorithm:")
algorithm_label.pack(pady=10)

# Entry for user input (value)
value_label = tk.Label(window, text="Enter value:")
value_label.pack(pady=5)
value_entry = tk.Entry(window)
value_entry.pack(pady=5)

# Buttons for choosing algorithms
static_button = tk.Button(window, text="Static Hashing", command=on_static_button_click)
static_button.pack(pady=5)

dynamic_button = tk.Button(window, text="Dynamic Hashing", command=on_dynamic_button_click)
dynamic_button.pack(pady=5)

# Buttons for Insert, Search, Delete
insert_button = tk.Button(window, text="Insert")
insert_button.pack(pady=5)

search_button = tk.Button(window, text="Search")
search_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete")
delete_button.pack(pady=5)

# Button to display the dictionary
display_button = tk.Button(window, text="Display Dictionary", command=display_dictionary)
display_button.pack(pady=10)

# Start the main loop
window.mainloop()