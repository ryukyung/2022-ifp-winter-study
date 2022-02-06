# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.
# 입력
# 정수가 순서대로 입력된다.

# 출력
# 입력된 정수를 줄을 바꿔 하나씩 출력하는데,
# 0이 입력되면 종료한다. (0은 출력하지 않는다.)
def arrayTest(array, i):
    if i == len(a):
        return
    if array[i] == 0:
        return
    else:
        print(array[i])
        i = i + 1
        arrayTest(array, i)


number = list(map(int, input().split()))
arrayTest(number, i=0)
