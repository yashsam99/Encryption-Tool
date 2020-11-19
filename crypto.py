import tkinter as tk
from tkinter.filedialog import askopenfilename

def encryptt():
    f=askopenfilename(filetypes=[('Text',['*.TXT'])])
    file = open(f,"r")
    msg = file.read()
    file = open("key.txt","r")
    key = file.read()
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    encrypted=''.join(encryped)
    outfile= open("encryptedmsg.txt","w")
    outfile.write(encrypted)
    outfile.close()

def decryptt():
    f=askopenfilename(filetypes=[('Text',['*.TXT'])])
    file = open(f,"r")
    encryped=file.read()
    file = open("key.txt","r")
    key = file.read()
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    decrypted=''.join(msg)
    outfile= open("decryptedmsg.txt","w")
    outfile.write(decrypted)
    outfile.close()
