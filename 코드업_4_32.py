'''
10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
'''
hexadecimal = int(input()) #hexadecimal에 int형으로 입력받은 수 저장
print( hex(hexadecimal)[2:] ) #[2:]으로 앞 두자리 수 생략