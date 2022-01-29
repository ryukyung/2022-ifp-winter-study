# 두 가지의 참(1) 또는 거짓(0)이 입력될 때
# , 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.

# 카르노 맵과 논리식으로 만들기 + 드모르간의 법칙, 분배법칙
# a'b + ab' => ( a and not(b)) or ( not(a) and b )
a, b = map(int, input().split())
print(bool((a and not(b)) or (not(a) and b)))
