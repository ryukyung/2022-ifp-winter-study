'''
1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
'''
boolean = int(input())
print( not boolean )


'''
두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.
'''
for _ in range(4): #4번 반복
      x, y = map(int, input().split())
      print( x and y )


'''
두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
'''
for i in range(4): #4번 반복
      x, y = map(int, input().split())
      print( x or y )


'''
두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
'''
for _ in range(4):
    x, y = map(int, input().split())
    print( (x and (not y)) or ((not x) and y) ) #x가 참 이고 y가 거짓일 때 또는 x가 거짓이고 y가 참일때


'''
두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
'''
for _ in range(4):
      x, y = map(int, input().split())
      print( ((not x) and (not y)) or (x and y) )


'''
두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
'''
for _ in range(4):
      a, b = map(int, input().split())
      print( not(a or b) )


'''
1개의 정수형 입력이 들어오면 논리 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
'''
x = int(input())
print( x%2 and '홀수' or '짝수' )