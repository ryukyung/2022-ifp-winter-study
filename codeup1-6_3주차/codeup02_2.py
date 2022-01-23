# 기초-입출력(2)
# [20] 1개의 문자열을 입력받아 그대로 출력해보자 
# [22] 공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의 단어로 구성되고 엔터로 끝난다
string = input()
print(string)

# [23] 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
string = input().split('.')
print('''\
{}
{}
'''. format(string[0], string[1]))

# [24] 영어 단어를 1개 입력받는다. 입력받은 단어의 각 문자를 1줄에 1문자씩 분리해 출력한다.
#      (단, 단어의 문자를 하나씩 나누어 한 줄에 한 개씩 ''로 묶어서 출력한다.)
string = input()
for i in string:
    print("'{}' ".format(i))

# [25] 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
num = input()
count = len(num) -1 # 5->4->3->2->1 자리
for i in range(len(num)): # integer의 길이만큼 반복
    print([int(num[i] + '0'*count)]) # 자리 수에 맞게 0을 붙임
    count -= 1

# [26] 입력되는 시:분:초에서 분만 출력해보자
h,m,s= input().split(':')
print(m)

# [27] 년월일을 출력하는 방법은 나라마다, 형식마다 다르다. 년월일(yyyy.mm.dd)을 입력받아 일월년(dd-mm-yyyy)로 출력해보자
#      (단, 한 자리 일/월은 0을 붙여 두 자리로 출력한다)
year, month, day = input().split('.')
if len(month) == 1:
    month = '0'+month
if len(day) ==1:
    day = '0'+day
print('{}-{}-{}'.format(day, month, year))