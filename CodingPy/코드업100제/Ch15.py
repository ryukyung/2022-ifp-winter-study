# [우리밋의 LAST 보너스 문제] 내 미래

fild = [[0 for _ in range(5)] for _ in range(5)]
i, j = map(int, input().split())
lf, rt, up, down = map(int, input().split())

i = i - 1 - up + down
j = j -1 -lf + rt

fild[i][j] = 1

for rowFild in fild:
    print(*rowFild)



# [96] 바둑판에 흰 돌 놓기

fild = [[0]*19 for _ in range(19)]
forInt = int(input())

for _ in range(forInt):
    i , j = map(int, input().split())
    fild[i-1][j-1] = 1

for rowFild in fild:
    print(*rowFild)


# [97] 바둑판에 십자 뒤집기

baduk = [
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
]

forInt = int(input())

for _ in range(forInt):
    i, j = map(int, input().split())
    for y in range(19): 
        baduk[y][j-1] = 1 if baduk[y][j-1] == 0 else 0 
        baduk[i-1][y] = 1 if baduk[i-1][y] == 0 else 0 

for rowBaduk in baduk:
    print(*rowBaduk)


# [98] 설탕과자 뽑기

x, y = map(int, input().split())
xyFild = [[0 for _ in range(x)] for _ in range(y)]

stickNum = int(input())
for _ in range(stickNum):
    l, d, sX, sY = map(int, input().split())
    if d == 0:
        for _ in range(l):
            xyFild[sX-1][sY-1] = 1
            sY += 1
    else:
        for _ in range(l):
            xyFild[sX-1][sY-1] = 1 
            sX += 1


for fild in xyFild:
    print(*fild)


# [99] 성실한 개미

ant_house = [
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


i = 1
j = 1

def moveDOWN():
    pass

def moveRIGHT():
    pass

def move():
    global i 
    global j 
    if ant_house[i][j] == 2:
        ant_house[i][j] = 9
        return
    else:
        ant_house[i][j] = 9

    if ant_house[i][j+1] == 0:
        j = j + 1
        move()
    elif ant_house[i][j+1] == 1:
        i = i + 1
        move()

move()    

for antHouseView in ant_house:
    print(*antHouseView)

