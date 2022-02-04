# 정수 1개가 입력되었을 때,
# 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

a = int(input())
print('minus' if a < 0 else 'plus')
print('odd' if a % 2 else 'even')
