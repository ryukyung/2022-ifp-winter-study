#다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 
# 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 
# 2과 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.
#실행 결과
#1
#Fizz
#3
#... (생략)
#FizzBuzz
#89
#Fizz
#91
#Fizz
#93
#Fizz
#95
#Fizz
#97
#Fizz
#Buzz
#Fizz
for i in range(1, 101):
    if i%2==0 and i%11==0:
        print('FizzBuzz')
    elif i%2==0:
        print('Fizz')
    elif i%11==0:
        print('Buzz')
    else:
        print(i)