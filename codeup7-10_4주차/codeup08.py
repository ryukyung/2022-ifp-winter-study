# [53] 1(true, 참) 또는 0(false, 거짓)이 입력되었을 때 반대로 출력하는 프로그램을 작성해보자.
boolean = int(input())
print( not boolean)

# [54]두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때만 참을 출력하는 프로그램을 작성해보자.
a, b = map(int, input().split())
print(a and b)

# [55]두 개의 참(1) 또는 거짓(0)이  입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
a, b = map(int, input().split())
print(a or b)

# [우리밋이 알려주는 Bonus 문제(1)] 1개의 정수형 입력이 들어오면 논리 연산을 이용하여 '홀수'와 '짝수'를 판별하여라.
num = int(input())
if (num %2)==0:
    print('짝수')
elif (num%2)!=0:
    print('홀수')

# [56]두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.
a, b = map(int, input().split())
print((a and(not b) or ((not a) and b)))

# [57]두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.
a, b = map(int, input().split())
print((not a)and (not b) or (a and b))

# [58]두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.
a, b = map(int, input().split())
print( not (a or b))