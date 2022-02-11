#표준 입력으로 삼각형의 높이가 입력됩니다. 
# 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 출력 결과는 예제와 정확히 일치해야 합니다. 
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.
#입력
#3
#결과
#  *
# ***
#*****
#~~~~~~~풀이01~~~~~~~~~~~~~~~~~~~~~~~~~
num=int(input())
for i in range(num):
    for j in range(num+i):
        if num-i-1<=j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#~~~~~~~풀이02~~~~~~~~~~~~~~~~~~~~~~~~~

num=int(input())
for i in range(num):
    for j in reversed(range(num)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(num):
        if j < i:
            print('*', end='')
    print()
    