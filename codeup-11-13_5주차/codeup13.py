# [78] 정수(1~100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
num = int(input())            # 정수 1개를 입력받음
hap = 0                       # 0으로 초기화
for i in range(2, num+1, 2):  # 짝수의 합 -> 2씩 차이
    hap += i
print(hap)                    # 짝수 전부가 아닌 합이기 때문에 for문 밖에서

# [79] 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
word = input().split()    # 공백을 기준으로 계속 입력
for i in word:
    print(i)              # 입력한 문자 출력
    if word == 'q': break # 'q'면 for문 나감

'''[80]
1,2,3,..을 계속 더해 나갈 때, 그 합이 입력한 정수(0~1000)보다
같거나 작을 때까지 계속 더하는 프로그램을 작성해보자.
즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다
같거나 커지는지 알아보고자 하는 문제이다.
'''
sum=0              # 0으로 초기화
num = int(input()) # 정수 1개 입력받음
for i in range(1, num+1): 
    sum += i
    if sum >= num: # 합이 입력받은 정수보다 크면
        print(i)   # 출력하고
        break      # 나감

# [81] 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.
n,m = map(int, input().split())
for n in range(1, n+1):       # n이 1씩 커짐
    for m in range(1, m+1):   # m도 1씩 커짐(n이 커지기 전에)
        print(n, m)           # 모든 경우

#[82] A,B,C,D,E,F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자. (단, A~F까지만 입력된다.)
string = input()
for i in range(1,16): # F가 15
    print('%sx%s=%s' %(string, hex(i)[2:].upeer(), hex(int(string, 16)*i)[2:].upper()))
# hex_16진수로 바꿔서 출력& [2:]_두번째부터 출력&upper_대문자로 출력
# int(x, 16)_x를 숫자로 바꾸는데 16진수


'''[83]
여러 사람이 순서를 정해 순서대로 수를 부르는 게임이다.
만약 3, 6, 9가 들어간 수를 자신이 불러야 하는 상황이면 "박수"를 쳐야한다.
33까지 진행했다면 "짝짝"과 같이 박수를 두번 치는 형태도 있다
'''
num1 = int(input())
print('3의 배수일 때')
for i in range(1, num1+1):
    if i%3 != 0:      # 3의 배수가 아닐 때
        count = i
        print(count, end='') 
    else:             # 3의 배수일 때
        print('짝', end='') # 짝
num2 = int(input())

print('3 6 9가 포함될 때')
for i in range(1, num2+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        count = '짝'   # 3,6,9가 들어갈 때
    else: 
        count = i      # 3,6,9가 아닐 때
    print(count, end='')


'''[84]
빨강(red) 초록(green), 파랑(blue) 빛을 섞어 여러 가지 빛의 색을 만들어 내려고 한다.
빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때(빛의 강약에 따라 0~n-1까지의 n가지의 빛 색깔을 만들 수 있다.) 
주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(rgb)과 총 가짓 수를 계산해보자.'''
r,g,b = map(int, input().split())
n = 0 
for a in range(r):
    for b in range(g):
        for c in range(b):
            print(a, b, c)
            n +=1
print(n)

'''[85]
소리가 컴퓨터에 저장될 때에는 디지털 데이터화 되어 저장된다. 
마이크를 통해 1초에 적게는 수십 번, 많게는 수만 번 소리의 강약을 체크해 그 값을 정수값으로 바꾸고 그 값을 저장해 소리를 파일로 저장할 수 있다. 
값을 저장할 때에는 비트를 사용하는 정도에 따라 세세한 녹음 정도를 결정할 수 있고 
좌우(스테리오) 채널로 저장하면 2배.... 5.1채널이면 6배의 저장공간이 필요하고 녹음 시간이 길면 그 만큼 더 많은 저장공간이 필요하다.

1초 동안 마이크로 소리강약을 체크하는 수를 h(Hz, 1초에 몇 번?체크하는가를 의미한다.)
한 번 체크한 결과를 저장하는 비트 b(2비트를 사용하면 0또는 1 두가지, 16비트를 사용하면 65536가지) 
좌우등 소리를 저장할 트랙 개수인 채널 c(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.) 
녹음할 시간 s가 주어질 때 필요한 저장 용량을 계산하는 프로그램을 작성해보자. '''
h,b,c,s = map(int, input().split())
MB = (h*b*c*s)/(8*1024**2)
print(round(MB, 1), 'MB')



'''[86]
이미지가 컴퓨터에 저장될 때에도 디지털 데이터화 되어 저장된다. 
가장 기본적인 방법으로는 그림을 구성하는 한 점(pixel, 픽셀)의 색상을 빨강(r), 초록(g), 파랑(b)의 3가지의 빛의 세기 값으로 
따로 변환하여 저장하는 것인데, 예를 들어 r, g, b 각 색에 대해서 8비트(0~255, 256가지 가능)씩을 사용한다고 하면, 
한 점의 색상은 3가지 r, g, b의 8비트+8비트+8비트로 총 24비트로 표현해서 총 2^24 가지의 서로 다른 빛의 색깔을 사용할 수 있는 것이다.

그렇게 저장하는 점을 모아 하나의 큰 이미지를 저장할 수 있게 되는데, 
1024 * 768 사이즈에 각 점에 대해 24비트로 저장하면 그 이미지를 저장하기 위한 저장 용량을 계산할 수 있다.
이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b가 주어질 때,
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해보자. '''
w,h,b = map(int, input().split())
MB = (w*h*b) /(8*1024**2)
print( round(MB, 2),'MB') # 셋재 자리에서 반올림

'''[87]
1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자. 
즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.
하지만, 이번에는 그 때의 합을 출력해야 한다. 
예를 들어 57을 입력하면 1+2+3+...+8+9+10=55에 다시 11을 더해 66이 될 때, 그 값 66이 출력되어야 한다. '''
num = int(input())
sum = 0
i = 1
while sum < num: # 입력받은 수가 크면
    sum += i
    i += 1
print(sum)


'''[88]
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.
예를 들면, 1 2 4 5 7 8 10 11 13 14 ...와 같이 출력하는 것이다. '''
num = int(input())
for i in range(1, num+1):
    if i%3 != 0:
        print(i, end='')

# [89] this 시작 값(a), 등차의 값(d), 몇 번째 수인지를 의미하는 정수(n)가 공백을 두고 입력된다. (모두 0~100)
a,d,n = map(int, input().split())
i = a
count = 0
list = []
while count < n:
    list.append(i) # 리스트에 요소 추가
    i+=d            # 시작 값에 등차를 더함
    count +=1
print(list[-1])


# [90] this 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.(모두 0~100)
a,r,n = map(int, input().split())
i = a
count = 0
list = []
while count <n:
    list.append(i)  # 리스트에 요소 추가
    i *= r          # 시작 값에 등비를 곱함
    count += 1
print(list[-1])

# [91] this 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자. (a,m,d는 -50~+50, n은 10 이하의 자연수)
a,m,d,n = map(int, input().split())
i = a
list = []
while len(list) <n:
    list.append(i)
    i = i*m +d
print(list[-1])

'''[92]
같은 날 동시에 가입한 3명의 사람들이 온라인 채점 시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
예를 들어 3명이 같은날 가입/등업하고 각각 3일마다, 7일마다, 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게된다

같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다.
(단, 입력값은 100이하의 자연수이다.) '''
a,b,c = map(int, input().split())
day = 1
while 1:
    day += 1
    if day%a == 0 and day %b == 0 and day%c == 0: break
print(day)