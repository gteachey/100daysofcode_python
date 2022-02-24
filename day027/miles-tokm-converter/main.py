from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)
entry_input = Entry()
entry_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.config(padx=10)
miles_label.grid(column=2, row=0)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
equal_to_label = Label(text="is equal to")
equal_to_label.config(padx=10)
equal_to_label.grid(column=0, row=1)
km_conversion = 0
km_conversion_label = Label(text=km_conversion)
km_conversion_label.grid(column=1, row=1)


def button_clicked():
    if (entry_input.get().isnumeric()):
        km_conversion = round(int(entry_input.get()) * 1.609344, 2)
        print(km_conversion)
        km_conversion_label.configure(text=km_conversion)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
window.mainloop()
