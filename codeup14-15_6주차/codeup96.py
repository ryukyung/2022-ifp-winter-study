'''[96]. 바둑판에 흰 돌 놓기
영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가 "바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다. 
바둑판(19*19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
입력) 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
    둘째 줄부터 n+1번째 줄까지 흰 돌을 놓을 좌표(x,y)가 n줄 입력된다.
    n은 10 이하의 자연수이고 x,y 좌표는 1~19까지이며, 같은 좌표는 입력되지 않는다.
출력) 흰 돌이 올려진 바둑판의 상황을 출력한다.
    흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.'''
import numpy
n = int(input())                           # 올릴 흰 돌의 수
space = numpy.zeros( (19,19), dtype = int) # 19*19에 0할당, int형으로 고침(.제거)
for i in range(n):                         # 올릴 흰 돌의 수만큼 돌아
    x, y = map(int, input().split())       # x, y로 흰 돌이 올라갈 위치
    space[x-1][y-1] = 1                    # 0~18이기 때문에 -1
for s in space:
    print(*s)