from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + \
                    [random.choice(symbols) for char in range(nr_symbols)] + \
                    [str(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_textbox.delete(0, END)
    password_textbox.insert(0, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_name = website_textbox.get()
    user_id = email_textbox.get()
    password = password_textbox.get()
    if website_name == "" or \
            user_id == "" or \
            password == "":
        messagebox.showinfo("Missing Details", message="Please fill out all boxes")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details to save:\nEmail/Username: {user_id}\nPassword: {password}")
        if is_ok:
            with open(file="data.txt", mode="a") as save_file:
                save_file.write(f"{website_name} | {user_id} | {password}\n")
                website_textbox.delete(0, "end")
                password_textbox.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #


BACKGROUND = "white"

window = Tk()
window.title("Password Manager App")
window.config(background=BACKGROUND, padx=10, pady=20)

canvas = Canvas(height=200, width=200, background='white', highlightthickness=0)

pwdmgr_logo = PhotoImage(file="logo.png")
pwdmgr_logo.config(height=200, width=200)
canvas.create_image(200, 100, image=pwdmgr_logo)
canvas.grid(column=0, row=0, columnspan=3, sticky=(N, W, E, S))

# Create website label and textbox
website_label = Label(justify="right", width=15, text="Website:", bg=BACKGROUND)
website_label.grid(column=0, row=1, sticky=(N, W, E, S))
website_textbox = Entry(width=35, bg=BACKGROUND)
website_textbox.grid(column=1, row=1, columnspan=2, sticky=(N, W, E, S))
website_textbox.focus()

# Create Email Label and textbox
email_label = Label(justify="right", width=15, text="Email/Username:", bg=BACKGROUND)
email_label.grid(column=0, row=2, sticky=(N, W, E, S))
email_textbox = Entry(width=35, bg=BACKGROUND)
email_textbox.grid(columnspan=2, column=1, row=2, sticky=(N, W, E, S))
email_textbox.insert(index=0, string="gteachey@outlook.com")
# email_textbox.insert(END,"global")
# Create Password Label, textbox, and button
password_label = Label(justify="right", text="Password::", bg=BACKGROUND, width=15)
password_label.grid(column=0, row=3, sticky=(N, W, E, S))
password_textbox = Entry(width=25, bg=BACKGROUND)
password_textbox.grid(column=1, row=3, sticky=(N, W, E, S))
gen_pass_button = Button(text="Generate Password", bg=BACKGROUND, command=gen_password)
gen_pass_button.grid(column=2, row=3, sticky=(N, W, E, S))

# Create Add Button
add_button = Button(text="Add", width=30, bg=BACKGROUND, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=(N, W, E, S))

window.mainloop()
