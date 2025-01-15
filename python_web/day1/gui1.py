from tkinter import*
from tkinter import messagebox

import mysql.connector

def myFunc() :
    messagebox.showinfo("애옹이 버튼", "애옹이는 귀여워")

def myFunc_chk() :
    if chk.get() == 0:
        messagebox.showinfo("","체크 꺼짐")
    else :
        messagebox.showinfo("", "체크켜짐")

def myFunc_radio():
    if var.get() == 1:
        lb2.configure(text = "파이썬")
    elif var.get() == 2:
        lb2.configure(text = "c++")
    elif var.get() == 3:
        lb2.configure(text = "java")
        
        
w = Tk()
w.title("윈도우창 연습")
w.geometry("400x400")
w.resizable(width=FALSE, height=TRUE)

# lb1 = Label(w,text = "a")
# lb2 = Label(w,text = "b", font=("궁서체",30),fg="blue")
# lb3 = Label(w,text = "c",bg="magenta",width=20,height=5, anchor=SE)\
    
# lb1.pack()
# lb2.pack()
# lb3.pack()

photo = PhotoImage(file="C:\\Users\\USER\\Desktop\\python\\python\\python_web\\day1\\cat2.gif")

label1 = Label(w, image=photo)
label1.pack()

b1 = Button(w, text="종료", fg="red", command= myFunc, width=10, height=10)
# b1.pack()

chk = IntVar()
cb1 = Checkbutton(w, text="클릭하세요.", variable=chk, command=myFunc_chk)
cb1.pack()

var = IntVar()
rb1 = Radiobutton(w, text="파이썬", variable=var, value=1, command=myFunc_radio)
rb2 = Radiobutton(w, text="c++", variable=var, value=2, command=myFunc_radio)
rb3 = Radiobutton(w, text="java", variable=var, value=3, command=myFunc_radio)

lb2 = Label(w, text="선택한 언어는 :", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
lb2.pack()

w.mainloop()
