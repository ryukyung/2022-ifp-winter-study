#코딩도장-unit11.9
#표준 입력으로 문자열 두 개가 각 줄에 입력됩니다
#(문자열의 길이는 정해져 있지 않음).
#첫 번째 문자열에서 인덱스가 홀수인 문자와 두 번째 문자열에서 인덱스가 짝수인 문자를 연결하여 출력하는 프로그램을 만드세요
#(input에서 안내 문자열은 출력하지 않아야 합니다). 
#연결 순서는 첫 번째 문자열, 두 번째 문자열 순입니다. 0은 짝수로 처리합니다.

x = input() #입력 python
y = input() #입력 python

z = x[1::2]
k = y[::2]
print(z + k) #yhnpto

a = input() #입력 apple
b = input() #입력 strawberry

c = a[1::2]
d = b[0::2]
print(c + d) #plsrwer

