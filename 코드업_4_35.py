'''
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
'''
hexadecimal = '0x' + input()
integer = int(hexadecimal, 16)
print( oct(integer)[2:] )
