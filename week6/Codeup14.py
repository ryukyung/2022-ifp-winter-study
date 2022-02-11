#93
#출석 번호를 n번 무작위로 불렀을 때,
#각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
a = int(input())
b = map(int, input().split())
LIST = [0 for _ in range(23)]  #0~22번까지 0으로 채움
for c in b:
    LIST[c-1] += 1  #주소값의 값을 +1 해준다
print(*LIST)  #내부의 원소를 그대로 출력하길 요구해서 *(Asterisk) 사용

#94
#출석 번호를 n번 무작위로 불렀을 때,
#부른 번호를 거꾸로 출력해 보자.
a = int(input())
b = list(map(int, input().split()))
b.reverse()    #리스트의 메소드인 reverse() 이용
print(*b)

#95
#출석 번호를 n번 무작위로 불렀을 때,
#가장 빠른 번호를 출력해 보자.
a = int(input())
b = map(int, input().split())
print(min(b))   #배열 객체의 원소 중 가장 작은 값을 반환해주는 min() 함수 이용