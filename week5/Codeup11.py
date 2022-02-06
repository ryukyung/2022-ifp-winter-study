#65
#세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
a, b, c = map(int, input().split())
if not a%2: print(a)
if not b%2: print(b)
if not c%2: print(c)

#66
#세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a, b, c = map(int, input().split())
print( *map(lambda num: 'odd' if num%2 else 'even', [a, b, c]) )
#객체가 num에 들어가 참이면 odd 거짓이면 even이 반환

#67
#정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
a = int(input())
print( a>0 and 'plus' or 'minus' )
print( a%2 and 'odd' or 'even' )

#68
#점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
a = int(input())
if a >= 90:
  print('A+')
elif a >= 70:
  print('B')
elif a >= 40:
  print('C')
else:
  print('D')

#69
#평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
a = input()
if a == 'A':
  print('best!!!')
elif a == 'B':
  print('good!!')
elif a == 'C':
  print('run!')
elif a == 'D':
  print('slowly~')
else:
  print('what?')

#70
#월이 입력될 때 계절 이름이 출력되도록 해보자.
a = int(input())
if a==12 or a==1 or a==2:
  print('winter')
elif a==3 or a==4 or a==5:
  print('spring')
elif a==6 or a==7 or a==8:
  print('summer')
else:
  print('fall')