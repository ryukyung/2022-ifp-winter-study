# 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.
# 입력 :
# 1.435867

# 출력 :
# 1
# 435867
num = input().split('.')
print(num[0], num[1], sep='\n')
# print("{}\n{}".format(num[0],num[1]))
