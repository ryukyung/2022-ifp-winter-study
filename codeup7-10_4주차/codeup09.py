# [59] 입력된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
a = ~ int(input())
print(a)
 
# [60] 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
a, b = map(int, input().split())
print( a&b )

# [우리밋이 알려주는 Bonus 문제2] 1개의 정수형 입력이 들어오면 비트 연산을 이용하여 '홀수'와 '짝수'를 판별하여라.
num = int(input())
print(['짝수','홀수'][num & 1])

# [61] 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
a, b = map(int, input().split())
print( a|b )

# [62] 입력된 정수 두 개를 비트 단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
a, b = map(int, input().split())
print( a^b )

'''[우리밋이 알려주는 Bonus 문제 2-2]
직사각형을 만드는데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다.
점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 
직사각형을 만드는데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요. 
단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 겨우만 입력으로 주어집니다
 - v는 세 점의 좌표가 들어있는 2차원 배열입니다
 - v의 각 원소는 점의 좌표를 나타내며 좌표는 [x축 좌표, y축 좌표]순으로 주어집니다
 - 좌표 값은 1이상 10억 이하의 자연수입니다.
 - 직사각형을 만드는데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요
'''
# 기본 풀이
coordinates = [[1,4],[3,4],[3,10]]                    # 입력받은 값
answer= []                                            # 리스트 생성
for i in range(2):                                    # (x,y)라 2번 해야함
    if coordinates[0][i] == coordinates[1][i]:        # (1,4)와 (3,4)에서 x(y)좌표가 같으면
        answer.append(coordinates[2][1])              # answer에 들어갈 좌표값은 (3,10)에서의 x(y)좌표임
    elif coordinates[0][i] == coordinates[2][i]:      # (1,4)와 (3,10)에서 x(y)좌표가 같으면
        answer.append(coordinates[1][i])              # answer에 들어갈 좌표값은 (3,4)에서의 x(y)좌표임
    elif coordinates[1][i] == coordinates[2][i]:      # (3,4)와 (3,10)에서 x(y)좌표가 같으면
        answer.append(coordinates[0][i])              # answer에 들어갈 좌표값은 (1,4)에서의 x(y)좌표임
print(answer)
# XOR 사용
coordinates = [[1,4],[3,4],[3,10]]
result = []
result.append( coordinates[0][0] ^ coordinates[1][0] ^ coordinates[2][0]) # x축끼리 xor
result.append( coordinates[0][1] ^ coordinates[1][1] ^ coordinates[2][1]) # y축끼리 xor
print(result)
