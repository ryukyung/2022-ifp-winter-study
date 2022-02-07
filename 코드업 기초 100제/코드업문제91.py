# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 10
# 10 4 2 3 6 6 7 9 8 5

# 출력
# 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.
# 5 8 9 7 6 6 3 2 4 10

# Tip::
# 리스트의 메소드인 reverse()를 이용하면 된다.

# 내 풀이)
call = int(input())
randomCall = map(int, input().split())
rev = []
for i in randomCall:
    rev.append(i)
rev.reverse()
print(*rev)
# 강의 풀이)
n = int(input())
rand = list(map(int, input().split()))
rand.reverse()
print(*rand)