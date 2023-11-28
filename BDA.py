import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.hash_dictionary = {}
        self.current_hash_function = None
        self.current_collision_resolution = None

    def hash_div(self, x):
        return x % self.size

    def hash_middle_square(self, x):
        squared = x ** 2
        middle_digits = self.extract_middle_digits(squared)
        return middle_digits % self.size

    def hash_transformation_radix(self, x, base=16):
        return int(str(x), base) % self.size

    def linear_probing(self, key, i):
        return (key + i) % self.size

    def double_hashing(self, key, i):
        hash1 = key % self.size
        hash2 = 1 + (key % (self.size - 1))
        return (hash1 + i * hash2) % self.size

    def separate_chaining(self, key, value):
        if key not in self.hash_dictionary:
            self.hash_dictionary[key] = [value]
        else:
            self.hash_dictionary[key].append(value)

    def internal_chaining(self, key, value):
        if key not in self.hash_dictionary:
            self.hash_dictionary[key] = [value]
        else:
            self.hash_dictionary[key][0] += value

    def extract_middle_digits(self, num):
        num_str = str(num)
        middle_start = (len(num_str) - 2) // 2
        middle_end = middle_start + 2
        middle_digits = int(num_str[middle_start:middle_end])
        return middle_digits

    def insert_value(self, value):
        if self.current_hash_function is None or self.current_collision_resolution is None:
            messagebox.showinfo("Error", "Please select a hashing algorithm and a collision resolution method before inserting.")
            return

        key = self.current_hash_function(value)
        i = 0
        while key in self.hash_dictionary and self.hash_dictionary[key] is not None:
            if self.current_collision_resolution == "Linear Probing":
                key = self.linear_probing(key, i)
            elif self.current_collision_resolution == "Double Hashing":
                key = self.double_hashing(key, i)
            i += 1

        if self.current_collision_resolution in ["Separate Chaining", "Internal Chaining"]:
            self.hash_dictionary[key] = [value]
        else:
            self.hash_dictionary[key] = value

        messagebox.showinfo("Operation Successful", f"Value '{value}' inserted into the hash table.")

    def delete_value(self, key):
        if key in self.hash_dictionary:
            del self.hash_dictionary[key]
            messagebox.showinfo("Operation Successful", f"Cell with key '{key}' deleted from the hash table.")
        else:
            messagebox.showinfo("Key not found", f"Key '{key}' not found in the hash table.")

    def search_value(self, key):
        if key in self.hash_dictionary:
            messagebox.showinfo("Key Found", f"Key '{key}' found in the hash table with value(s): {self.hash_dictionary[key]}.")
        else:
            messagebox.showinfo("Key Not Found", f"Key '{key}' not found in the hash table.")

class HashGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hashing Algorithms")

        self.hash_table = HashTable()
        self.current_collision_resolution = None

        frame = tk.Frame(master)
        frame.pack()

        self.algorithm_label = tk.Label(frame, text="Selected Algorithm:")
        self.algorithm_label.grid(row=0, column=0, pady=10, columnspan=3)

        value_label = tk.Label(frame, text="Enter value:")
        value_label.grid(row=1, column=0, pady=5)

        self.value_entry = tk.Entry(frame)
        self.value_entry.grid(row=1, column=1, pady=5)

        # Dropdown for selecting hashing function
        self.hash_function_var = tk.StringVar()
        self.hash_function_var.set("Select Hashing Function")
        hash_function_menu = tk.OptionMenu(frame, self.hash_function_var, "Select Hashing Function", "Division", "Middle Square", "Transformation Radix")
        hash_function_menu.grid(row=1, column=2, pady=5)

        # Dropdown for selecting collision resolution method
        self.collision_resolution_var = tk.StringVar()
        self.collision_resolution_var.set("Select Collision Resolution")
        collision_resolution_menu = tk.OptionMenu(frame, self.collision_resolution_var, "Select Collision Resolution", "Linear Probing", "Double Hashing", "Separate Chaining", "Internal Chaining")
        collision_resolution_menu.grid(row=1, column=3, pady=5)

        insert_button = tk.Button(frame, text="Insert Value", command=self.on_insert_button_click)
        insert_button.grid(row=2, column=0, pady=5)

        search_button = tk.Button(frame, text="Search Value", command=self.on_search_button_click)
        search_button.grid(row=3, column=0, pady=5)

        delete_button = tk.Button(frame, text="Delete Value", command=self.on_delete_button_click)
        delete_button.grid(row=4, column=0, pady=5)

        display_button = tk.Button(frame, text="Display Dictionary", command=self.display_dictionary)
        display_button.grid(row=5, column=0, pady=5)

        self.dictionary_frame = tk.Frame(frame)
        self.dictionary_frame.grid(row=2, column=1, rowspan=4, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Add scrollbar to the dictionary frame
        scrollbar = tk.Scrollbar(self.dictionary_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Text widget to display dictionary content
        self.dictionary_text = tk.Text(self.dictionary_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        self.dictionary_text.pack(expand=True, fill=tk.BOTH)

        # Configure the scrollbar to work with the text widget
        scrollbar.config(command=self.dictionary_text.yview)

    def on_insert_button_click(self):
        value = int(self.value_entry.get())
        hash_function_name = self.hash_function_var.get()
        if hash_function_name == "Select Hashing Function":
            messagebox.showinfo("Error", "Please select a hashing function before inserting.")
            return

        collision_resolution = self.collision_resolution_var.get()
        if collision_resolution == "Select Collision Resolution":
            messagebox.showinfo("Error", "Please select a collision resolution method before inserting.")
            return

        hash_function = self.get_hash_function(hash_function_name)
        if hash_function is None:
            messagebox.showinfo("Error", "Invalid hashing function selected.")
            return

        self.hash_table.current_hash_function = hash_function
        self.hash_table.current_collision_resolution = collision_resolution

        self.hash_table.insert_value(value)
        self.update_dictionary_display()

    def on_search_button_click(self):
        key = int(self.value_entry.get())
        self.hash_table.search_value(key)

    def on_delete_button_click(self):
        key = int(self.value_entry.get())
        self.hash_table.delete_value(key)
        self.update_dictionary_display()

    def display_dictionary(self):
        self.update_dictionary_display()

    def update_dictionary_display(self):
        self.dictionary_text.delete(1.0, tk.END)
        for key, value in self.hash_table.hash_dictionary.items():
            self.dictionary_text.insert(tk.END, f"Key: {key}, Value: {value}\n")

    def get_hash_function(self, name):
        if name == "Division":
            return self.hash_table.hash_div
        elif name == "Middle Square":
            return self.hash_table.hash_middle_square
        elif name == "Transformation Radix":
            return self.hash_table.hash_transformation_radix
        else:
            return None

# Create the main window
window = tk.Tk()

# Create an instance of the HashGUI class
hash_gui = HashGUI(window)

# Start the main loop
window.mainloop()
