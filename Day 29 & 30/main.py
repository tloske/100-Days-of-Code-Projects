from multiprocessing import Process, Queue
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = "".join(hard(nr_letters, nr_symbols, nr_numbers))
    password_input.delete(0, tkinter.END)
    password_input.insert(0, password)
    pyperclip.copy(password)


def hard(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    q = Queue()
    p_letters = Process(target=get_symbol_list,
                        args=(nr_letters, letters, q,))
    p_symbols = Process(target=get_symbol_list,
                        args=(nr_symbols, symbols, q,))
    p_numbers = Process(target=get_symbol_list,
                        args=(nr_numbers, numbers, q,))
    p_letters.start()
    p_symbols.start()
    p_numbers.start()
    password += q.get()
    password += q.get()
    password += q.get()
    p_letters.join()
    p_symbols.join()
    p_numbers.join()
    random.shuffle(password)
    return password


def get_symbol_list(amount, list, q):
    q.put([random.choice(list) for _ in range(amount)])
# ---------------------------- SAVE PASSWORD ------------------------------- #


def get_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {}
    else:
        return data


def search_for_website():
    website = website_input.get().lower()
    data = get_data()

    if website in data:
        messagebox.showinfo(
            title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
    else:
        messagebox.showwarning(
            title="No Entry", message=f"No password entry for {website} found.")


def save_password():
    website = website_input.get().lower()
    email = email_input.get()
    password = password_input.get()

    data = get_data()

    data[website] = {"email": email, "password": password}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=f"{website}", message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

    if not is_ok:
        return

    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    except:
        messagebox.showerror(title="Error", message="Error saving File !!!")
    else:
        website_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)

    # ---------------------------- UI SETUP ------------------------------- #


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    canvas = tkinter.Canvas(width=200, height=200)
    logo_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)

    website_label = tkinter.Label(text="Website:")
    website_label.grid(column=0, row=1, sticky="W")

    global website_input
    website_input = tkinter.Entry(width=35)
    website_input.grid(column=1, row=1, sticky="EW")
    website_input.focus()

    search_button = tkinter.Button(text="Search", command=search_for_website)
    search_button.grid(column=2, row=1, sticky="EW")

    email_label = tkinter.Label(text="Email/Username:")
    email_label.grid(column=0, row=2, sticky="W")
    global email_input
    email_input = tkinter.Entry(width=35)
    email_input.insert(0, "user@web.com")
    email_input.grid(column=1, row=2, columnspan=2, sticky="EW")

    password_label = tkinter.Label(text="Password:")
    password_label.grid(column=0, row=3, sticky="W")
    global password_input
    password_input = tkinter.Entry(width=30)
    password_input.grid(column=1, row=3, sticky="EW")
    password_button = tkinter.Button(
        text="Generate Password", command=generate_password)
    password_button.grid(column=2, row=3, sticky="EW")

    add_button = tkinter.Button(text="Add", command=save_password, width=36)
    add_button.grid(column=1, row=4, columnspan=2, sticky="W")

    window.mainloop()
