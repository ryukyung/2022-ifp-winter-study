# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# 평가 내용
# [평가 : 내용]
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?
# 내 풀이)
grade = input()
if grade == 'A' or 'a':
    print('best!!!')
elif grade == 'B' or 'b':
    print('good!!')
elif grade == 'C' or 'c':
    print('run!')
elif grade == 'D' or 'd':
    print('slowly~')
else:
  print('what?')
# 강의 풀이)
word = input()
if word == 'A':
  print('best!!!')
elif word == 'B':
  print('good!!')
elif word == 'C':
  print('run!')
elif word == 'D':
  print('slowly~')
else:
  print('what?')