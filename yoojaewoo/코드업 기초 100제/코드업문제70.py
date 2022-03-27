# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

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
for i in num:
    if i == 0:
        break
    print(i)
# 강의 풀이)
# 1
number = map(int, input().split())
for element in number:
  if element is not 0:
    print(element)
    continue # continue를 만나면 아래의 구문은 실행하지 않고 다음 반복으로 넘어간다.
  break

# 2
number = map(int, input().split())
for value in number:
  if value == 0: break
  print( value )