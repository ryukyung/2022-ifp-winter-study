# n개의 정수가 순서대로 입력된다.
# (단 n의 최대 개수는 알 수 없다.)
# n개의 입력된 정수를 순서대로 출력해보자.
# while( ), for( ) 등의 반복문을 사용할 수 없다.

# 입력
# 첫 줄에 정수의 개수 n이 입력되고, 두 번째 줄에 n개의 정수가 공백을 두고 입력된다.
# 5  
# 1 2 3 4 5  

# 출력
# n개의 정수를 한 개씩 줄을 바꿔 출력한다.
# 1  
# 2  
# 3  
# 4  
# 5  

# 내 풀이)
def printNumber(num, i):
    if i == end:
        return
    print(num[i])
    i += 1
    printNumber(num, i)
end = int(input())
num = list(map(int, input().split()))
printNumber(num, i = 0)

# 강의 풀이)
