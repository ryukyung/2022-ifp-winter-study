'''
입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
'''
Bitnot = ~int(input())
print( Bitnot )


'''
입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
'''
x, y = map(int, input().split())
print( x&y )


'''
1개의 정수형 입력이 들어오면 비트 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
'''
x = int(input())
print( ['짝수', '홀수'][x & 1] )


'''
입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
'''
x, y = map(int, input().split())
print( x|y )


'''
입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
'''
x, y = map(int, input().split())
print( x^y )
