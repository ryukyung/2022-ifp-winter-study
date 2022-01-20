'''
년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

년월일(yyyy.mm.dd)를 입력받아,

일월년(dd-mm-yyyy)로 출력해보자.

(단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
'''
year, month, day = input().split('.')
month = '0'+ month if len(month) == 1 else month
day = '0' + day if len(day) == 1 else day
print('{}-{}-{}'.format(day,month,year))