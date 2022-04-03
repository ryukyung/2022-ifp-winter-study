''' 7.4 연습문제
다음 소스 코드를 완성하여 날짜와 시간이 출력되게 만드세요
'''
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59
print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')
# 2000/10/27 11:43:59

''' 7.5 심사문제
표준 입력으로 년,월,일,시,분,초가 입력됩니다.
다음 소스 코드를 완성하여 입력된 날짜와 시간을 년-월-일T시:분:초 형식으로 출력되게 만드세요
'''
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep='-', end ='T')
print(hour, minute, second, sep=':')