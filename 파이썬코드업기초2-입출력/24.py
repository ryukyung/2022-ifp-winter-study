''' 24. 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
입력 :
75254

출력 :
[70000]
[5000]
[200]
[50]
[4] 
'''
integer = input()
count = len(integer)-1
for i in range(len(integer)):
  print([int(integer[i] + '0'*count)])
  count -= 1
  
# 더 간단하게
integer = input()
count = len(integer)-1
for i in integer:
  print([int(i + '0'*count)])
  count -= 1