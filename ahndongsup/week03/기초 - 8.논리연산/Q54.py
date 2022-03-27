# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 
# 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.

# Tip
# 파이썬에서는 AND연산값이 참이면 뒤에 있는 값을 출력하게 된다.
# ex) '앞' and '뒤' >> '뒤'

for _ in range(4):
  a, b = map(int, input().split())
  print( a and b )