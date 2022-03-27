# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# **평가 기준**
# 점수 범위 : 평가
#  90 ~  100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#   0 ~   39 : D
# 로 평가되어야 한다.
# 내 풀이)
score = int(input())
if 90<=score<=100:
    print('A')
elif 70<=score<=89:
    print('B')
elif 40<=score<=69:
    print('C')
elif 0<=score<=39:
    print('D')
else:
    print('0부터 100사이의 점수를 입력하세요')
# 강의 풀이)
grade = int(input())
if grade >= 90:
  print('A+')
elif grade >= 70:
  print('B')
elif grade >= 40:
  print('C')
else:
  print('D')