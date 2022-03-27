# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. (단, 삼항 연산자 이용)
# Tip::
# 파이썬에서는 논리연산을 이용한 삼항 연산자 외에 if-else를 이용한 삼항 연산도 제공한다. 이러한 이유는 논리연산을 이용한 삼항연산 때 발생할 수 있는 오류가 있기 때문이다.
# 3항 논리 연산의 오류 : 5==5 and 5-5 or 5+5 >> 10
# 위 연산에서는 5==5가 참이기 때문에 5-5가 실행되어 0이 출력되는 것이 맞다. 그러나 10이 출력된다. 이유는 논리 연산의 특성 때문이다.
# 위 구문을 크게 따져보면 (True and false) or true 로 표현할 수 있다. 따라서 앞의 (True and false)가 false가 되므로 or 오른쪽에 true 값인 10이 출력된 것이다.
# if-else를 이용한 삼항 연산은 "(참일 때의 값) if (조건식) else (거짓일 때의 값)"으로 나타낼 수 있다.
# 삼항 연산자는 중첩하여 이용할 수 있다.

# 내 풀이)
a, b, c = map(int, input().split())
if a < b:
    print(a < c and a or c)
elif b < c:
    print(b < a and b or a)
elif c < a:
    print(c < b and c or b)
# 강의 풀이)
a, b, c = map(int, input().split())
num = a if a<b else b
print(  num if num < c else c )


# [우리밋이 알려주는 Bonus 문제 (3)]
# 1개의 정수형 입력이 들어오면 삼항 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
# Tip::
# 입력이 2로 나눠지면 짝수이고, 그렇지 않으면 홀수임을 이용한다.
# 파이썬에서의 논리연산인 AND와 OR의 특징(Chapter 8 참고)을 이용한다. => 파이썬에서는 이러한 연산을 "삼항 연산"으로 정의한다.
# Tip2::
# 입력이 2로 나눠지면 짝수이고, 그렇지 않으면 홀수임을 이용한다.
# 파이썬에서의 삼항 연산은 if-else로도 구현할 수 있다.

# 내 풀이)
a = int(input())
print('짝수' if a % 2 == 0 else '홀수')
# 강의 풀이)
number = int(input())
print( '홀수' if number%2 else '짝수' )