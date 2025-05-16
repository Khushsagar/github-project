from tkinter import *
from tkinter import colorchooser

def choos_color():
    color_code = colorchooser.askcolor(title = "Color chooser")
    label =Label(root,text=f"color code : {color_code}",fg="red")
    label.pack() 

root = Tk()
button = Button(root,text="Select Color",command=choos_color)

button.pack()

root.geometry("300x300")

root.mainloop()


