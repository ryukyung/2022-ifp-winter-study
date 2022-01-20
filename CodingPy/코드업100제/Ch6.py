# [47]

# 정수 1개를 입력받아 2배 곱해 출력해보자.

# Tip::

# 곱하기 2를 해도 되지만 이진수를 왼쪽으로 한 번씩 이동시켜주면 기존 값의 두 배가 된다.
# ex) 5(101) => 10(1010), 7(111) => 14(1110)


#답안 1
inputInt = int(input())
print( inputInt * 2 )

#답안 2
inputInt = int(input())
print( inputInt << 1 )
#비트시프트 1번, 왼쪽으로 하면 두배



# [48]

# 정수 2개(a, b)를 입력받아 a를 2(b 제곱)배 곱한 값으로 출력해보자. ( a * 2(b 제곱) )


a, b = map(int, input().split())
print( a << b )
