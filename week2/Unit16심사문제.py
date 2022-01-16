#Unit16
#정수를 입력받아
#입력된 정수의 구구단을 출력하는 프로그램 작성
n = int(input())
for i in range(1, 10):
    print(n, '*', i , '=', n * i)