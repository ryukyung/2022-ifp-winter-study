# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

# while 사용
count = int(input())

i = 0
while count >= 0:
  print( i )
  i += 1
  count -= 1

# for 사용
count = int(input())

for i in range(0, count+1):
  print( i )