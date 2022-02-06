# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# - 입력 : 문자들이 1개씩 계속해서 입력된다.
#   x b k d l q g a c

# - 출력 : 'q'가 입력될 때까지 입력된 문자를 줄을 바꿔 한 줄씩 출력한다.
#   x
#   b
#   k
#   d
#   l
#   q


aa = input().split()

# 방법 1
for a in aa:
    print(a)
    if a == 'q':
        break

# 방법 2
i = 0
while aa[i] != 'q':
    print(aa[i])
    i += 1
print(aa[i])
