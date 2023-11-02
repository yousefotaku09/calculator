from tkinter import *
from tkinter import ttk


app=Tk()
app.title("calculatore")
app.geometry('500x380')

text_box=Text(app,width=70,height=10)
text_box.pack()



text_box2=Text(app,width=30,height=13)
text_box2.place(x=240,y=165)





def button1():
    num1 = 1
    text_box.insert(END, str(num1))



button1=Button(text="1",width=6,height=2,command=button1)
button1.place(x=2,y=165)

def button2():
    num2 = 2
    text_box.insert(END, str(num2))



button2=Button(text="2",width=6,height=2,command=button2)
button2.place(x=2,y=207)

def button3():
    num3 = 3
    text_box.insert(END, str(num3))



button3=Button(text="3",width=6,height=2,command=button3)
button3.place(x=2,y=249)


def button4():
    num4 = 4
    text_box.insert(END, str(num4))



button4=Button(text="4",width=6,height=2,command=button4)
button4.place(x=2,y=292)

def button5():
    num5 = 5
    text_box.insert(END, str(num5))



button5=Button(text="5",width=6,height=2,command=button5)
button5.place(x=2,y=335)

def button6():
    num6 = 6
    text_box.insert(END, str(num6))



button6=Button(text="6",width=6,height=2,command=button6)
button6.place(x=58,y=165)


def button7():
    num7 = 7
    text_box.insert(END, str(num7))



button7=Button(text="7",width=6,height=2,command=button7)
button7.place(x=58,y=207)


def button8():
    num8 = 8
    text_box.insert(END, str(num8))



button8=Button(text="8",width=6,height=2,command=button8)
button8.place(x=58,y=249)


def button9():
    num9 = 9
    text_box.insert(END, str(num9))



button9=Button(text="9",width=6,height=2,command=button9)
button9.place(x=58,y=292)

def button0():
    num0 = 0
    text_box.insert(END, str(num0))



button0=Button(text="0",width=6,height=2,command=button0)
button0.place(x=58,y=335)

def button_p():
    num_p = "+"
    text_box.insert(END, str(num_p))



button_p=Button(text="+",width=6,height=2,command=button_p)
button_p.place(x=117,y=165)



def button_m():
    num_m = "-"
    text_box.insert(END, str(num_m))



button_m=Button(text="-",width=6,height=2,command=button_m)
button_m.place(x=117,y=207)


def button_d():
    num_d = "/"
    text_box.insert(END, str(num_d))



button_d=Button(text="/",width=6,height=2,command=button_d)
button_d.place(x=117,y=249)

def button_t():
    num_t = "*"
    text_box.insert(END, str(num_t))



button_t=Button(text="*",width=6,height=2,command=button_t)
button_t.place(x=117,y=292)

def button_e():
    text_box2.delete("1.0", END)  # حذف المحتوى الحالي في مربع النص الثاني
    expression = text_box.get("1.0", END).strip()

    try:
        result = eval(expression)
        text_box2.insert(END, result)
    except:
        text_box2.insert(END, "Write the right math question")
    


button_e=Button(text="equal",width=6,height=2,command=button_e)
button_e.place(x=117,y=335)





def button_clear():
    text_box.delete("1.0", END)
    text_box2.delete("1.0", END)


button_clear = Button(text="clear(all)", width=6, height=2, command=button_clear)
button_clear.place(x=175, y=335)



def button_delete():
    current_text = text_box.get("1.0", END)
    updated_text = current_text[:-2]  # حذف الحرف الأخير والمسافة السابقة
    text_box.delete("1.0", END)
    text_box.insert(END, updated_text)


button_delete = Button(text="clear(one)", width=7, height=2, command=button_delete)
button_delete.place(x=175, y=292)


app.mainloop()