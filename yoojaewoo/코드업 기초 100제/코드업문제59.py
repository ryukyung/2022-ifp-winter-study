# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
# 내 풀이)
a, b = map(int, input().split())
print(a ^ b)
# 강의 풀이)
a, b = map(int, input().split())
print( a^b )

# [우리밋이 알려주는 Bonus 문제 (2-2]
# 문제 직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다. 점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요.
# 단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.
# 제한사항
# v는 세 점의 좌표가 들어있는 2차원 배열입니다.
# v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
# 좌표 값은 1 이상 10억 이하의 자연수입니다.
# 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 [x축 좌표, y축 좌표] 순으로 담아 return 해주세요.
# 입력(1)
# [[1,4], [3,4], [3,10]]
# 출력(1)
# [1,10]
# 입력(2)
# [[1,1], [2,2], [1,2]]
# 출력(2)
# [2,1]
# Tip:: 나머지 한 점의 좌표는 기존에 좌표에서 없는 좌표이니, 1번만 입력된 좌표들을 찾아서 반환해주면 된다.
#       XOR 연산을 통해 구현할 수도 있으며, 이 경우 코드의 실행 속도가 굉장히 빠르다.
# 내 풀이)
a, b ,c = [1,4], [3,4], [3,10]
d =[]
if a[0] == b[0]:
    d.append(c[0])
elif b[0] == c[0]:
    d.append(a[0])
elif c[0] == a[0]:
    d.append(b[0])
if a[1] == b[1]:
    d.append(c[1])
elif b[1] == c[1]:
    d.append(a[1])
elif c[1] == a[1]:
    d.append(b[1])
print(d)
# 강의 풀이)
coordinates = [[1,4], [3,4], [3,10]]
answer = []
for i in range(2):
  if coordinates[0][i] == coordinates[1][i]:
    answer.append(coordinates[2][i])
  elif coordinates[0][i] == coordinates[2][i]:
    answer.append(coordinates[1][i])
  elif coordinates[1][i] == coordinates[2][i]:
    answer.append(coordinates[0][i])
print( answer )

# XOR 적용
coordinates = [[1,4], [3,4], [3,10]]
result = []
result.append( coordinates[0][0] ^ coordinates[1][0] ^ coordinates[2][0] )
result.append( coordinates[0][1] ^ coordinates[1][1] ^ coordinates[2][1] )
print( result )