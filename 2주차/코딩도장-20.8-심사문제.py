x, y = map(int, input().split())
for i in range(x, y+1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)