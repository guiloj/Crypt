import random
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *

def password_get():
    def decrypt_entry():
        message = E2.get()
        try:
            encoded = message.encode()
            f2 = Fernet(key)
            decrypted = f2.decrypt(encoded)

            original_message = decrypted.decode()
            ent = Entry(root, state='readonly', readonlybackground='white', fg='black')
            print('test')
            var = StringVar()
            var.set(original_message)
            ent.config(textvariable=var, relief='flat')
            ent.place(relx = 0., rely = 0.12, anchor = W)

        except:
            ent = Entry(root, state='readonly', readonlybackground='white', fg='black')
            var = StringVar()
            var.set('key error!')
            ent.config(textvariable=var, relief='flat')
            ent.place(relx = 0., rely = 0.12, anchor = W)
            return
    def encrypt_entry():
        message = E2.get()
        encoded = message.encode()
        f = Fernet(key)
        encryped = f.encrypt(encoded)
        ent = Entry(root, state='readonly', readonlybackground='white', fg='black')
        var = StringVar()
        var.set(encryped.decode())
        ent.config(textvariable=var, relief='flat')
        ent.place(relx = 0., rely = 0.12, anchor = W)

    global Entry
    e1e = E1.get()
    password = e1e.encode()

    salt =b'\xef\xc3U\x95\xfb!k\xc2\xdb+\xc4*\xbf\x85\xb6m[\xbc\xb1\x84\xc6\xbf\x19\xe6S\xba2\x8c\xbf\xac\x9b\xc2\xe9j\xbe\xea\xcd\x06~\xd9\x1f!\xdb_D\xaa\xbb\xfd\x9d\xc5"\xda\xfe\xd0\xe1\xb7\x8aH\xed\xbb\x86\x0c_kw\xf9\x8d\xdd/\xf4\xbc\xeal$\x7f\x12\xd8\xed6C|\x0c\xfb'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base = base64.urlsafe_b64encode(kdf.derive(password))

    l1 = Label(root, text='input your message').grid(row=2,column=0)

    E2 = Entry(root, show='')
    E2.grid(row=2, column=1)

    be20 = Button(root, text='Encrypt', command=encrypt_entry).grid(row=2, column=2)

    be21 = Button(root, text='Decrypt', activebackground='#003d4d', command=decrypt_entry).grid(row=2, column=3)


#GUI
root = Tk(screenName='CryptGUI',  baseName='CryptGUI',  className='CryptGUI')
root.resizable(width=False, height=False)
root.geometry('500x500')
canvas = Canvas(root, width = 500, height = 500, bg="#d7d7d7")
canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img1 = PhotoImage(file='C:/Users/guilo/Documents/Atom Projects/others/dist/canvas1.png')

my_image = canvas.create_image(0, 0, image=img1, anchor=NW)

l0 = Label(root, text='input your password').grid(row=1, column=0)

E1 = Entry(root, show='*')
E1.grid(row=1, column=1)

be = Button(root, text='OK', width= 5, command= password_get).grid(row=1, column=2)


root.mainloop()
