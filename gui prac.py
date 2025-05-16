from tkinter import *
from tkinter.filedialog import *

win = Tk()
                                        

win.title("Khush")

win.geometry("500x500")
l1 = Label(win,font = ("arial 10 italic"),fg='red')
l1.place(x=50,y=50)




def NewFile():
    f = open('New File.txt',"x")
    a = input("do you want to write something or not[for yes type (y) for no type(n)]: ")
    if a=="y":
        x = input("Type here:")
        f.write(x)
        f.close()
    elif a=="n":
        print("okay no problem !")
    else:
        print("sorry we can't help you")

def OpenFile():
    name = askopenfile()
    if name is not None:
        con = name.read()
        l1.config(text=con)
    
def About():
    l1.config(text="Sorry! we don't have any information right now ")
    #print("Sorry! we don't have any information right now ")
m = Menu(win)

win.config(menu=m)

filemenu = Menu(m)
helpmenu = Menu(m)

m.add_cascade(label="File",menu=filemenu)
m.add_cascade(label="Help",menu=helpmenu)

filemenu.add_command(label="New File",command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Open File",command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

helpmenu.add_command(label="About",command=About)
helpmenu.add_separator()
helpmenu.add_command(label="Exit",command=quit)

win.mainloop()
