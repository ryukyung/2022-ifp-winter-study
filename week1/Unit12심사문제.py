#Unit12
#입력받은 문자열과 숫자(실수)
#첫번째 줄은 키, 두번째 줄은 값으로 하여 딕셔너리를 생성한 뒤
#딕셔너리를 출력하는 프로그램 작성
a = input().split()
b = map(float, input().split())
c = dict(zip(a,b))
print(c)
