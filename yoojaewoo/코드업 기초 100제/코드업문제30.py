#8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
# 내 풀이)
hexa = hex(int(input()))
print(hexa[2:].upper())
# 강의 풀이)
hexadecimal = int(input())
hexConv = hex(hexadecimal)[2:]
print( hexConv.upper() )