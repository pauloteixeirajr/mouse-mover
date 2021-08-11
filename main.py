import mouse
import random

from datetime import datetime
from tkinter import *

milliseconds = 30000
is_active = True

window = Tk(screenName="Keep Screen Active")
window.title("Keep Screen Active")
window.geometry("680x500")


def toggle_clicking():
    global is_active
    global window
    global label
    is_active = not is_active
    label.config(text=f"App is active: {is_active}")


def keep_clicking():
    global is_active
    global window
    global listbox

    if is_active:
        y_axis = random.randint(1, 500)
        mouse.move("500", f"{y_axis}", duration=1)
        mouse.click()
        listbox.insert(0, f'Last run: {datetime.now()}')
    window.after(milliseconds, keep_clicking)


button = Button(text="Toggle Application", command=toggle_clicking, width=30)
button.config(anchor=CENTER)
button.pack()

label = Label(text=f"App is active: {is_active}", font=('Arial', 18))
label.config(anchor=CENTER)
label.pack()

frame = Frame(window, width=100, height=100)
frame.pack()

listbox = Listbox(frame, width=100, height=20)
listbox.pack(side=RIGHT, fill=Y)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)

window.after(milliseconds, keep_clicking)
window.mainloop()
