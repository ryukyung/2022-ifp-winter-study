# 3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다. 
# 3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.

num = int(input())

#1
for i in range(1, num+1):
  count = i if i%3 else 'X'
  print(count, end=' ')

  # 다시 pr
