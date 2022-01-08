#Unit03
#Hello, world! 올바르게 출력하기
print('Hello, world!')

#연습문제:문자열 출력하기
#다음 소스 코드를 완성하여 'Hello, world!'와 'Python Programming'이 각 줄에 출력되게 만드세요.
#print('Hello, world!') -> Hello, world!
#print(               ) -> Python Programming
print('Python Programming')

#문자열 출력하기
#Hello, world!
#Hello, world! 나오게 소스작성
print('Hello, world!')
print('Hello, world!')

#Unit05
#연습문제 0.2467 * 도로와의 거리(m) + 4.159 - 12m일때
#print(                    )
print(int(0.2467 * 12 + 4.159))

#심사문제
# 스킬피해량 계수 : ap * 0.6 + 225 에서 ap가 120일때
# 스킬의 피해량이 출력되는 소스
print(102 * 0.6 + 225)

#Unit06
# 50, 100, None 이 출력되게 작성
#_________
#_________
#_________
#print(a)
#print(b)
#print(c)
a = 50
b = 100
c = "None"

#국어, 영어, 수학, 과학 점수를 입력받아 평균 출력하는 프로그램 작성
korean, english, mathematics, science = map(int, input().split())
print((korean + english + mathematics + science) // 4)

#Unit07
# 밑줄친 부분에 들어갈 코드만 작성하시오
year, month, day, hour, minute, second = input().split()
#_______________________________________
print(hour, minute, second, sep=':')
#출력예시 : 1999-12-31T10:37:21
print(year, month, day, sep='-', end='T')

#Unit08
#입력받은 점수가
#국어는 90점이상, 영어는 80점초과, 수학은 85점초과, 과학은 80점이상
#일 때 합격(한 과목이라도 조건에 만족하지 않으면 불합격)이며
#합격이면 True, 불합격이면 False가 출력되게 작성
korean, english, mathematics, science = map(int, input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)

#Unit09
#결과대로 문자열이 출력되게 작성
#'Python' is a "programming language"
#that lets you work quickly
#and
#integrate systems more effectively.
s = ''''Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

#Unit10
#-10부터 10까지 입력된 정수만큼 증가하는 숫자가
#들어가는 튜플을 만들고 출력하기
print(tuple(range(-10, 10, int(input()))))

#Unit11
#입력받은 숫자 또는 문자열이 저장된 리스트 x에서
#마지막 요소 5개를 삭제한 뒤 튜플로 출력되게 작성
x = input().split()
del x[-5:]
print(tuple(x))

#각 두줄에 입력 받은 문자열중
#첫번째 문자열은 인덱스가 홀수
#두번째 문자열은 인덱스가 짝수인 문자를 연결하여 출력하는 프로그램 작성
a = input()
b = input()
print(a[1::2]+b[0::2])

#Unit12
#입력받은 문자열과 숫자(실수)
#첫번째 줄은 키, 두번째 줄은 값으로 하여 딕셔너리를 생성한 뒤
#딕셔너리를 출력하는 프로그램 작성
a = input().split()
b = map(float, input().split())
c = dict(zip(a,b))
print(c)
