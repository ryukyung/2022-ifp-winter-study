# ◼ 다음 소스 코드를 완성하여 튜플 n에서 인덱스가 홀수인 요소들이 출력되게 만드세요.

# n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2

# print(________)
# 결과 : (75, -10, 32, -15, 76, 2)

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2

# 정답 
print(n[1::2])
print(n[1:12:2])
print(n[1:len(n):2])