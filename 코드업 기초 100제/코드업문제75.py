# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 입력
# 정수 1개가 입력된다. (0 ~ 100)
# 5

# 출력
# 1부터 입력된 수까지 짝수의 합을 출력한다.
# 6

# 내 풀이)
num = int(input())
hap = 0
for i in range(2, num+1, 2):
    hap += i
    print(i)
print(hap)
# 강의 풀이)
num = int(input())
#1
answer = 0
for i in range(2, num+1, 2):
  answer += i
print(answer)

#2
answer2 = [i for i in range(2, num+1, 2)]
print( sum(answer2) )

#3
answer3 = range(2, num+1, 2)
print( sum(answer3) )