# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

# 입력
# 정수 1개가 입력된다. (0 ~ 100)
# 4

# 출력
# 0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.
# 0
# 1
# 2
# 3
# 4

# 내 풀이)
number = int(input())
for i in range(0, number + 1, 1):
    print(i)

# 강의 풀이)
#1 
count = int(input())
i = 0
while count >= 0:
  print( i )
  i += 1
  count -= 1
# 2 
count = int(input())
for i in range(0, count+1):
  print( i )