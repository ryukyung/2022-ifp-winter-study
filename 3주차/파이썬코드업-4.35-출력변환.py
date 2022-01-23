'''
16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
'''

x = '0x' + input()
integer = int(x, 16)
octal = oct(integer)
print(octal[2:])