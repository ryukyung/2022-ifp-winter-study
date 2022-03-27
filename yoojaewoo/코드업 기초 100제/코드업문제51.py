# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
# 내 풀이)
a, b = map(bool, input().split())
if a == True and b == True:
    print('True')
# 강의 풀이)
for _ in range(4):
  a, b = map(int, input().split())
  print( a and b )
# 파이썬에서는 AND연산값이 참이면 뒤에 있는 값을 출력하게 된다.