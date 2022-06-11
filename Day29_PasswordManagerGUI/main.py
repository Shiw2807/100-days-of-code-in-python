from cProfile import label
from tkinter import *
from tkinter import messagebox
from turtle import title
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=25,pady=50)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list= password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password= "".join(password_list)
    password_box.insert(0,password)
    pyperclip.copy(password)    


def save():
    website = website_box.get()
    email = email_box.get()
    password = password_box.get()

    new_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            
        except:

            with open("data.json", "w") as data_file: 
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file: 
                json.dump(data,data_file,indent=4)

        finally:
            website_box.delete(0,END)
            password_box.delete(0,END)


def find_password():
        website=website_box.get()

        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file)

        except FileNotFoundError:
            messagebox.showerror(title="Error",message= "No such Data File found")

        else:
            if website in data:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website, message= f" email= {email}\n Password = {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists!")


website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

website_box = Entry(width=35)
website_box.grid(column=1,row=1)
website_box.focus()

email_label = Label(text= "Email/Username: ")
email_label.grid(column=0,row=2)

email_box = Entry(width=35)
email_box.grid(column=1,row=2)
email_box.insert(0, "shiws2807@gmail.com")

password_label = Label(text="Password: ", width=21)
password_label.grid(column=0,row=3)

password_box = Entry(width=35)
password_box.grid(column=1,row=3)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2,row=3)

add = Button(text="Add", width=45, command=save)
add.grid(column=1,row=4,columnspan=2)

search_box=Button(text="Search", width=14, command=find_password)
search_box.grid(column=2,row=1)

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(93,100,image=logo_image)
canvas.grid(column=1,row=0)


window.mainloop()