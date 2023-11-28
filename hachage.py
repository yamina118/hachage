import tkinter as tk
from tkinter import messagebox
from functools import partial

class HashTableStatic:
    def __init__(self, size=10):
        self.size = size
        self.hash_dictionary = {}

    def hash_div(self, x):
        return x % self.size

    def static_hashing_algorithm(self, value):
        key = self.hash_div(value)
        if key not in self.hash_dictionary:
            self.hash_dictionary[key] = value
            messagebox.showinfo("Operation Successful", f"Value '{value}' inserted into the hash table.")
        else:
            messagebox.showinfo("Collision", f"Collision occurred for value '{value}'. Choose a different value.")

    def delete_value(self, value):
        key = self.hash_div(value)
        if key in self.hash_dictionary and self.hash_dictionary[key] == value:
            del self.hash_dictionary[key]
            messagebox.showinfo("Operation Successful", f"Cell with value '{value}' deleted from the hash table.")
        else:
            messagebox.showinfo("Key not found", f"Value '{value}' not found in the hash table.")

    def search_value(self, value):
        key = self.hash_div(value)
        if key in self.hash_dictionary and self.hash_dictionary[key] == value:
            messagebox.showinfo("Value Found", f"Value '{value}' found in the hash table with key: {key}.")
        else:
            messagebox.showinfo("Value Not Found", f"Value '{value}' not found in the hash table.")

class HashTableDynamic:
    def __init__(self, size=10):
        self.size = size
        self.hash_dictionary = {}

    def hash_div(self, x):
        return x % self.size

    def dynamic_hashing_algorithm(self, value):
        key = self.hash_div(value)
        if key not in self.hash_dictionary:
            self.hash_dictionary[key] = value
            messagebox.showinfo("Operation Successful", f"Value '{value}' inserted into the hash table.")
        else:
            messagebox.showinfo("Collision", f"Collision occurred for value '{value}'. Choose a different value.")

    def delete_value(self, value):
        key = self.hash_div(value)
        if key in self.hash_dictionary and self.hash_dictionary[key] == value:
            del self.hash_dictionary[key]
            messagebox.showinfo("Operation Successful", f"Cell with value '{value}' deleted from the hash table.")
        else:
            messagebox.showinfo("Key not found", f"Value '{value}' not found in the hash table.")

    def search_value(self, value):
        key = self.hash_div(value)
        if key in self.hash_dictionary and self.hash_dictionary[key] == value:
            messagebox.showinfo("Value Found", f"Value '{value}' found in the hash table with key: {key}.")
        else:
            messagebox.showinfo("Value Not Found", f"Value '{value}' not found in the hash table.")

class HashGUI:
    def __init__(self, master, hash_table):
        self.master = master
        self.master.title("Hashing Algorithms")

        self.hash_table = hash_table

        frame = tk.Frame(master)
        frame.pack()

        self.algorithm_label = tk.Label(frame, text="Selected Algorithm:")
        self.algorithm_label.grid(row=0, column=0, pady=10, columnspan=2)

        value_label = tk.Label(frame, text="Enter value:")
        value_label.grid(row=1, column=0, pady=5)
        self.value_entry = tk.Entry(frame)
        self.value_entry.grid(row=1, column=1, pady=5)

        static_button = tk.Button(frame, text="Static Hashing", command=self.on_static_button_click, bg="lightblue")
        static_button.grid(row=2, column=0, pady=5)

        dynamic_button = tk.Button(frame, text="Dynamic Hashing", command=self.on_dynamic_button_click, bg="lightgreen")
        dynamic_button.grid(row=2, column=1, pady=5)

        insert_button = tk.Button(frame, text="Insert", command=self.on_insert_button_click)
        insert_button.grid(row=3, column=0, pady=5)

        search_button = tk.Button(frame, text="Search", command=self.on_search_button_click)
        search_button.grid(row=4, column=0, pady=5)

        delete_button = tk.Button(frame, text="Delete", command=self.on_delete_button_click)
        delete_button.grid(row=5, column=0, pady=5)

        display_button = tk.Button(frame, text="Display Dictionary", command=self.display_dictionary)
        display_button.grid(row=6, column=0, pady=5)

    def on_static_button_click(self):
        self.hash_table = HashTableStatic()
        self.algorithm_label.config(text="Selected Algorithm: Static Hashing")

    def on_dynamic_button_click(self):
        self.hash_table = HashTableDynamic()
        self.algorithm_label.config(text="Selected Algorithm: Dynamic Hashing")

    def on_insert_button_click(self):
        value = int(self.value_entry.get())
        if isinstance(self.hash_table, HashTableStatic):
            self.hash_table.static_hashing_algorithm(value)
        elif isinstance(self.hash_table, HashTableDynamic):
            self.hash_table.dynamic_hashing_algorithm(value)

    def on_search_button_click(self):
        value = int(self.value_entry.get())
        self.hash_table.search_value(value)

    def on_delete_button_click(self):
        value = int(self.value_entry.get())
        self.hash_table.delete_value(value)

    def display_dictionary(self):
        dictionary_window = tk.Toplevel(self.master)
        dictionary_window.title("Hash Dictionary")

        text_widget = tk.Text(dictionary_window)
        text_widget.insert(tk.END, "Dictionary:\n")
        for key, value in self.hash_table.hash_dictionary.items():
            text_widget.insert(tk.END, f"Key: {key}, Value: {value}\n")

        text_widget.pack(padx=10, pady=10)

# Create the main window
window = tk.Tk()

# Create a placeholder for hash_table (it will be set in on_static_button_click or on_dynamic_button_click)
hash_table = None

# Create an instance of the HashGUI class
hash_gui = HashGUI(window, hash_table)

# Start the main loop
window.mainloop()
