class Calculator:
    def __init__(self): #생성자
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    

cal1 = Calculator() # 객체생성, 인스턴스화
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.add(4))
print(cal2.add(3))

