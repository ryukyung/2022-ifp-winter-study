# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# - 입력 : 정수 1개가 입력된다. (0 ~ 100)
#   5

# - 출력 : 1부터 입력된 수까지 짝수의 합을 출력한다.
#   6


num = int(input())

# 방법 1
hap = 0
for i in range(2, num + 1, 2):
    hap += i
print(hap)

# 방법 2
hap = [i for i in range(2, num + 1, 2)]
print(sum(hap))

# 방법 3
hap = range(2, num + 1, 2)
print(sum(hap))
