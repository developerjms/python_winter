from tkinter import*
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼 클릭")
    
window = Tk()
window.bind("<Double-Button-1>", clickLeft)
window.mainloop()