from tkinter import*
from tkinter import messagebox

w = Tk()
w.title("윈도우창 연습")
w.geometry("400x400")
w.resizable(width=FALSE, height=TRUE)

# b1 = Button(w, text="버튼1")
# b2 = Button(w, text="버튼2")
# b3 = Button(w, text="버튼3")

# b1.pack(side=LEFT)
# b2.pack(side=LEFT)
# b3.pack(side=LEFT)

btnList = [None] * 3

for i in range(0,3):
    btnList[i] = Button(w, text="버튼"+str(i+1))
    btnList[i].pack(side=LEFT, fill=X, ipadx = 10, ipady = 10)

w.mainloop()
