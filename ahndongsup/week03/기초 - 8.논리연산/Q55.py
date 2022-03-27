# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 
# 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.

# Tip
# 파이썬에서는 OR연산값이 참이면 참인 값을 출력하게 된다.
# ex) '참' or 0 >> '참
# ex) 0 or True >> True

for i in range(4):
  a, b = map(int, input().split())
  print( a or b )