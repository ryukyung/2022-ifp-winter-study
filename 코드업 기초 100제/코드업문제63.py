# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
# 내 풀이)
a, b, c = map(int, input().split())
print('even', *(filter(lambda x: not x%2, [a, b, c])))
print('odd', *(filter(lambda x: x%2, [a, b, c])))
# 강의 풀이)
# 1
a, b, c = map(int, input().split())
print( 'odd' if a%2 else 'even' )
print( b%2 and 'odd' or 'even' )
print( ['even', 'odd'][c%2] )
#2
a, b, c = map(int, input().split())
print( *map(lambda num: 'odd' if num%2 else 'even', [a, b, c]) )