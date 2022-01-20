'''
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
입력 :
75254
출력 :
[70000]
[5000]
[200]
[50]
[4]
'''
x = input()
count = len(x)-1
for i in range(len(x)):
  print([int(x[i] + '0'*count)])
  count -= 1