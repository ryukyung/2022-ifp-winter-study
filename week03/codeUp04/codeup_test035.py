# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.
num ='0x' +input()
numToInt = int(num,16)
print(oct(numToInt)[2:])
