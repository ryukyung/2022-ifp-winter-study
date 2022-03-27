# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
# 내 풀이)
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)
# 강의 풀이)
# 1
a, b, c = map(int, input().split())
if not a%2: print(a)
if not b%2: print(b)
if not c%2: print(c)

#2
a, b, c = map(int, input().split())
print( *(filter(lambda num: num%2 == 0, [a, b, c])) )