from tkinter import *

# Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# LABEL
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100,y=0)
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label["text"] = my_input.get()


button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=0,y=200)
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=button_clicked)
# button.pack()
# button.place(x=0,y=200)
button2.grid(column=3, row=0)
# Entry
my_input = Entry(width=10)
# my_input.pack()
# my_input.place(x=150,y=150)
my_input.grid(column=4, row=3)
print(my_input.get())
window.mainloop()
