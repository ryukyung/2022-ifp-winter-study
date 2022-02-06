# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

num = int(input())
print( num>0 and 'plus' or 'minus' )
print( num%2 and 'odd' or 'even' )