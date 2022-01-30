# 58. 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

for _ in range(4):
	a, b = map(int, input().split())
  print(not(a or b))
 
