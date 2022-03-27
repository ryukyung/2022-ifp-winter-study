# 두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.

# Tip
# 이러한 논리연산을 XOR(exclusive or, 배타적 논리합)연산이라고도 부른다. 
# 이를 표현하기 위해서는 (a AND (NOT b)) OR ((NOT a) AND b)처럼 하면 된다.

for _ in range(4):
  a, b = map(int, input().split())
  print( (a and (not b)) or ((not a) and b) )