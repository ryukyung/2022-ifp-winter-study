# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자
 
a, b, c = map(int, input().split())
if not a%2: print(a)
if not b%2: print(b)
if not c%2: print(c)

# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자

a, b, c = map(int, input().split())
print( 'odd' if a%2 else 'even' )
print( b%2 and 'odd' or 'even' )
print( ['even', 'odd'][c%2] )

# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자

num = int(input())
print( num>0 and 'plus' or 'minus' )
print( num%2 and 'odd' or 'even' )

# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자

grade = int(input())
if grade >= 90:
  print('A+')
elif grade >= 70:
  print('B')
elif grade >= 40:
  print('C')
else:
  print('D')

# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자
# [평가 : 내용]
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

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

# 월이 입력될 때 계절 이름이 출력되도록 해보자
# 예
# [월 : 계절 이름]
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall

month = int(input())
if month==12 or month==1 or month==2:
  print('winter')
elif month==3 or month==4 or month==5:
  print('spring')
elif month==6 or month==7 or month==8:
  print('summer')
else:
  print('fall')