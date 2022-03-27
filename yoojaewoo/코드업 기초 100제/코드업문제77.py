# 언제까지 더해야 할까?
# 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지 계속 더하는 프로그램을 작성해보자.
# 즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.

# 입력
# 정수 1개가 입력된다.
# 55

# 출력
# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가, 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.
# 10

# 내 풀이)
end = int(input())
hap = 0
i = 0
while hap < end:
    i += 1
    hap += i
print(i)
# 강의 풀이)
end_point = int(input())
#1
total = 0
i = 0
while total < end_point:
  i += 1
  total += i
print( i )
#2
total = 0
for i in range(1, end_point+1):
  total += i
  if total >= end_point:
    print( i )
    break