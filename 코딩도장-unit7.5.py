#코딩도장-unit7.5
#표준 입력으로 년, 월, 일, 시, 분, 초가 입력됩니다.
#다음 소스 코드를 완성하여 입력된 날짜와 시간을 년-월-일T시:분:초 형식으로 출력되게 만드세요.

year, month, day, hour, minute, second = input().split()
print(year, month, day, sep = '-', end = 'T') #1999-12-31T
print(hour, minute, second, sep=':') #10:37:21


