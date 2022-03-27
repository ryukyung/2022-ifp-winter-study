# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.
# 입력
# 정수가 순서대로 입력된다.
# 7 4 2 3 0 1 5 6 9 10 8
# 출력
# 입력된 정수를 줄을 바꿔 하나씩 출력하는데, 0이 입력되면 종료한다. (0은 출력하지 않는다.)
# 7
# 4
# 2
# 3
# 내 풀이)
num = map(int, input().split())

# 강의 풀이)
def goto(array, i):
  if array[i] == 0:
    return
  print(array[i])
  i += 1
  goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)