# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

word = input().split()

#1
for w in word:
  print(w)
  if w == 'q': break

#2
i = 0
while word[i] != 'q':
  print(word[i])
  i += 1
print(word[i])