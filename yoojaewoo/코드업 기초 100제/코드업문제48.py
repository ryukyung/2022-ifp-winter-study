# 두 정수(a, b)를 입력받아 b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
# 내 풀이)
a, b = map(int, input().split())
if a <= b:
    print(1)
else:
    print(0)
# 강의 풀이)
a, b = map(int, input().split())
if b >= a:
  print( 1 )
else:
  print( 0 )