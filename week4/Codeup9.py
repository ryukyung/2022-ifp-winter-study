#59
#입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
#비트단위(bitwise)연산자 ' ~ ' 를 붙이면 된다.
a = ~int(input())
print(a)

#60
#입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
#비트단위(bitwise)연산자 &를 사용하면 된다.
a, b = map(int, input().split())
print(a&b)

#61
#입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
#비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
a, b = map(int, input().split())
print(a|b)

#62
#입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
#비트단위(bitwise) 연산자 ^(xor, circumflex/caret, 서컴플렉스/카릿)를 사용하면 된다.
a, b = map(int, input().split())
print(a^b)