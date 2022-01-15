#Unit20
#정수 두 개를 입력받고
#첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서
#의 배수일 때는 'Fizz', 7의 배수일 때는 'Buzz'
#5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램 작성
start, stop = map(int, input().split())
for i in range(start, stop+1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)