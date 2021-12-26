import math as m
from tkinter import*
root=Tk()
root.title("SCIENTIFIC CALCULATOR")
root.config(bg='#272533')
e=Entry(root,width=32,borderwidth=10,bg="white",fg="black",font=('Segoe UI',20))
e.grid(row=0,column=0,columnspan=5,padx=30,pady=20,ipady=12)
def click(number):
    c=e.get()
    e.delete(0,END)
    e.insert(0,str(c)+str(number))
def clear():
    e.delete(0,END)
def add():
    num1=e.get()
    global f_num
    global math
    math="add"
    f_num=float(num1)
    e.delete(0,END)
def sub():
     num1=e.get()
     global f_num
     global math
     math="sub"
     f_num=float(num1)
     e.delete(0,END)
def mul():
     num1=e.get()
     global f_num
     global math
     math="mul"
     f_num=float(num1)
     e.delete(0,END)
def div():
     num1=e.get()
     global f_num
     global math
     math="div"
     f_num=float(num1)
     e.delete(0,END)
def per():
    num1=e.get()
    global f_num
    global math
    math="per"
    f_num=float(num1)
    e.delete(0,END)
def sin():
    import math as m
    num1=e.get()
    global f_num
    global math
    math="sin"
    f_num=float(num1)
def cos():
    import math as m
    num1=e.get()
    global f_num
    global math
    math="cos"
    f_num=float(num1)
def tan():
    import math as m
    num1=e.get()
    global f_num
    global math
    math="tan"
    f_num=float(num1)
def log():
    import math as m
    num1=e.get()
    global f_num
    global math
    math="log"
    f_num=float(num1)
def pow():
    num1=e.get()
    global f_num
    global math
    math="pow"
    f_num=float(num1)
    e.delete(0,END)
def sq():
    num1=e.get()
    global f_num
    global math
    math="sq"
    f_num=float(num1)
    e.delete(0,END)
def ln():
    num1=e.get()
    global f_num
    global math
    math="ln"
    f_num=float(num1)
    e.delete(0,END)
def equal():
    num2=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num+float(num2))
    elif math=="sub":
         e.insert(0,f_num-float(num2))
    elif math=="mul":
         e.insert(0,f_num*float(num2))
    elif math=="div":
         e.insert(0,f_num/float(num2))
    elif math=="log":
        e.insert(0,m.log10(f_num))
    elif math=="dot":
        e.insert(0,".")
    elif math=="per":
        e.insert(0,f_num/float(num2)*100)
    elif math=="sin":
        e.insert(0,m.sin(f_num))
    elif math=="cos":
        e.insert(0,m.cos(f_num))
    elif math=="tan":
        e.insert(0,m.tan(f_num))
    elif math=="pow":
        e.insert(0,m.pow(f_num,float(num2)))
    elif math=="sq":
        e.insert(0,f_num**2)
    elif math=="ln":
        e.insert(0,m.log(f_num))
button1=Button(root,text="1",padx=44,pady=20,command=lambda:click(1),bg="green",fg="white",font=('Segoe UI',20))

button2=Button(root,text="2",padx=40,pady=20,command=lambda:click(2),bg="green",fg="white",font=('Segoe UI',20))

button3=Button(root,text="3",padx=36,pady=20,command=lambda:click(3),bg="green",fg="white",font=('Segoe UI',20))

button4=Button(root,text="4",padx=44,pady=20,command=lambda:click(4),bg="green",fg="white",font=('Segoe UI',20))

button5=Button(root,text="5",padx=40,pady=20,command=lambda:click(5),bg="green",fg="white",font=('Segoe UI',20))

button6=Button(root,text="6",padx=36,pady=20,command=lambda:click(6),bg="green",fg="white",font=('Segoe UI',20))

button7=Button(root,text="7",padx=44,pady=20,command=lambda:click(7),bg="green",fg="white",font=('Segoe UI',20))

button8=Button(root,text="8",padx=40,pady=20,command=lambda:click(8),bg="green",fg="white",font=('Segoe UI',20))

button9=Button(root,text="9",padx=36,pady=20,command=lambda:click(9),bg="green",fg="white",font=('Segoe UI',20))

button0=Button(root,text="0",padx=40,pady=20,command=lambda:click(0),bg="green",fg="white",font=('Segoe UI',20))

button_add=Button(root,text="+",padx=34,pady=20,command=add,bg="red",fg="black",font=('Segoe UI',20))

button_sub=Button(root,text="-",padx=38,pady=20,command=sub,bg="red",fg="black",font=('Segoe UI',20))

button_mul=Button(root,text="x",padx=37,pady=20,command=mul,bg="red",fg="black",font=('Segoe UI',20))

button_div=Button(root,text="/",padx=38,pady=20,command=div,bg="red",fg="black",font=('Segoe UI',20))

button_clear1=Button(root,text="C",padx=44,pady=20,command=clear,bg="red",fg="black",font=('Segoe UI',20))

button_equal=Button(root,text="=",padx=98,pady=20,command=equal,bg="#FFFF66",fg="black",font=('Segoe UI',20))




button_per=Button(root,text="%",padx=40,pady=20,command=per,bg="red",fg="black",font=('Segoe UI',20))

button_sin=Button(root,text="sin",padx=34,pady=20,command=sin,bg="red",fg="black",font=('Segoe UI',20))

button_cos=Button(root,text="cos",padx=28,pady=20,command=cos,bg="red",fg="black",font=('Segoe UI',20))

button_tan=Button(root,text="tan",padx=24,pady=20,command=tan,bg="red",fg="black",font=('Segoe UI',20))

button_log=Button(root,text="log",padx=24,pady=20,command=log,bg="red",fg="black",font=('Segoe UI',20))





button_pow=Button(root,text="X^n",padx=28,pady=20,command=pow,bg="red",fg="black",font=('Segoe UI',20))

button_sq=Button(root,text="X^2",padx=28,pady=20,command=sq,bg="red",fg="black",font=('Segoe UI',20))

button_ln=Button(root,text="ln",padx=42,pady=20,command=ln,bg="red",fg="black",font=('Segoe UI',20))




button_pow.grid(row=2,column=4)

button_sq.grid(row=3,column=4)

button_ln.grid(row=4,column=4)




button7.grid(row=2,column=0)

button8.grid(row=2,column=1)

button9.grid(row=2,column=2)

button_clear1.grid(row=1,column=4)




button4.grid(row=3,column=0)

button5.grid(row=3,column=1)

button6.grid(row=3,column=2)

button_sub.grid(row=3,column=3)



button1.grid(row=4,column=0)

button2.grid(row=4,column=1)

button3.grid(row=4,column=2)

button_add.grid(row=2,column=3)


button0.grid(row=5,column=1)



button_equal.grid(row=5,column=3,columnspan=3)

button_mul.grid(row=4,column=3)

button_div.grid(row=5,column=2)

button_per.grid(row=5,column=0)



button_sin.grid(row=1,column=0)

button_cos.grid(row=1,column=1)

button_tan.grid(row=1,column=2)

button_log.grid(row=1,column=3)



root.mainloop()