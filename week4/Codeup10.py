#63
#입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
#단, 조건문을 사용하지 않고 3항 연산자 'and or' 를 사용한다.
a, b = map(int, input().split())
print( a>b and a or b)

#64
#입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
#(단, 삼항 연산자 이용)
a, b, c = map(int, input().split())
num = a<b and a or b
print(num<c and num or c)  #최솟값을 c와 비교하여 출력