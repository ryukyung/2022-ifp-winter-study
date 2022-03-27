# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

# 입력
# 영문자 1개가 입력된다. (a ~ z)
# f

# 출력
# a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.
# a b c d e f

# Tip
# 아스키 코드를 이용하면 된다.
# ord() : 문자를 아스키 코드의 10진수로 변환 ex) 'a' >> 97
# chr() : 10진수의 아스키 코드를 문자로 변환 ex) 97 >> 'a'
# print() 함수의 두번째 파라미터인 end는 줄바꿈을 없애줄 수 있다. default값이 줄바꿈이다.

converter = ord(input())

for i in range(97, converter+1):
  print( chr(i), end=' ' )