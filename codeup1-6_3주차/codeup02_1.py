# 기초-입출력(1)
# [10] 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자
var = int(input())
print(var)
# [11] 문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자
var = input()
print(var)
# [12] 실수형(float)으로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자
var = float(input())
print(var)
# [13] 정수(int) 2개를 입력받아 그대로 출력해보자 (단, 띄어쓰기를 기준으로 입력한다)
a, b = map(int, input().split())
print(a, b)
# [14] 2개의 문자(ASSCII CODE)를 입력받아서 순서를 바꿔 출력해보자
a, b = map(int, input().split())
print(b, a)
# [15] 실수(float) 1개를 입력받아 저장한 후 저장되어 있는 값을 소수점 셋째 자리에서 반올림하여 소수점 이하 둘째 자리까지 출력하시오
var = round(float(input()), 2)
print(var)
# [16] int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자
num = int(input())
print(num, num, num)
# [17] 어떤 형식에 맞추어 시간이 입력될 때 그대로 출력하는 연습을 해보자. 콜론 기호를 기준으로 두 수가 각 변수에 저장된다.
h, m = input().split(':')
print(h,':',m)
# [18] 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자
#     연, 월, 일이 "."으로 구분되어 입력된다, 입력받은 연, 월, 일은 yyyy.mm.dd 형식으로 출력한다
year, month, day = input().split('.')
if len(month) == 1:
    month = '0' + month
if len(day) == 1:
    day= '0'+ day
print(year, month, day, sep='.')
# [19] 주민번호는 앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다
#      주민번호 앞 6자리와 뒤 7자리가 '-'로 구분되어 입력된다, '-'를 제외한 주민번호를 모두 붙여 출력한다
first, second = input().split('-')
print(first, second, sep='')