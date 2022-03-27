# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# 내 풀이)
hexa = hex(int(input()))
print(hexa[2:])
# 강의 풀이)
hexadecimal = int(input())
print( hex(hexadecimal)[2:] )