# 10진수를 입력받아 8진수(octal)로 출력해보자.
# 내 풀이)
pal = oct(input())
print(pal)
# 강의 풀이)
octal = int(input())
print( oct(octal)[2:] )