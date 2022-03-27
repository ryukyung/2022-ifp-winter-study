# 두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
# 내 풀이)
a, b = map(int, input().split())
print(not ((a and 1) and (b and 1)))
# 강의 풀이)
a, b = map(int, input().split())
print( (a and (not b)) or ((not a) and b) )
