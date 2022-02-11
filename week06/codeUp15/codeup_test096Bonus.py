# 훈련병인 철수는 교관의 지시에 따라야한다.
# 교관은 "좌로 1보, 하로 2보 가!"와 같이 좌,우,상,하로 이동할 것을 명령한다.
# 철수의 현재 위치가 입력으로 주어질 때 교관의 명령대로 이동한 위치는 어디일까?

# 제한 조건
# 1. 철수의 현재 위치는 첫 입력 값으로 공백을 두고 입력된다.
#   ex) 1 1 => (0, 0), 5 4 => (4, 3)
# 2. 훈련소의 전체 공간 크기는 5*5 이다.
# 3. 교관이 지시한 명령은 절대 훈련소 공간을 벗어나지 않는다.
# 4. 좌는 왼쪽, 우는 오른쪽, 상은 위쪽, 하는 아래쪽으로 한다.
# 5. 입력은 좌,우,상,하의 순서대로 공백을 두고 입력된다.
#   ex) 3 2 3 3 => 좌로 2보, 우로 2보, 상으로 3보, 하로 3보 이동.
# 입력

# 3 3
# 1 2 1 3
# 출력

# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 1 0

# 입력
cX, cY = map(int, input().split())
left, right, up, down = map(int, input().split())

# 입력을 통한 최종 좌표 구하기
fX = cY - up + down - 1
fY = cX - left + right - 1

# 1
for i in range(5):
    for j in range(5):
        if fX == i and fY == j:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

# 2
coords = [[0 for _ in range(5)] for _ in range(5)]
coords[fX][fY] = 1
for crd in coords:
    print(*crd)
