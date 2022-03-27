# 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
# 콜론(:) 기호를 기준으로 두 수가 각 변수에 저장된다.
# 입력 : 3:15
# 출력 : 3:15
# 내 풀이)
hour, min = input().split(':')
print(hour+':'+min)
# 강의 풀이)
h, m = input().split(':')
print('{}:{}'.format(h, m))