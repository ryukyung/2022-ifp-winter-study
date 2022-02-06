'''''''''''''''''''''
65. 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.
'''''''''''''''''''''

# 방법 1
a, b, c = map(int, input().split())
if not a % 2:
    print(a)
if not b % 2:
    print(b)
if not c % 2:
    print(c)

# 방법 2
a, b, c = map(int, input().split())
print(*(filter(lambda num: not(num % 2), [a, b, c])))
# 조건식 not(num % 2)의 num에 a, b, c가 차례대로 들어가고 결과가 참인 값만 반환된다.
# filter()는 filter 타입으로 반환되기 때문에 리스트나 튜플에 넣어주어야 한다.
# *를 사용하면 대괄호나 괄호 없이 리스트나 튜플 안의 값들만 출력할 수 있다.

'''''''''''''''''''''
66. 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
'''''''''''''''''''''

a, b, c = map(int, input().split())

# 방법 1
print(*(filter(lambda num: 'odd' if num % 2 else 'even', [a, b, c])))

# 방법 2
print('odd' if a % 2 else 'even')
print(b % 2 and 'odd' or 'even')
print(['even', 'odd'][c % 2])

'''''''''''''''''''''
67. 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

입력 : -4
출력 : 
minus
even
'''''''''''''''''''''

a = int(input())
print('minus' if a < 0 else 'plus')
print('odd' if a % 2 else 'even')

'''''''''''''''''''''
68. 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

**평가 기준**

| 점수 범위 | 평가 |
| --------- | ---- |
| 90 ~ 100  | A    |
| 70 ~ 89   | B    |
| 40 ~ 69   | C    |
| 0 ~ 39    | D    |

'''''''''''''''''''''

a = int(input())
if a >= 90:
  print('A')
elif a >= 70:
  print('B')
elif a >= 40:
  print('C')
else:
  print('D')

'''''''''''''''''''''
69. 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

| 평가          | 내용    |
| ------------- | ------- |
| A             | best!!! |
| B             | good!!  |
| C             | run!    |
| D             | slowly~ |
| 나머지 문자들 | what?   |
'''''''''''''''''''''

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

'''''''''''''''''''''
70. 월이 입력될 때 계절 이름이 출력되도록 해보자.

| 월        | 계절 이름 |
| --------- | --------- |
| 12, 1, 2  | winter    |
| 3, 4, 5   | spring    |
| 6, 7, 8   | summer    |
| 9, 10, 11 | fall      |
'''''''''''''''''''''

a = int(input())

# 방법 1
if a == 12 or a == 1 or a == 2:
  print('winter')
elif a == 3 or a == 4 or a == 5:
  print('spring')
elif a == 6 or a == 7 or a == 8:
  print('summer')
else:
  print('fall')

# 방법 2
if a in [12, 1, 2]:
  print('winter')
elif a in [3, 4, 5]:
  print('spring')
elif a in [6, 7, 8]:
  print('summer')
else:
  print('fall')
