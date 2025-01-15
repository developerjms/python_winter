class FourCal:
    name='홍길동'#  클래스 변수: (이 클래스를 사용하는 모든 객채들이 사용((공유))함)해당 클래스로 부터 생성된 모든 객체에 동일한 값을 부여
    classCount=0#  공유 변수와 같음음
    def __init__(self,first=0,second=0):
        self.first = first
        self.second = second
        FourCal.classCount+=1
    
    # def __del__(self):#  소멸자
    #     FourCal.classCount-=1

    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        #  if(self.second==0):
        #      return 0
        result = self.first / self.second
        return result

if __name__=='__main__': #name은 현재 파일을 실행할때 main으로 인식 다른 파일에서 import할땐 main으로 인식 안함 // import하여 다른파일에서 실행할때 main이 아니므로 실행안됌
    no=input('숫자 두 개: ').strip().split()

    c1=FourCal(int(no[0]),int(no[1]))#생성자 이용
    print(c1.add())
    print(c1.mul())
    print(c1.sub())
    print(c1.div())

    no=input('숫자 두 개: ').strip().split()
    c2=FourCal()
    c2.setdata(int(no[0]),int(no[1]))#매서드 이용
    print(c2.add())

    no=input('숫자 두 개: ').strip().split()#맴버 변수를 이용하여 직접 값을 넘겨줌
    c3=FourCal()
    c3.first=int(no[0]) #좋은 방법이 아님
    c3.second=int(no[1])
    addres=c3.add()
    print(addres)
    FourCal.classCount=1000 #클래스 카운트를 1000으로 바꿨음음

    #c1, c2, c3 각각의 first, second 값은 각각 다름

    print(c1.first,c2.first,c3.first)
    print(c1.name,c2.name,c3.name) #3개의 객체가 다름에도 동일한 값이 부여됨
    print(c1.classCount) #3개의 객체가 열렸으므로 카운트도 3번 나옴, c3에서 1000으로 바꿨으므로 c1을 출력했지만 c3인 1000이 나옴
    # del.c3 #해당 객체를 삭제. 더이상 해당 객체를 사용하지 않겠다는 의미
    print(c1.classCount)