'''
년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력해보자.
(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
'''

y, m, d = input().split('.')
t = '{}-{}-{}'.format(y, m, d)
if len(m) == 1 and len(d) == 1:
    m = '0'+ m
    d = '0'+ d
elif len(m) == 1:
    m = '0'+ m
elif len(d) == 1:
    d = '0'+ d
print(t)