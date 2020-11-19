from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename
import start
import crypto

def forimagedialog():
    global result
    result.destroy()
    
    global imagename
    imagename=askopenfilename(filetypes=[('Image',['*.JPG','*.BMP','*.PNG'])])
    global imgtxt
    imgtxt.destroy()
    imgtxt=tk.Text(Encryptpanel,height=1,width=500)
    imgtxt.insert(tk.INSERT,'Image:  '+imagename)
    imgtxt.configure(state=tk.DISABLED)
    imgtxt.place(x=0,y=150)
    check()

def fortextdialog():  
    global result
    result.destroy()
    
    global filename
    filename=askopenfilename(filetypes=[('Text File',['*.txt'])])
    global filetxt
    filetxt.destroy()
    filetxt=tk.Text(Encryptpanel,height=1,width=500)
    filetxt.insert(tk.INSERT,'TextFile:  '+filename)
    filetxt.configure(state=tk.DISABLED)
    filetxt.place(x=0,y=120)
    check()

def decryptimage():
    global result
    result.destroy()
    
    global decimage
    decimage=askopenfilename(filetypes=[("Image File",["*.jpg","*.bmp","*.png"])])
    global decryptbut
    decryptbut.destroy()
    global decimgtxt
    decimgtxt.destroy()
    decimgtxt=tk.Text(Encryptpanel,height=1,width=500)
    decimgtxt.insert(tk.INSERT,'Decrypt Image : '+decimage)
    decimgtxt.configure(state=tk.DISABLED)
    decimgtxt.place(x=0,y=70)
    
    if(decimage!=''):
        decryptbut=tk.Button(Encryptpanel,text="Decrypt",font=("Trebuchet MS bold",12),fg='white',command=startdecryption)
        decryptbut.configure(background='#1E88E5')
        decryptbut.place(x=320,y=110)
        

def check():
    global result
    result.destroy()
    global Next
    Next.destroy()
    if(filename!='' and imagename!=''):
        Next=tk.Button(Encryptpanel,text="Encrypt",font=("Trebuchet MS bold",12),fg='white',command=startencryption)
        Next.configure(background='#1E88E5')
        Next.place(x=320,y=190)

def startencryption():
    global filename
    global imagename
    global result
    
    result.destroy()
    t=start.startencryption(imagename,filename)
    result=tk.Label(Encryptpanel,text=t)
    result.place(x=275,y=180)
    

def startdecryption():
    global decimage
    global result
    
    result.destroy()
    t=start.startdecryption(decimage)
    result=tk.Label(Encryptpanel,text=t)
    result.place(x=275,y=180)

def encrypttab():
    getimage.destroy()
    decimgtxt.destroy()
    decryptbut.destroy()
    result.destroy()
    selecttextfile2.destroy()
    selecttextfile3.destroy()
    
    global selectimage
    selectimage=tk.Button(Encryptpanel,text="Select Image",font=("Trebuchet MS bold",12),fg='white',command=forimagedialog)
    selectimage.configure(background='#1E88E5')
    selectimage.place(x=350,y=20)
    
    global selecttextfile
    selecttextfile=tk.Button(Encryptpanel,text="Select File",font=("Trebuchet MS bold",12),fg='white',command=fortextdialog)
    selecttextfile.configure(background='#1E88E5')
    selecttextfile.place(x=350,y=80)

def decrypttab():
    selectimage.destroy()
    global filename
    filename=''
    global imagename
    imagename=''
    selecttextfile.destroy()
    selecttextfile2.destroy()
    selecttextfile3.destroy()
    imgtxt.destroy()
    filetxt.destroy()
    Next.destroy()
    result.destroy()
    
    global getimage
    getimage=tk.Button(Encryptpanel,text="Select Image",font=("Trebuchet MS bold",12),fg='white',command=decryptimage)
    getimage.configure(background='#1E88E5')
    getimage.place(x=510,y=20)

def encryptt():
    selectimage.destroy()
    imgtxt.destroy()
    filetxt.destroy()
    Next.destroy()
    result.destroy()
    selecttextfile.destroy()
    selecttextfile3.destroy()
    global selecttextfile2
    selecttextfile2=tk.Button(Encryptpanel,text="Select File",font=("Trebuchet MS bold",12),fg='white',command=crypto.encryptt)
    selecttextfile2.configure(background='#1E88E5')
    selecttextfile2.place(x=50,y=20)

def decryptt():
    selectimage.destroy()
    imgtxt.destroy()
    filetxt.destroy()
    Next.destroy()
    result.destroy()
    selecttextfile.destroy()
    selecttextfile2.destroy()
    global selecttextfile3
    selecttextfile3=tk.Button(Encryptpanel,text="Select File",font=("Trebuchet MS bold",12),fg='white',command=crypto.decryptt)
    selecttextfile3.configure(background='#1E88E5')
    selecttextfile3.place(x=200,y=20)
    
filename=''
imagename=''
decimage=''

window=tk.Tk()
window.geometry('700x500')
window.title("Pro-tech-t")
window.configure(background='#ffffff')
                 
Subject=tk.Label(window,text="Select for\nStegnogrpahy/Cryptography:",font=("Trebuchet MS",20),fg="#1e88e5")
Subject.place(x=200,y=60)
Subject.configure(background='white')

encryptt=tk.Button(window,text="Encrypt Text",font=("Trebuchet MS bold",12),command=encryptt)
encryptt.configure(background='white')
encryptt.place(x=50,y=150)

decryptt=tk.Button(window,text="Decrypt Text",font=("Trebuchet MS bold",12),command=decryptt)
decryptt.configure(background='white')
decryptt.place(x=200,y=150)

encrypt=tk.Button(window,text="Encrypt Image",font=("Trebuchet MS bold",12),command=encrypttab)
encrypt.configure(background='white')
encrypt.place(x=350,y=150)

decrypt=tk.Button(window,text="Decrypt Image",font=("Trebuchet MS bold",12),command=decrypttab)
decrypt.configure(background='white')
decrypt.place(x=510,y=150)

Encryptpanel=tk.PanedWindow(width=700,height=500,background='white')

selectimage=tk.Button()
selecttextfile=tk.Button()
selecttextfile2=tk.Button()
selecttextfile3=tk.Button()
getimage=tk.Button()
filetxt=tk.Text()
imgtxt=tk.Text()
decimgtxt=tk.Text()
Next=tk.Button()
decryptbut=tk.Button()
result=tk.Label()

Encryptpanel.place(x=0,y=190)

window.mainloop()
