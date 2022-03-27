# 3 6 9 게임의 왕이 되자
# 3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.

# 입력
# 10 보다 작은 정수 1개가 입력된다. (1 ~ 9)
# 9

# 출력
# 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데, 3 또는 6 또는 9인 경우 그 수 대신 영문 대문자 X 를 출력한다.
# 1 2 X 4 5 X 7 8 X

# 내 풀이)
end = int(input())
for i in range(1, end+1):
    if i % 3 == 0:
        print('X')
    else:
        print(i, end=' ')
# 강의 풀이)
num = int(input())
#1
for i in range(1, num+1):
  count = i if i%3 else 'X'
  print(count, end=' ')
#2
for i in range(1, num+1):
  count = 'X' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i
  print(count, end=' ')