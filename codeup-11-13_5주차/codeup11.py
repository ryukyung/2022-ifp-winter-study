# [65] 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
a,b,c = map(int, input().split())
if a%2==0: print(a)
if b%2==0: print(b)
if c%2==0: print(c)

# [66] 세 정수 a,b,c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
a,b,c = map(int, input().split())
print( 'odd' if a%2 else 'even') 
print( 'odd' if b%2 else 'even')
print( 'odd' if c%2 else 'even')

# [67] 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
num = int(input())
print( num > 0 and 'plus' or 'minus')
print( num%2 and 'odd' or 'even')

# [68] 점수(정수, 1~100)를 입력받아 평가를 출력해보자 
score = int(input())
if score >= 90: print('A')
elif score >= 70: print('B')
elif score >= 40: print('C')
else: print('D')

# [69] 평가를 문자(A,B,C,D,...)로 입력받아 내용을 다르게 출력해보자
string = input()
if string =='A': print('best!!!')
elif string =='B': print('good!!')
elif string =='C': print('run!')
elif string =='D': print('slowly~')
else: print('what?')

# [70] 월이 입력될 때 계절 이름이 출력되도록 해보자
month = int(input())
if (month == 1) or (month == 2) or (month == 12): print('winter')
elif (month == 3) or (month == 4) or (month == 5): print('spring')
elif (month == 6) or (month == 7) or (month == 8): print('summer')
else: print('fall')