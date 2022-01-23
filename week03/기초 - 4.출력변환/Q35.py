# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.

# Tip
# 16진수 >> 10진수 >> 8진수 순서대로 변환

hexadecimal = '0x' + input()
integer = int(hexadecimal, 16)
print( oct(integer)[2:] )
