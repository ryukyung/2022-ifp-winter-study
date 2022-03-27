# 짝수 합 구하기
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 입력
# 정수 1개가 입력된다. (0 ~ 100)
# 5

# 출력
# 1부터 입력된 수까지 짝수의 합을 출력한다.
# 6

# Tip
# range()함수의 첫 인자를 2로하고, 
# 세 번째 인자를 2로 하면 2에서 2씩 증가하기 때문에 모든 숫자가 짝수가 된다. 
# 따라서 이를 모두 더해주면 되는 것.

num = int(input())

print('== #1 ==')
#1
answer = 0
for i in range(2, num+1, 2):
  answer += i
print(answer)

print('== #2 ==')
#2
answer2 = [i for i in range(2, num+1, 2)]
print( sum(answer2) )

print('== #3 ==')
#3
answer3 = range(2, num+1, 2)
print( sum(answer3) )