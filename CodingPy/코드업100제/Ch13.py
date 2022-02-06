# [78] 짝수 합 구하기

# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.


intInput = int(input())
countNum = 0
for i in range(2, intInput, 2):
    countNum = i + countNum
print(countNum)


# [79] 원하는 문자가 입력될 때까지 반복 출력하기

# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.


listChar = list(input().split())
for i in listChar:
    if i == "q":
        break
    else:
        print(i)


# [80] 언제까지 더해야 할까?

# 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지 계속 더하는 프로그램을 작성해보자.

# 즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.


intInput = int(input())
i = 1
count = 1
while(1):
    count += i
    if intInput > count:
        i += 1
    else:
        print(i)
        break


# [81] 주사위를 2개 던지면?

# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.

# 입력
# 주사위 2개의 면의 개수 n, m이 공백을 두고 입력된다.
# 단, n, m은 10이하의 자연수


n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, end=" ")
        print(j)


# [82] 16진수 구구단

# 16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운 영일(01)이는 16진수끼리 곱하는 16진수 구구단에 대해서 궁금해졌다.

# A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)


#출제자 답안
char = input()

for i in range(1, 16):
  print( '%s*%s=%s' %(char, hex(i)[2:].upper(), hex(int(char, 16) * i)[2:].upper()) )
#%s를 사용해서 print문 한개에 집어넣은 형태가 흥미롭다..


# [83] 3 6 9 게임의 왕이 되자

# 3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.


intInput = int(input())
for i in range(1, intInput+1):
    if i % 3: 
        count = i 
    else:
        count = "X"
    print(count, end=' ')


# [84] 빛 섞어 색 만들기

# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 빛의 색을 만들어 내려고 한다.

# 빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때,
# (빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다.)

# 주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과 총 가짓 수를 계산해보자.



r, g, b = map(int, input().split())
count = 0
for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
            count += 1
print(count)


# [85] 소리 파일 저장용량 계산하기


#출제자 답안
h, b, c, s = map(int, input().split())

result = h*b*c*s
resultMB = result / (8 * 1024**2)
print(round(resultMB, 1), 'MB')
#문제를 이해하지 못하였음.?????????


# [86] 그림 파일 저장용량 계산하기


#출제자답안
w, h, b = map(int, input().split())
result = (w*h*b) / (8 * 1024**2)
print( round(result, 2), 'MB' )
#뭔뜻인지, 동영상보고 이해하겠음....


# [87] 여기까지! 이제 그만~

# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.


intInput = int(input())
i = 1
count = 0
while(1):
    count += i
    if intInput > count:
        i += 1
    else:
        print(count)
        break



# [88] 3의 배수는 통과?

# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.


intInput = int(input())
for i in range(1, intInput+1):
    if i % 3: 
        count = i 
    else:
        continue
    print(count, end=' ')
#3의 배수 3 6 9 코드를 손봤다.


# [89] 수 나열하기1


a, d, n = map(int, input().split())
count = 1
while(1):
    if n > count:
        a += d
        count += 1
    else:
        break
print(a)




# [90] 수 나열하기2


a, d, n = map(int, input().split())
count = 1
while(1):
    if n > count:
        a *= d
        count += 1
    else:
        break
print(a)


# [91] 수 나열하기3


a, m, d, n = map(int, input().split())
count = 1
while(1):
    if n > count:
        a *= m
        a += d
        count += 1
    else:
        break
print(a)


# [92] 함께 문제 푸는 날


a, b, c = map(int, input().split())
date = 1
while(1):
    if date % a == 0 and date % b == 0 and date % c == 0:
        print(date)
        break
    date += 1

