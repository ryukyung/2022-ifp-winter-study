''' 23. 단어를 1개 입력받는다. 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
(단, 단어의 문자(영어)를 하나씩 나누어 한 줄에 한 개씩 ' '로 묶어서 출력한다.)
입력 : 'Boy'

출력 :
'B'
'o'
'y' '''

string = input()
for i in range(len(string)):
  print("'{}'".format(string[i]))
  
# 더 간단하게
string = input()
for i in string:
	print("'{}'".format(i))