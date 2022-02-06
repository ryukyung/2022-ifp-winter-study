# [65]

# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

#1번안
a, b, c = map(int, input().split())
def ifOdd(i):
    if i % 2 == 0:
        return i
    else:
        return ""
print(ifOdd(a),ifOdd(b),ifOdd(c))

#출제자 답안
a, b, c = map(int, input().split())
print( *(filter(lambda num: num%2 == 0, [a, b, c])) )
#필터와 람다를 이용하여 깔끔하게 처리하였다. 

# [66]

# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a, b, c = map(int, input().split())
print( *map(lambda num: "odd" if num % 2 == 0 else "even", [a, b, c]))
#3항 연산자를 이용하여 odd와 even을 구분하면 된다. 65번 문제의 출제자 답안을 수정하였다.



# [67]

# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

a = int(input())
print("minus" if a < 0 else "plus")
print("odd" if a % 2 == 0 else "even")


# [68]

# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

a = int(input())
if a >= 90 and a <= 100:
    print("A")
elif a >=70 and a < 90:
    print("B")
elif a >=40 and a < 70:
    print("C")
elif a >= 0 and a < 40:
    print("D")
else:
    print("잘못된 범위")


# [69]

# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")



# [70] 월이 입력될 때 계절 이름이 출력되도록 해보자.

a = int(input())
if a == 12 or a == 1 or a == 2:
    print("winter")
elif a == 3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a == 8:
    print("summer")
elif a == 9 or a == 10 or a == 11:
    print("fall")
else:
    print("what?")

