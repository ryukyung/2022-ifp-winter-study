# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

# 입력
# 정수 1개가 입력된다. (1 ~ 100)
# 5

# 출력
# 1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
# 5
# 4
# 3
# 2
# 1

# 내 풀이)
number = int(input())
for i in range(number,0,-1):
    print(i)
# 강의 풀이)
count = int(input())
for i in range(count, 0, -1):
  print( i )