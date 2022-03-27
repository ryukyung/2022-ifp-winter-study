# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
# 내 풀이)
a, b = map(int, input().split())
print((not a) and (not b))
# 강의 풀이)
a, b = map(int, input().split())
print( not(a or b) )