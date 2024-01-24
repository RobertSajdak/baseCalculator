import tkinter as tk


# The function responsible for adding character strings to the calculator display
# to represent digits and operators.
def button_click(entry):
    current = calculator_screen.get()
    calculator_screen.delete(0, tk.END)
    calculator_screen.insert(tk.END, current + str(entry))


# A function that cleans the calculator display.
def button_clear():
    calculator_screen.delete(0, tk.END)


# A function that takes the contents from the display
# and performs calculations using the 'eval' built-in function.
def button_equal():
    expression = calculator_screen.get()
    try:
        result = eval(expression)
        calculator_screen.delete(0, tk.END)
        calculator_screen.insert(tk.END, result)
    except Exception as ex:
        calculator_screen.delete(0, tk.END)
        calculator_screen.insert(tk.END, "Error")


# Create the main window.
window = tk.Tk()
window.title("Calculator")

# Create a file to display the result.
calculator_screen = tk.Entry(master=window)
calculator_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Buttons settings
padx, pady = 20, 10

# Create number buttons.
button_1 = tk.Button(window, text="1", padx=padx, pady=pady, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=padx, pady=pady, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=padx, pady=pady, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=padx, pady=pady, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=padx, pady=pady, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=padx, pady=pady, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=padx, pady=pady, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=padx, pady=pady, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=padx, pady=pady, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=padx, pady=pady, command=lambda: button_click(0))

# Create of operation buttons.
button_add = tk.Button(window, text="+", padx=padx, pady=pady, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=padx, pady=pady, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=padx, pady=pady, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=padx, pady=pady, command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", padx=padx, pady=pady, command=button_equal)
button_clear = tk.Button(window, text="C", padx=padx, pady=pady, command=button_clear)
