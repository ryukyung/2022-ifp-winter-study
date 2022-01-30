'''
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. (단, 삼항 연산자 이용)
'''

a, b, c = map(int, input().split())
small = a if a<b else b
small = small if small<c else c
print(small)