# 33. 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.16진수(대문자)로 출력한다.

a = int(input()) # 10 입력
num = hex(a)[2:]
print(num.upper()) # A 출력