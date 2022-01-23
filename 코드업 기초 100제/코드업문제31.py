# 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.
# 내 풀이)
inte = input(oct())
print(int(inte))
# 강의 풀이)
octal = '0o' + input()
print( int(octal, 8) )
