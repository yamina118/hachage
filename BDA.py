import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.hash_dictionary = {}
        self.current_hash_function = self.hash_div  # Default hash function
        self.current_collision_resolution = self.linear_probing  # Default collision resolution

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
        key = self.current_hash_function(value)
        i = 0
        while key in self.hash_dictionary and self.hash_dictionary[key] is not None:
            if self.current_collision_resolution == self.linear_probing:
                key = self.linear_probing(key, i)
            elif self.current_collision_resolution == self.double_hashing:
                key = self.double_hashing(key, i)
            i += 1

        if self.current_collision_resolution in [self.separate_chaining, self.internal_chaining]:
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
            values = self.hash_dictionary[key]
            messagebox.showinfo("Key Found", f"Key '{key}' found in the hash table with value(s): {values}.")
        else:
            messagebox.showinfo("Key Not Found", f"Key '{key}' not found in the hash table.")

class HashGUI:
    def __init__(self, master, hash_table):
        self.master = master
        self.master.title("Hashing Algorithms")

        self.hash_table = hash_table

        frame = tk.Frame(master)
        frame.pack()

        # Dropdown for selecting algorithm type
        self.algorithm_type_var = tk.StringVar()
        self.algorithm_type_var.set("Select Algorithm Type")
        algorithm_type_menu = tk.OptionMenu(frame, self.algorithm_type_var, "Select Algorithm Type", "Static", "Dynamic", command=self.on_algorithm_type_selected)
        algorithm_type_menu.grid(row=0, column=0, pady=5, padx=5)

        # Dropdown for selecting hashing function
        self.hash_function_var = tk.StringVar()
        self.hash_function_var.set("Select Hashing Function")
        hash_function_menu = tk.OptionMenu(frame, self.hash_function_var, "Select Hashing Function", "Division", "Middle Square", "Transformation Radix")
        hash_function_menu.grid(row=1, column=0, pady=5, padx=5)

        # Dropdown for selecting collision resolution method
        self.collision_resolution_var = tk.StringVar()
        self.collision_resolution_var.set("Select Collision Resolution")
        collision_resolution_menu = tk.OptionMenu(frame, self.collision_resolution_var, "Select Collision Resolution", "Linear Probing", "Double Hashing", "Separate Chaining", "Internal Chaining")
        collision_resolution_menu.grid(row=2, column=0, pady=5, padx=5)

        # Text input for insert
        insert_label = tk.Label(frame, text="Insert Value:")
        insert_label.grid(row=3, column=0, pady=5, padx=5)
        self.insert_entry = tk.Entry(frame)
        self.insert_entry.grid(row=3, column=1, pady=5, padx=5)

        # Insert button
        insert_button = tk.Button(frame, text="Insert", command=self.on_insert_button_click)
        insert_button.grid(row=3, column=2, pady=5, padx=5)

        # Text input for search
        search_label = tk.Label(frame, text="Search Value:")
        search_label.grid(row=4, column=0, pady=5, padx=5)
        self.search_entry = tk.Entry(frame)
        self.search_entry.grid(row=4, column=1, pady=5, padx=5)

        # Search button
        search_button = tk.Button(frame, text="Search", command=self.on_search_button_click)
        search_button.grid(row=4, column=2, pady=5, padx=5)

        # Button to display the dictionary
        display_button = tk.Button(frame, text="Display Dictionary", command=self.display_dictionary)
        display_button.grid(row=5, column=0, columnspan=3, pady=5, padx=5)

        # Text input for dictionary
        self.dictionary_text = tk.Text(frame, height=10, width=30)
        self.dictionary_text.grid(row=6, column=0, columnspan=3, pady=10, padx=5)

    def on_algorithm_type_selected(self, algorithm_type):
        if algorithm_type == "Static":
            # Set hash functions and collision resolutions for static hashing
            self.hash_function_var.set("Division")
            self.collision_resolution_var.set("Linear Probing")
            self.hash_table.current_hash_function = self.hash_table.hash_div
            self.hash_table.current_collision_resolution = self.hash_table.linear_probing
        elif algorithm_type == "Dynamic":
            # Set hash functions and collision resolutions for dynamic hashing
            self.hash_function_var.set("Middle Square")
            self.collision_resolution_var.set("Double Hashing")
            self.hash_table.current_hash_function = self.hash_table.hash_middle_square
            self.hash_table.current_collision_resolution = self.hash_table.double_hashing

    def on_insert_button_click(self):
        value = int(self.insert_entry.get())
        self.hash_table.insert_value(value)
        self.display_dictionary()

    def on_search_button_click(self):
        value = int(self.search_entry.get())
        self.hash_table.search_value(value)

    def display_dictionary(self):
        self.dictionary_text.delete(1.0, tk.END)  # Clear the text widget
        for key, value in self.hash_table.hash_dictionary.items():
            line = f"Key: {key}, Value: {value}\n"
            self.dictionary_text.insert(tk.END, line)

        # Add "Delete" button next to each value in the dictionary display
            delete_button = tk.Button(self.dictionary_text, text="Delete", command=lambda k=key: self.on_delete_button_click(k))
            self.dictionary_text.window_create(tk.END, window=delete_button)

    def on_delete_button_click(self, key):
        self.hash_table.delete_value(key)
        self.display_dictionary()

# Create the main window
window = tk.Tk()

# Create an instance of the HashTable class
hash_table = HashTable()

# Create an instance of the HashGUI class
hash_gui = HashGUI(window, hash_table)

# Start the main loop
window.mainloop()
