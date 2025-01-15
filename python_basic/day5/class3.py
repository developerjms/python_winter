import class2
# from day3 import snale module
# from day3 import snale module import *

class MoreFourCal(class2.FourCal):
    pass
    def pow(self):
        return self.first**self.second

    def div(self):#  부모의 메서드를 재정의
        if(self.second==0):
            return 0
        result = self.first / self.second
        return result

a=MoreFourCal()
a.setdata(10,50)
print(a.add())
print(a.pow())
a.second=0
print(a.div())