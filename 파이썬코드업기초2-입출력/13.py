'''13. 정수(int) 2개를 입력받아 그대로 출력해보자. (단, 띄어쓰기를 기준으로 입력한다.)
입력 : 1 5
출력 : 1 5
'''
var = list(map(int, input().split()))
print(var[0], var[1])