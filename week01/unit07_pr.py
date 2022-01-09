# ◼ 다음 소스 코드를 완성하여 날짜와 시간이 출력되게 만드세요.
# year, month, day, hour, minute, second = input().split()
# _______________________________________
# print(hour, minute, second, sep=':')
# 입력 : 1999 12 31 10 37 21
# 결과 : 1999-12-31T10:37:21

year, month, day, hour, minute, second = input().split()
# 정답
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')