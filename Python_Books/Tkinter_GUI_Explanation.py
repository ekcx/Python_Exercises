from tkinter import *

#
#
#
#
#

def Call():
    msg = Label(window, text="You pressed the button", background="gray")
    msg.place(x=250, y=455)
    button["bg"] = "blue"
    button["fg"] = "white"


window = Tk()
window.geometry("500x910")
button = Button(text="Press me", command=Call)
button.place(x=30, y=20, width=120, height=25)
window.mainloop()

