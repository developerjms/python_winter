from tkinter import*
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드이벤트", "눌린키" + chr(event.keycode))
    
window = Tk()
window.geometry("400x400")

label1 = Label(window,text="이곳 바뀜")
window.bind("<Key>", keyEvent)

label1.pack(expand=1, anchor=CENTER)
window.mainloop()