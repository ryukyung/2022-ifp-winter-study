# 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 
# 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?

a, b, c = map(int, input().split())
day = 1
while day%a != 0 or day%b != 0 or day%c != 0:
  day += 1
print( day )

day = 1
while 1:
  day += 1
  if day%a == 0 and day%b == 0 and day%c == 0: break
print( day )
