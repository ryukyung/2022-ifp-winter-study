# 짝수 합 구하기

# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 입력
# 정수 1개가 입력된다. (0 ~ 100)

# 출력
# 1부터 입력된 수까지 짝수의 합을 출력한다.

num = int(input())

# 1
total1 = 0
for i in range(2, num+1, 2):
    total1 += i
print(total1)

# 2
total2 = [i for i in range(2, num+1, 2)]
print(sum(total2))

# 3
total3 = range(2, num+1, 2)
print(sum(total3))

# 4
n = num//2
total4 = (1+n)*n  # (2+2*n)*n/2
print(int(total4))
