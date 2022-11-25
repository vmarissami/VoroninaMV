import requests
import json
from tkinter import *
from tkinter import scrolledtext

def progg():
    repo = txt.get()

    url = f"https://api.github.com/repos/{repo}"
    rep_url = requests.get(url).json()

    try:
        rep_url['company']
        rep_url['email']
    except KeyError:
        rep_url['company'] = None
        rep_url['email'] = None

    with open("File.txt", "a+") as f:
        f.write(f"'company': '{rep_url['company']}'\n")
        f.write(f"'created_at': '{rep_url['created_at']}'\n")
        f.write(f"'email': '{rep_url['email']}'\n")
        f.write(f"'id': '{rep_url['id']}'\n")
        f.write(f"'name': '{rep_url['name']}'\n")
        f.write(f"'url': '{rep_url['url']}'\n")
        f.write("\n")
    with open("File.txt", "r+") as f1:
        line = f1.read()
        txt1.insert('1.0', line)

okno = Tk()
okno.title("Прикольчик")
okno.geometry('600x600')
okno.configure(bg='#9999CC')
lb = Label(okno, text="Введите имя пользователя/репозиторий", bg='#9999CC', font='Calibri 14')
lb1 = Label(okno, text="Например: ansible/ansible", bg='#9999CC')
lb.grid(padx=100, pady=55)
lb1.grid(padx=10, pady=20)
txt = Entry(okno, width=30, justify="center")
txt.grid(padx=10, pady=10)
but = Button(okno, text="Произвести хакерство", command=progg, bg='#00FF33')
but.grid(padx=10, pady=10)
txt1 = scrolledtext.ScrolledText(okno, height=15, width=58)
txt1.grid(padx=55, pady=10)
okno.mainloop()