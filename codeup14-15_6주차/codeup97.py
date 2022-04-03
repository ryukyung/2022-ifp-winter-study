'''[97] 바둑판에 십자 뒤집기   
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가 "십(+)자 뒤집기를 해볼까?"하고 생각했다. 
바둑판(19*19)에 흰돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
입력)
 - 바둑알이 깔려 있는 상황이 19*19 크기의 정수값으로 입력된다.
 - 십자 뒤집기 횟수(n)가 입력된다.
 - 십자 뒤집기 좌표가 횟수(n)만큼 입력된다. 단, n은 10 이하의 자연수이다.

출력) 십자 뒤집기 결과를 출력한다. '''
space = []
for _ in range(19) : 
    basic = list(map(int, input().split()))   # map으로 인덱스 접근x -> list 사용
    space.append(basic)                       # 새로운 요소를 space 맨 끝에 객체로 추가

n = int(input())
for _ in range(n):
    x, y= map(lambda num : int(num)-1, int, input().split()) # lambda_mum-1해서 반환
    for i in range(19):
        if space[i][y] == 0: space[i][y] = 1                 # y축
        else: space[i][y] = 0
        # space[i][y] = 1 if space[i][y] == 0 else 0
        if space[x][i] == 0: space[x][i] = 1                 # x축
        else: space[x][i] = 0
        # space[x][i] = 1 if space[x][i] == 0 else 0
for s in space:
    print(*s)