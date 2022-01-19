# [31] 10진수를 입력받아 8진수(octal)로 출력해보자
num = int(input())
print(oct(num)[2:])
# [32] 10진수를 입력받아 16진수(hexadecimal)로 출력해보자
num = int(input())
print(hex(num)[2:])
# [33] 10진수를 입력받아 16진수(hexadecimal)로 출력해보자, 16진수(대문자)로 출력한다
num = int(input())
print( (hex(num).upper())[2:])
# [34] 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자
num = '0o' + input()
print( int(num, 8) )
# [35] 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자
hnum = '0x' + input()
inum = int(hnum, 16)
print( oct(inum))
# [36] 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자
string = ord(input())
print(string)
# [37] 10진 정수 1개를 입력받아 아스키 문자로 출력해보자
num = chr(int(input()))
print(num)