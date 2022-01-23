'''
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
16진수(대문자)로 출력한다.
'''
hexadecimal = int(input())
big = hex(hexadecimal)[2:]
print( big.upper() ) #.upper로 대문자 표기