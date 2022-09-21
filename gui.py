from tkinter import *

window = Tk()

window.title('My app')

entry_text = Entry(window, width=30)
entry_text.pack()
entry_text.focus_set()

def click_button():
	print(entry_text.get())

btn = Button(window, text='Click here', width=20, command=click_button)
btn.pack()

window.geometry('300x150')

window.mainloop()