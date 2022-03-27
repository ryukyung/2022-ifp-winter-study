# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# 내 풀이)
a = int(input())
print(int(not bin(a)))
# 강의 풀이)
bitNot = ~int(input())
print( bitNot )