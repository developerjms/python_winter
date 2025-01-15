from tkinter import*
from PIL import Image, ImageTk

btnList = [None] * 9
fnameList = ["cat1.gif", "cat2.gif", "cat3.gif", "cat4.gif", "cat5.gif", 
             "cat6.gif", "cat7.gif", "cat8.gif", "cat9.gif"]

photoList = [None] * 9
num = 0

def clickNext() :
    global num
    num += 1
    if num > 8:
        num = 0
    image = Image.open("C:\\Users\\USER\\Desktop\\python\\python\\python_web\\day1\\"+fnameList[num])
    resize_image = image.resize((700,700))
    photoList[num] = ImageTk.PhotoImage(resize_image)
    pLable.configure(image = photoList[num])
    pLable.image = image = photoList[num]
    
def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    image = Image.open("C:\\Users\\USER\\Desktop\\python\\python\\python_web\\day1\\"+fnameList[num])
    resize_image = image.resize((700,700))
    photoList[num] = ImageTk.PhotoImage(resize_image)
    pLable.configure(image = photoList[num])
    pLable.image = image = photoList[num]
    
window = Tk()
window.geometry("900x900")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="이전", command=clickPrev)
btnNext = Button(window, text="다음", command=clickNext)

image = Image.open("C:\\Users\\USER\\Desktop\\python\\python\\python_web\\day1\\"+fnameList[0])
resize_image = image.resize((700,700))
photoList[0] = ImageTk.PhotoImage(resize_image)
pLable = Label(window, image = photoList[0])

btnPrev.place( x = 250, y = 10)
btnNext.place( x = 400, y = 10)
pLable.place( x = 15, y = 50)

window.mainloop()