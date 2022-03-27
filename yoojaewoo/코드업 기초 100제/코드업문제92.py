# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

# 입력
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 10
# 10 4 2 3 6 6 7 9 8 5

# 출력
# 출석을 부른 번호 중에 가장 빠른 번호를 1개만 출력한다.
# 2

# Tip::
# 가장 작은 값을 찾으면 된다.
# 파이썬에서는 배열(iterable) 객체의 원소 중 가장 작은 값을 반환해주는 min() 함수를 제공하고 있다.

# 내 풀이)
# 1
call = int(input())
randomCall = map(int, input().split())
print(min(randomCall))
# 2
call = int(input())
randomCall = map(int, input().split())
min = 23
for i in randomCall:
    if i <= min:
        min = i
print(min)


# 강의 풀이)
n = int(input())
rand = map(int, input().split())
print( min(rand) )