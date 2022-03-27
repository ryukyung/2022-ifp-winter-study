# 두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.
# 내 풀이)
a, b = map(int, input().split())
print(a or b)
# 강의 풀이)
a, b = map(int, input().split())
print(a or b)
# 파이썬에서는 OR연산값이 참이면 참인 값을 출력하게 된다.
# ex) '참' or 0 >> '참
# ex) 0 or True >> True

# [우리밋이 알려주는 Bonus 문제 (1)]
# 1개의 정수형 입력이 들어오면 논리 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
# Tip::
# 입력이 2로 나눠지면 짝수이고, 그렇지 않으면 홀수임을 이용한다.
# 파이썬에서의 AND와 OR의 특징을 이용한다. => 파이썬에서는 이러한 연산을 "삼항 연산"으로 정의한다.(삼항연산은 Chapter 10에서 다룬다)
# 내 풀이)
a = int(input())
if a % 2 and True == True:
    print('홀수')
else:
    print('짝수')
# 강의 풀이)
number = int(input())
print( number%2 and '홀수' or '짝수' )