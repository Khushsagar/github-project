from tkinter import *

root = Tk()

root.title("Simple Calculator By Khush Sagar")
root.geometry("520x600+400+100")
root.resizable(False,False)
root.config(bg="black")



equation = ""

def clear():
    global equation
    equation=""
    label.config(text=equation)

def show(v):
    global equation
    equation+=v
    label.config(text=equation)

def backspace():
    global equation
    equation = equation[:-1]
    

def calculate():
    global equation
    result = ''
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
        label.config(text=result)



label = Label(root,width=100,height=2,bg="ghost white",text="",font="arial 20 bold")
label.pack()


Button(root,text="AC",width=4,height=1,bg="#fff",fg="#3697f5",font='arial 30 bold',command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("/")).place(x=130,y=100)
Button(root,text="←",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:backspace()).place(x=250,y=100)
Button(root,text="%",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("%")).place(x=380,y=100)


Button(root,text="7",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("8")).place(x=130,y=200)
Button(root,text="9",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("9")).place(x=250,y=200)
Button(root,text="*",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("*")).place(x=380,y=200)

Button(root,text="4",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("5")).place(x=130,y=300)
Button(root,text="6",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("6")).place(x=250,y=300)
Button(root,text="-",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("-")).place(x=380,y=300)

Button(root,text="1",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("2")).place(x=130,y=400)
Button(root,text="3",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("3")).place(x=250,y=400)
Button(root,text="+",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("+")).place(x=380,y=400)

Button(root,text="00",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("00")).place(x=10,y=500)
Button(root,text="0",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show("0")).place(x=130,y=500)
Button(root,text=".",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:show(".")).place(x=250,y=500)
Button(root,text="=",width=4,height=1,bg="#fff",fg="#2a2d36",font='arial 30 bold',command=lambda:calculate()).place(x=380,y=500)

root.mainloop()
