'''
세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
'''
a, b, c = map(int, input().split())
if not a%2: print(a)
if not b%2: print(b)
if not c%2: print(c)


'''
세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''
a, b, c = map(int, input().split())
print('odd' if a%2 else 'even')
print('odd' if b%2 else 'even')
print('odd' if c%2 else 'even')


'''
정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
'''
x = int(input())
print('plus'if x>0 else 'minus')
print('odd' if x%2 else 'even')


'''
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

**평가 기준**
점수 범위 : 평가
 90 ~  100 : A
 70 ~   89 : B
 40 ~   69 : C
  0 ~   39 : D
로 평가되어야 한다.
'''
x = int(input())
if x>=90:
    print('A+')
elif x>=70:
    print('B')
elif x>=40:
    print('C')
else:
    print('D')


'''
평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
[평가 : 내용]
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?
'''
x = input()
if x == 'A':
    print('best!!!')
elif x == 'B':
    print('good!!')
elif x == 'C':
    print('run!')
elif x == 'D':
    print('slowly~')
else:
    print('what?')


'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

예
[월 : 계절 이름]
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
'''
x = int(input())
if x==12 or x==1 or x==2:
    print('winter')
elif x==3 or x==4 or x==5:
    print('spring')
elif x==6 or x==7 or x==8:
    print('summer')
else:
    print('fall')
