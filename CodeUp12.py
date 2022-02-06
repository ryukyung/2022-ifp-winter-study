# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.

def goto(array, i):
  if array[i] == 0:
    return
  print(array[i])
  i += 1
  goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)

# n개의 정수가 순서대로 입력된다.
# (단 n의 최대 개수는 알 수 없다.)
# n개의 입력된 정수를 순서대로 출력해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.

n = int(input())
number = list(map(int, input().split()))

print('== #1 ==')

def goto(number, n, i):
  if i == n: return
  print( number[i] )
  i += 1
  goto(number, n, i)

goto(number, n, 0)

# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

number = map(int, input().split())

for element in number:
  if element is not 0:
    print(element)
    continue # continue를 만나면 아래의 구문은 실행하지 않고 다음 반복으로 넘어간다.
  break

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

count = int(input())

for i in range(count, 0, -1):
  print( i )

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

count = int(input())

for i in range(count-1, -1, -1):
  print( i )

# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

converter = ord(input())

for i in range(97, converter+1):
  print( chr(i), end=' ' )

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.

count = int(input())

i = 0
while count >= 0:
  print( i )
  i += 1
  count -= 1