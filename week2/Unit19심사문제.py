#Unit19
#입력받은 정수의 높이만큼 산 모양으로
#별을 출력하는 프로그램 작성
height = int(input())
for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height):
        if j < i:
            print('*', end='')
    print()