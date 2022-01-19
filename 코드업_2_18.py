'''
년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

입력
연, 월, 일이 ".(닷)"으로 구분되어 입력된다.
출력
입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.

입력 : 2020.2.9
출력 : 2020.02.09
(단, m 혹은 d가 한 자리 수인 경우 앞에 0을 붙여 출력한다.)
'''
year, month ,day = input().split('.')
if len(month) == 1:
    month = '0' + month
if len(day) == 1:
    day = '0' + day
    print('{}.{}.{}'.format(year,month,day))