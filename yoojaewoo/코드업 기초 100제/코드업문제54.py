# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
# 내 풀이)
a, b = map(int, input().split())
print((1 and a) and (1 and b))
# 강의 풀이)
a, b = map(int, input().split())
print( ((not a) and (not b)) or (a and b) )
