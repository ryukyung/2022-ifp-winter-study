'''
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
16진수(대문자)로 출력한다.
'''

n = int(input())
print((hex(n).upper())[2:])