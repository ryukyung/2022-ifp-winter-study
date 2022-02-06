#71
#정수가 순서대로 입력된다.
#(단, 개수는 알 수 없다.)
#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
#while( ), for( ) 등의 반복문을 사용할 수 없다.
#입력
#정수가 순서대로 입력된다.
#출력
#입력된 정수를 줄을 바꿔 하나씩 출력하는데,
#0이 입력되면 종료한다. (0은 출력하지 않는다.)
# 재귀함수, 다시 한번 확인
def goto(array, i):
  if array[i] == 0:
    return
  print(array[i])
  i += 1
  goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)

#72
#n개의 정수가 순서대로 입력된다.
#(단 n의 최대 개수는 알 수 없다.)
#n개의 입력된 정수를 순서대로 출력해보자.
#while( ), for( ) 등의 반복문을 사용할 수 없다.
#입력
#첫 줄에 정수의 개수 n이 입력되고, 두 번째 줄에 n개의 정수가 공백을 두고 입력된다.
#출력
#n개의 정수를 한 개씩 줄을 바꿔 출력한다.
n = int(input())
number = list(map(int, input().split()))
def goto(number, n, i):
  if i == n: return
  print( number[i] )
  i += 1
  goto(number, n, i)
goto(number, n, 0)

#73
#정수가 순서대로 입력된다.
#(단, 개수는 알 수 없다.)
#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
#입력
#정수가 순서대로 입력된다.
#출력
#입력된 정수를 줄을 바꿔 하나씩 출력하는데,
#0이 입력되면 종료한다. (0은 출력하지 않는다.)
number = map(int, input().split())
for value in number:
  if value == 0: break
  print( value )

#74
#정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
#입력
#정수 1개가 입력된다. (1 ~ 100)
#출력
#1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
count = int(input())
for i in range(count, 0, -1):
  print( i )

#75
#정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
#입력
#정수 1개가 입력된다. (1 ~ 100)
#출력
#1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
count = int(input())
for i in range(count-1, -1, -1):
  print( i )

#76
#영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
#입력
#영문자 1개가 입력된다. (a ~ z)
#출력
#a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.
converter = ord(input())
for i in range(97, converter+1):
  print( chr(i), end=' ' )

#77
#정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
#입력
#정수 1개가 입력된다. (0 ~ 100)
#출력
#0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.
count = int(input())
i = 0
while count >= 0:
  print( i )
  i += 1
  count -= 1