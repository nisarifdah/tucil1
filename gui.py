# GUI

from vigenere import *

from tkinter import *
from tkinter.filedialog import askopenfile

def compute():
    text = ent_text.get().upper()
    key = ent_key.get().upper()

    # Get mode
    mode = var1.get()
    
    # Get encryption type
    encType = var2.get()
    if(encType=='1'): # Standard Vigenere Cipher
        lbl_result_text['text'] = mainVigenere(mode,text,key)
    # elif(encType==2): # Full Vigenere Cipher
    # elif(encType==3): # Auto-key Vigenere Cipher
    # elif(encType==4): # Extended Vigenere Cipher
    # elif(encType==5): # Playfair Cipher
    

def openFile(): 
    file = askopenfile(mode ='rb') 
    if file is not None: 
        content = file.read() 
        print(content)


window = Tk()
window.title('Encrypt & Decrypt')

lbl_title = Label(text='Welcome to Enigma!')
lbl_title.pack()

frm_form = Frame(relief=RIDGE, borderwidth=3)
frm_form.pack()

lbl_text = Label(master=frm_form, text='Enter message:')
ent_text = Entry(master=frm_form, width=40)
lbl_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_text.grid(row=0, column=1, padx=5, pady=5)

lbl_key = Label(master=frm_form, text='Enter key:')
ent_key = Entry(master=frm_form, width=40)
lbl_key.grid(row=1, column=0, padx=5, pady=5, sticky='w')
ent_key.grid(row=1, column=1, padx=5, pady=5)

btn_open = Button(master=frm_form, text='Open file', width=10, command=openFile)
btn_open.grid(row=2, column=1, padx=5, pady=5, sticky='w')

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var1.set(0)
var2.set(0)
var3.set(0)


lbl_mode = Label(master=frm_form, text='Choose mode:')
lbl_mode.grid(row=3, column=0, padx=5, pady=5, sticky="w")
rad_mode = Radiobutton(master=frm_form,text='Encryption', variable = var1, value=1)
rad_mode.grid(row=3, column=1, padx=5, pady=5, sticky='w')
rad_mode = Radiobutton(master=frm_form,text='Decryption', variable = var1, value=2)
rad_mode.grid(row=4, column=1, padx=5, pady=5, sticky='w')

lbl_type = Label(master=frm_form, text='Choose type:')
lbl_type.grid(row=5, column=0, padx=5, pady=5, sticky="w")
rad_type = Radiobutton(master=frm_form,text='Vigenere Cipher', variable = var2, value=1)
rad_type.grid(row=5, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Full Vigenere Cipher', variable = var2, value=2)
rad_type.grid(row=6, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Auto-key Vigenere Cipher', variable = var2, value=3)
rad_type.grid(row=7, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Extended Vigenere Cipher', variable = var2, value=4)
rad_type.grid(row=8, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Playfair Cipher', variable = var2, value=5)
rad_type.grid(row=9, column=1, padx=5, pady=5, sticky='w')

lbl_type = Label(master=frm_form, text='Choose text option:')
lbl_type.grid(row=10, column=0, padx=5, pady=5, sticky="w")
rad_type = Radiobutton(master=frm_form,text='Without space', variable = var3, value=1)
rad_type.grid(row=10, column=1, padx=5, pady=5, sticky='w')
rad_type = Radiobutton(master=frm_form,text='Separated every 5 letters', variable = var3, value=2)
rad_type.grid(row=11, column=1, padx=5, pady=5, sticky='w')

btn_compute = Button(master=frm_form, text='Go!', width=10, command=compute)
btn_compute.grid(row=13, column=1, padx=5, pady=5, sticky='w')

lbl_result = Label(master=frm_form, text='Result:')
lbl_result_text = Label(master=frm_form, text='R')
lbl_result.grid(row=14, column=0, padx=5, pady=5, sticky="w")
lbl_result_text.grid(row=14, column=1, padx=5, pady=5, sticky="w")


# Keeps window alive 
window.mainloop()