# 정수가 순서대로 입력된다. (단, 개수는 알 수 없다.) 
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

#1
number = map(int, input().split())

for element in number:
  if element is not 0:
    print(element)
    continue # continue를 만나면 아래의 구문은 실행하지 않고 다음 반복으로 넘어간다.
  break