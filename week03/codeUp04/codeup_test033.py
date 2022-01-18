# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# 16진수(대문자)로 출력한다.
num = int(input())
numToString = str(hex(num)[2:])
print(numToString.upper())
