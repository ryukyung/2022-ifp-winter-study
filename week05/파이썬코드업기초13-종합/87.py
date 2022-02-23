# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.

end_point = int(input())
total = 0
i = 1
while total < end_point:
  total += i
  i += 1
print( total )