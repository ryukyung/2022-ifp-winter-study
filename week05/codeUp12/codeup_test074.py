# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

# 입력
# 정수 1개가 입력된다. (1 ~ 100)
# 출력
# 1씩 줄이면서 한 줄에 하나씩 1이 될 때까지 출력한다.
number = int(input())
# 1
for i in range(number, 0, -1):
    print(i)

# 2
while True:
    if number == 0:
        break
    else:
        print(number)
        number -= 1
