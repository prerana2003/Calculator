import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("480x590")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    lable_result.config(text=equation)

def clear():
    equation=""
    lable_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    lable_result.config(text=result)

lable_result= Label(root,width=21,height=2,text="",font=("arial",30))
lable_result.pack()

Button(root,text="C",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#ff0000",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("/")).place(x=130,y=100)
Button(root,text="%",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("%")).place(x=250,y=100)
Button(root,text="*",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("*")).place(x=370,y=100)

Button(root,text="8",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("8")).place(x=130,y=200)
Button(root,text="9",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("9")).place(x=250,y=200)
Button(root,text="-",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("-")).place(x=370,y=200)
Button(root,text="7",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("7")).place(x=10,y=200)

Button(root,text="4",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("5")).place(x=130,y=300)
Button(root,text="6",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("6")).place(x=250,y=300)
Button(root,text="+",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("+")).place(x=370,y=300)

Button(root,text="1",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("2")).place(x=130,y=400)
Button(root,text="3",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("3")).place(x=250,y=400)
Button(root,text="0",width=9,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2F4F4F",command=lambda: show(".")).place(x=250,y=500)
Button(root,text="=",width=4,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#20B2AA",command=lambda: calculate()).place(x=370,y=400)


root.mainloop()
