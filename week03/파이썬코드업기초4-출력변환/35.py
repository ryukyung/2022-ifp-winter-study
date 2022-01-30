# 35. 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.

hexa = '0x' + input()
a = int(hexa, 16)
print(oct(a)[2:])