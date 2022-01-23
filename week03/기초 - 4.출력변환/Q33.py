# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# 16진수(대문자)로 출력한다.

# Tip
# 소문자를 대문자로 변환하려면 문자열의 메소드(함수)인 upper()를 이용하면 된다.

hexadecimal = int(input())
hexConv = hex(hexadecimal)[2:]
print( hexConv.upper() )