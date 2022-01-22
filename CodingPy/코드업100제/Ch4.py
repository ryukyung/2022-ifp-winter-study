# [31]

# 10진수를 입력받아 8진수(octal)로 출력해보자.

# Tip::

# 8진수는 '0o12'처럼 숫자 앞에 '0o'를 붙여준다. 이것으로 '12'가 8진수의 '12'임을 인지한다.
# 10진수를 8진수로 변환하는 함수는 oct()이며, '0o12'와 같이 출력되므로 앞 두자리를 생략하고 출력하면된다. 따라서 '0o12'[2:]를 해주면 되는 것.


tenByOct = int(input())
print(oct(tenByOct)[2:])



# [32]

# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

# Tip::

# 16진수는 '0xa'처럼 숫자 앞에 '0x'를 붙여준다. 이것으로 'a'가 16진수의 'a'임을 인지한다.
# 10진수를 16진수로 변환하는 함수는 hex()이며, '0xa'와 같이 출력되므로 앞 두자리를 생략하고 출력하면된다. 따라서 '0xa'[2:]를 해주면 되는 것.


tenByHexa = int(input())
print(hex(tenByHexa)[2:])



# [33]
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# 16진수(대문자)로 출력한다.

# Tip::

# 소문자를 대문자로 변환하려면 문자열의 메소드(함수)인 upper()를 이용하면 된다.


tenByHexa = int(input())
tenByHexa = hex(tenByHexa)[2:]
print(tenByHexa.upper())



# [34]
# 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.

# Tip::

# 10진수로 변환하고자 할 때는 int()를 이용하면 된다. 첫번째 파라미터로는 변환하고자하는 숫자의 문자열('0o12')을, 두번째 파라미터로는 첫번째 값이 몇 진수인지를 정수로 입력하면 된다.


inputOct = input()
if "0o" in inputOct:
    pass
else:
    inputOct = "0o" + inputOct
print(int(inputOct,8))



# [35]

# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.

# Tip::

# 16진수 >> 10진수 >> 8진수 순서대로 변환


inputHex = input()
if "0x" in inputHex:
    pass
else:
    inputHex = "0x" + inputHex
intVerHex = int(inputHex, 16)
print(oct(intVerHex)[2:])



# [36]

# 영문자 1개를 입력받아 아스키 코드표의 10진수 값으로 출력해보자.

# 아스키 코드란?

# 문자를 이진수의 7비트로 표현한 것
# 예 ) A => 1100001
# Tip::

# 문자열에 대응되는 아스키코드를 반환해주는 함수 ord()를 이용하면 된다.


engVerAsc = input()
print(ord(engVerAsc))



# [37]

# 10진 정수 1개를 입력받아 아스키 문자로 출력해보자.


numberVerAsc = chr(int(input()))
print(numberVerAsc)

