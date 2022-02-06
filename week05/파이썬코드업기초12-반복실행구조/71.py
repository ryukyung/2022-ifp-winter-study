# 정수가 순서대로 입력된다. (단, 개수는 알 수 없다.) 
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자. 
# while( ), for( ) 등의 반복문을 사용할 수 없다.

# define : 정의하다
# 파이썬에서 함수는 def(define)을 써서 정리한다.
# 재귀함수

def goto(array, i):
  if array[i] == 0:
    return
  print(array[i])
  i += 1
  goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)
