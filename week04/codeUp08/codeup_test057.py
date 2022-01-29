# 두 개의 참(1) 또는 거짓(0)이 입력될 때
# , 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.

# 카르노 맵과 논리식으로 만들기 + 드모르간의 법칙, 분배법칙
# a'b' + ab = (a+b)' + ab => not(a or b) or (a and b)
a, b = map(int, input().split())
print(bool(not(a or b) or (a and b)))
