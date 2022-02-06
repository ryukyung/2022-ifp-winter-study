# [71]
# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.


listLike = list(map(int, input().split()))
i = 0
def whileLike(listLike, i):
    if listLike[i] != 0:
        print(listLike[i])
    else:
        return
    i += 1
    whileLike(listLike, i)

whileLike(listLike, i)



# [[72]
# n개의 정수가 순서대로 입력된다.
# (단 n의 최대 개수는 알 수 없다.)

# n개의 입력된 정수를 순서대로 출력해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.


intInit = int(input())
listLike = list(map(int, input().split()))
i = 0

def forLike(listLike, intInit, i):
    
    if intInit > i:
        print(listLike[i])
    else:
        return
    i += 1
    forLike(listLike, intInit, i)

forLike(listLike, intInit, i)


# [73]

# 정수가 순서대로 입력된다.
# (단, 개수는 알 수 없다.)

# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.


forList = map(int, input().split())
for i in forList:
    if i == 0:
        break
    else:
        print(i)


# [74]

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.


intCount = int(input())
for i in range (1, intCount+1):
    print(intCount)
    intCount -= 1



# [75]

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.


intCount = int(input())
for i in range (1, intCount+1):
    print(intCount-1)
    intCount -= 1



# [76]

# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.


charInput = ord(input())
for i in range(97, charInput+1):
    print(chr(i), end=" ")



# [77]

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.


#1번답안 for문
intInput = int(input())
for i in range(0, intInput+1):
    print(i)

#2번답안 while문
intInput = int(input())
i = 0
while(1):
    if i < intInput+1:
        print(i)
        i += 1
    else:
        break
    