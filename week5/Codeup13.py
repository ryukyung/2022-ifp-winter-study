#78
#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
a = int(input())
b = range(2, a+1, 2)
print(sum(b))

#79
#원하는 문자가 입력될 때까지 반복 출력하기
#'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
a = input().split()
for b in a:
  print(b)
  if b == 'q': break

#80
#1, 2, 3 ... 을 계속 더해 나갈 때,
#그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지
#계속 더하는 프로그램을 작성해보자.
a = int(input())
b = 0
i = 0
while b < a:
  i += 1
  b += i
print(i)

#81
#주사위를 2개 던지면?
#1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때
#나올 수 있는 모든 경우를 출력해보자.
a, b = map(int, input().split())
for a in range(1, a+1):
  for b in range(1, b+1):
    print(a, b)

#82
#A, B, C, D, E, F 중 하나가 입력될 때,
#1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
#****************다시한번체크*****************
char = input()
for i in range(1, 16):
  print( '%s*%s=%s' %(char, hex(i)[2:].upper(), hex(int(char, 16) * i)[2:].upper()) )

#83
#3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.
a = int(input())
for i in range(1, a+1):
  count = i if i%3 else 'X'
  print(count, end=' ')

#84
#주어진 rgb 빛들을 다르게 섞어 만들 수 있는
#모든 경우의 조합(r g b)과 총 가짓 수를 계산해보자.
r, g, b = map(int, input().split())
count = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      count += 1
print(count)

#85
#1초 동안 마이크로 소리강약을 체크하는 수를 h
#한 번 체크한 결과를 저장하는 비트 b
#좌우 등 소리를 저장할 트랙 개수인 채널 c
#녹음할 시간 s가 주어질 때, 필요한 저장 용량을 계산하는 프로그램을 작성해보자.
#************다시체크***********
h, b, c, s = map(int, input().split())
result = h*b*c*s
resultMB = result / (8 * 1024**2)
print(round(resultMB, 1), 'MB')

#86
#이미지의 가로 해상도 w, 세로 해상도 h,
#한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
#압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.
w, h, b = map(int, input().split())
result = (w*h*b) / (8 * 1024**2)
print( round(result, 2), 'MB' )

#87
#1, 2, 3 ... 을 순서대로 계속 더해나갈 때,
#그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
a = int(input())
b = 0
i = 1
while b < a:
  b += i
  i += 1
print(b)

#88
#1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
#3의 배수인 경우는 출력하지 않도록 만들어보자.
a = int(input())
for i in range(1, a+1):
  if i%3:
    print(i, end=' ')

#89
#시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때
#n번째 수를 출력하는 프로그램을 만들어보자.
a, d, n = map(int, input().split())
i = a
count = 0
arith = []
while count < n:
  arith.append(i)
  i += d
  count += 1
print(arith[-1])

#90
#시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때
#n번째 수를 출력하는 프로그램을 만들어보자.
a, r, n = map(int, input().split())
i = a
count = 0
geom = []
while count < n:
  geom.append(i)
  i *= r
  count += 1
print(geom[-1])

#91
#시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
#n번째 수를 출력하는 프로그램을 만들어보자.
a, m, d, n = map(int, input().split())
i = a
prog = []
while len(prog) < n:
  prog.append(i)
  i = i*m+d
print(prog[-1])

#92
#같은 날 동시에 가입한 3명의 사람들이
#온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때,
#다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
a, b, c = map(int, input().split())
day = 1
while day%a != 0 or day%b != 0 or day%c != 0:
  day += 1
print(day)