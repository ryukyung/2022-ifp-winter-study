# 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.
# 년월일(yyyy.mm.dd)를 입력받아,
# 일월년(dd-mm-yyyy)로 출력해보자.
# (단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)
# 내 풀이)
y, m ,d = input().split('.')
if len(m) == 1:
    m = '0' + m
if len(d) == 1:
    d = '0' + d
print('{}-{}-{}'.format(d,m,y))
# 강의 풀이)
y, m, d = input().split('.')
m = '0'+m if len(m) == 1 else m
d = '0'+d if len(d) == 1 else d
print('{}-{}-{}'.format(d, m, y))