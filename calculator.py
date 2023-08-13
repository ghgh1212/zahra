from tkinter import *

def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(END, current + str(number))

def button_clear():
    display.delete(0, END)

def button_equal():
    result = eval(display.get())
    display.delete(0, END)
    display.insert(END, result)

# Create a Tkinter window
window = Tk()
window.title("Simple Calculator")

# Create an Entry widget to display the numbers and results
display = Entry(window, width=20, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create number buttons
button_1 = Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Create operation buttons
button_add = Button(window, text="+", padx=19, pady=10, command=lambda: button_click('+'))
button_subtract = Button(window, text="-", padx=20, pady=10, command=lambda: button_click('-'))
button_multiply = Button(window, text="*", padx=20, pady=10, command=lambda: button_click('*'))
button_divide = Button(window, text="/", padx=20, pady=10, command=lambda: button_click('/'))
button_equal = Button(window, text="=", padx=49, pady=10, command=button_equal)
button_clear = Button(window, text="Clear", padx=38, pady=10, command=button_clear)

# Place the buttons on the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

# Start the Tkinter event loop
window.mainloop()
