# 19.6 실습 문제 ▶ 표준 입력으로 삼각형의 높이가 입력됩니다. 
# 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 출력 결과는 예제와 정확히 일치해야 합니다. 
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

# 입력 : 3
# 결과
#   *
#  ***
# *****

a = int(input())  # 높이 입력
i = a-1  # 빈칸 = 높이 수-1
 
for i in range(a):  # 세로 방향
    for j in range(a + i):  # 가로 방향 
        if j < i:  
            print(' ', end = '')
        else:  
            print('*', end = '')
    print()  # 다음 줄로 넘어감
    i -= 1  # 밑으로 갈 수록 공백이 하나씩 줄어듦

    
# a = int(input())
# for i in range(a): 
#   for j in range(a-i-1): 
#     print(' ',end='') 
#   for j in range(2*i+1): 
#     print('*',end='')
#   print()