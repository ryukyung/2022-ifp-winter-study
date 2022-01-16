'''
표준 입력으로 삼각형의 높이가 입력됩니다. 
입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요. 
이때 출력 결과는 예제와 정확히 일치해야 합니다. 
모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.
'''

x = int(input())
for i in range(x):
    for j in reversed(range(x)):
        if j>i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(x):
        if j<i:
            print('*', end='')
    print()