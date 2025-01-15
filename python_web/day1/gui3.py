from tkinter import *
from PIL import Image, ImageTk

# 메인 윈도우 생성
w = Tk()
w.title("윈도우창 연습")
w.geometry("1100x1100")  # 창 크기 조정
w.resizable(width=False, height=True)

# 버튼과 이미지 리스트 초기화
btnList = [None] * 9
photoList = [None] * 9
num = 0

# 이미지 불러오기 및 리사이징
for j in range(1, 10):
    try:
        image = Image.open(f"C:\\Users\\USER\\Desktop\\python\\python\\python_web\\day1\\cat{j}.gif")
        resize_image = image.resize((300, 300))  # 이미지 크기 변경
        photoList[num] = ImageTk.PhotoImage(resize_image)  # tkinter용 이미지 객체로 변환
        btnList[num] = Button(w, image=photoList[num])  # 버튼 생성
        num += 1
    except FileNotFoundError:
        print(f"이미지 'cat{j}.gif'을(를) 지정된 경로에서 찾을 수 없습니다.")

# 버튼을 그리드 형식으로 배치 (3x3)
xPos, yPos = 50, 50
for i in range(3):
    for k in range(3):
        btnList[i * 3 + k].place(x=xPos, y=yPos)  # 각 버튼을 (xPos, yPos) 위치에 배치
        xPos += 350  # 버튼 사이 간격을 350으로 설정
    xPos = 50  # 각 행이 끝날 때마다 xPos 초기화
    yPos += 350  # 각 열이 끝날 때마다 yPos 증가

# 메인 루프 실행
w.mainloop()