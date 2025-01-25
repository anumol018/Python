from tkinter import*
root=Tk()
root.title("Calculator")
root.geometry('400x300')

def add():
    t.delete(0,END)
    a=int(e1.get())
    b=int(e2.get())
    r=a+b
    print("result=",r)
    t.insert(0,r)

def sub():
    t.delete(0,END)
    a=int(e1.get())
    b=int(e2.get())
    r=a-b
    print("result=",r)
    t.insert(0,r)

def multi():
    t.delete(0,END)
    a=int(e1.get())
    b=int(e2.get())
    r=a*b
    print("result=",r)
    t.insert(0,r)
    
def div():
    t.delete(0,END)
    a=int(e1.get())
    b=int(e2.get())
    r=a/b
    print("result=",r)
    t.insert(0,r)

def clear():
    t.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)

l1=Label(root,text="Initial value:")
l1.place(x=50,y=50)
l2=Label(root,text="Final value:")
l2.place(x=50,y=100)
l3=Label(root,text="Result")
l3.place(x=50,y=150)

e1=Entry(root)
e1.place(x=200,y=50)
e2=Entry(root)
e2.place(x=200,y=100)

t=Entry(root)
t.place(x=200,y=150)


b3=Button(root,text="Add",command=add)
b3.place(x=50,y=200)

b3=Button(root,text="Sub",command=sub)
b3.place(x=100,y=200)

b3=Button(root,text="Multi",command=multi)
b3.place(x=150,y=200)

b3=Button(root,text="Div",command=div)
b3.place(x=200,y=200)

b3=Button(root,text="Clear",command=clear)
b3.place(x=250,y=200)

root.mainloop()
