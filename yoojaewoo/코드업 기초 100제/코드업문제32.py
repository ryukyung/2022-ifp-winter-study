# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
# 내 풀이)
pal = '0x' + input()
print(int(pal, 16))
# 강의 풀이)
hexadecimal = '0x' + input()
integer = int(hexadecimal, 16)
print( oct(integer)[2:] )