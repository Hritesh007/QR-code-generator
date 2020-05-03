from tkinter import *
import pyqrcode
window = Tk()

window.title("QR Creator")

window.geometry('350x200')
lb  = Label(window, text="Enter URL/Message :-")
lb.grid(column=0 , row=0)
lbl = Label(window, text="")

lbl.grid(column=0, row=3)

txt = Entry(window,width=55)

txt.grid(column=0, row=1)

def clicked():
    res = ""+txt.get()
    url=pyqrcode.create(res)
    url.svg('qr.svg',scale=8)
    res="QR code created successfully for :-"+res
    lbl.configure(text=res)

btn = Button(window, text="Create", command=clicked)

btn.grid(column=0, row=2)

window.mainloop()
