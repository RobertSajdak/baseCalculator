import tkinter as tk

# Create the main window.
window = tk.Tk()
window.title("Calculator")

# Create a file to display the result.
calculator_screen = tk.Entry(master=window)
calculator_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Buttons settings
padx, pady = 20, 10

# Create number buttons.
button_1 = tk.Button(window, text="1", padx=padx, pady=pady)
button_2 = tk.Button(window, text="2", padx=padx, pady=pady)
button_3 = tk.Button(window, text="3", padx=padx, pady=pady)
button_4 = tk.Button(window, text="4", padx=padx, pady=pady)
button_5 = tk.Button(window, text="5", padx=padx, pady=pady)
button_6 = tk.Button(window, text="6", padx=padx, pady=pady)
button_7 = tk.Button(window, text="7", padx=padx, pady=pady)
button_8 = tk.Button(window, text="8", padx=padx, pady=pady)
button_9 = tk.Button(window, text="9", padx=padx, pady=pady)
button_0 = tk.Button(window, text="0", padx=padx, pady=pady)

# Create of operation buttons.
button_add = tk.Button(window, text="+", padx=padx, pady=pady)
button_subtract = tk.Button(window, text="-", padx=padx, pady=pady)
button_multiply = tk.Button(window, text="*", padx=padx, pady=pady)
button_divide = tk.Button(window, text="/", padx=padx, pady=pady)
button_equal = tk.Button(window, text="=", padx=padx, pady=pady)
button_clear = tk.Button(window, text="C", padx=padx, pady=pady)
