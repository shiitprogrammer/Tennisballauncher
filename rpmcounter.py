from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="hello")

lbl.grid(column=0, row=0)
def Close():
    window.destroy()

btn = Button(window, text="Exit", command=Close)

btn.grid(column=1, row=0)

window.mainloop()


