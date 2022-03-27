# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
# 입력
# -4
# 출력
# minus
# even
# 내 풀이)
a = int(input())
print(a<0 and 'minus' or 'plus')
print(a%2 and 'odd' or 'even' )
# 강의 풀이)
num = int(input())
print( num>0 and 'plus' or 'minus' )
print( num%2 and 'odd' or 'even' )