'''[71]
정수가 순서대로 입력된다.(단, 개수는 알 수 없다.)
0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
while(), for() 등의 반복문을 사용할 수 없다. '''
def go(number, i):   # go함수 생성
    if number[i]==0: # number 자체 말고 원소 비교를 위한 i, number[i]가 0이면
        return       # 나가
    print(number[i]) # i 출력
    i += 1           # 정수가 순서대로 입력됨 -> +1씩 해야함
number = list(map (int, input().split())) 
go(number, i=0)

'''[72]
n개의 정수가 순서대로 입력된다.(단 n의 최대 개수는 알 수 없다.)
n개의 입력된 정수를 순서대로 출력해보자.
while(), for() 등의 반복문을 사용할 수 없다. '''
n = int(input())
number = list(map(int, input().split()))
def go(number, n, i):
    if n == i:        # n이랑 i가 같으면
        return        # 나가
    print(number[i])  # number[i] 출력
    i += 1            # 정수가 순서대로 입력됨 -> +1
    go(number, n, i)  # i 다음인 i+1로 가
go(number, n, 0)
 
'''[73]
정수가 순서대로 입력된다.(단, 개수는 알 수 없다.)
0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자. '''
number = map(int, input().split())
for i in number:
    if i is not 0: 
        print(i)
        continue # break로 안 가고 위로 올라감
    break        # i가 0이면 나가

# [74]&[75] 정수(1~100) 1개가 입력되었을 때 카운트다운을 출력해보자.
count = int(input())
for i in range(count, 0, -1): # count부터 0까지 1씩 작아짐
    print(i)

# [76] 영문자(a~z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
string = ord(input())
for i in range(97, string+1):
    print( chr(i), end='')

# [77] 정수(0~100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
count = int(input())
for i in range(0, count+1):
    print(i)