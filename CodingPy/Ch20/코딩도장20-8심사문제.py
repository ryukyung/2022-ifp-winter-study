# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~1000, 두 번째 입력 값의 범위는 10~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서 5의 배수일 때는 'Fizz', 7의 배수일 때는 'Buzz', 5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# ex)
# >>> 35 40
# FizzBuzz
# 36
# 37
# 38
# 39
# Fizz
# 문제 제출 코딩도장 Python
# 답안 제출 2022/01/11 18:18 경준현

FstItg, SecItg = map(int, input().split())
for i in range(FstItg, SecItg+1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)


# FstItg, SecItg = map(int, input().split())

# while True:
#     if FstItg % 5 == 0 and FstItg % 7 == 0:
#         print("FizzBuzz")
#         FstItg += 1
#         continue
#     elif FstItg % 5 == 0:
#         print("Fizz")
#         FstItg += 1
#         continue
#     elif FstItg % 7 == 0:
#         print("Buzz")
#         FstItg += 1
#         continue
#     if FstItg > SecItg :
#         break
#     print(FstItg)
#     FstItg += 1

# while로 짜면 이렇게 길어진다, 이런 짓은 어지간해서 하지 말자...

# 간단한 Fizz~ Buzz~ 문제다. 먼저 map으로 분리시키고 int로 캐스팅해 표준입력 받는다.
# 그리고 범위를 지정해주는데, 아래 while문으로 제작된 동일 코드처럼, while문으로 작성할경우 멈춰야하는 부분을 따로 제작해줘야 해 코드가 더 늘어나는 문제가 있다.
# for문, range를 이용하여 범위를 지정한다. ~부터 ~까지지만, ~까지는 직전까지를 의미하므로 +1하여준다.
# 그 이후는 전형적인 if문 예제이다. 