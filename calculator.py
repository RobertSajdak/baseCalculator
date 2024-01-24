import tkinter as tk

# Create the main window.
window = tk.Tk()
window.title("Calculator")

# Create a file to display the result.
calculator_screen = tk.Entry(master=window)
calculator_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
