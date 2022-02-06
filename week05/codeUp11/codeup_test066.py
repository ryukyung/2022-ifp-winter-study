# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a, b, c = map(int, input().split())
# 1
for i in [a, b, c]:
    print('odd' if i % 2 else 'even', end=' ')

# 2
print(*map(lambda num: 'odd' if num % 2 else 'even', [a, b, c]))
