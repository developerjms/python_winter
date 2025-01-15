# input함수로 입력된 데이터를 a.txt파일 뒤에 추가 내용 집어넣기
f = open('a.txt', 'a', encoding='utf-8')
f.write('\n')
while True:
    data = input('이름과 점수 3개 입력(q입력시 종료) : ')
    if data[0] == 'q' :
        break
    f.write(data+'\n') 
f.close()