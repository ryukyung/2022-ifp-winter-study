# 19.5 연습 문제 ▶ 다음 소스 코드를 완성하여 역삼각형 모양으로 별이 출력되게 만드세요.

# 결과 
# *****
#  ****
#   ***
#    **
#     *

# for i in range(5):
#     for j in range(5): 
#         ____________               
#     print()

# 정답
for i in range(5):
    for j in range(5): 
        if j < i: 
            print(' ', end='')
        else: 
            print('*', end='')              
    print()