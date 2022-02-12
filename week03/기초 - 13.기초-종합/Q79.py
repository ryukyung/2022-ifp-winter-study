# 원하는 문자가 입력될 때까지 반복 출력하기
# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

# 입력
# 문자들이 1개씩 계속해서 입력된다.
# x b k d l q g a c

# 출력
# 'q'가 입력될 때까지 입력된 문자를 줄을 바꿔 한 줄씩 출력한다.
# x
# b
# k
# d
# l
# q

# Tip
# 입력값이 공백을 기준으로 한 번에 입력되기 때문에 input()을 매번 호출할 필요가 없다.
# 입력된 문자열의 길이만큼만 반복하여 출력하면 되기에 for()문을 사용해도 된다.

word = input().split()

print('== #1 ==')
#1
for w in word:
  print(w)
  if w == 'q': break

print('== #2 ==')
#2
i = 0
while word[i] != 'q':
  print(word[i])
  i += 1
print(word[i])