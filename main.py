from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("Kilometers to Miles Converter")
window.config(padx=50, pady=50)


# The conversion formula
# 1 mile = 1.6 kilometers
def conversion():
    input_num = float(user_input.get())
    if conversion_mode.get() == 1:
        result = input_num / 1.609

    elif conversion_mode.get() == 2:
        result = input_num * 1.609
    result = round(result, 4)
    result_label.config(text=result)


# Invert labels and title when a new radiobutton is clicked
def invert_labels():
    if conversion_mode.get() == 1:
        window.title("Kilometers to Miles Converter")
        input_label.config(text="Km")
        result_text_label.config(text="Miles")
    elif conversion_mode.get() == 2:
        window.title("Miles to Kilometers Converter")
        input_label.config(text="Miles")
        result_text_label.config(text="Km")


# Widgets

# Start by Convert to Miles mode (value=1)
conversion_mode = IntVar(value=1)
to_miles = Radiobutton(text="Convert to Miles", value=1, variable=conversion_mode, command=invert_labels)
to_km = Radiobutton(text="Convert to Km", value=2, variable=conversion_mode, command=invert_labels)
to_miles.grid(row = 0, column = 1)
to_km.grid(row = 0, column = 2)

user_input = Entry(width=10, justify="center")
user_input.config(font=("Arial", 18, "bold"))
user_input.insert(END, string='0')
user_input.grid(row=1, column=1)

input_label = Label(text="Km", font=("Arial", 18))
input_label.grid(row=1, column=2)

result_text_label = Label(text="Miles", font=("Arial", 18))
result_text_label.grid(row=2, column=2)

equal_label = Label(text="is equal to", font=("Arial", 18))
equal_label.grid(row=2, column=0)

result_label = Label(text=0, font=("Arial", 18, "bold"))
result_label.grid(row=2, column=1, padx=10, pady=10)

calc_button = Button(text="Calculate", font=("Arial", 16), command=conversion)
calc_button.grid(row=3, column=1, pady=10)


window.mainloop()
