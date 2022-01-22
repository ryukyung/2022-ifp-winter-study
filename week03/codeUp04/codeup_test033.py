# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# 16진수(대문자)로 출력한다.

#num = int(input())
#numToString = hex(num)[2:]
# print(numToString.upper())

num = int(input())
print(format(num, 'X'))
