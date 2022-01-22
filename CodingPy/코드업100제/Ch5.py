# [38]
# 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.



firstInput, secondInput = map(int, input().split())
print(firstInput + secondInput)



# [39]
# 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.

# 실제 문제에서는 굉장히 넓은 정수 범위의 데이터형을 요구하는 문제이나 파이썬에서는 int()로 처리가 가능하다.
# 예를 들어 C에서 unsinged int보다도 크며 unsinged long과 같은 범위를 지니고 있다고 한다.
# 실제 범위

# 범위 : -9223372036854775808 ~ 9223372036854775807

# 이보다 큰 범위를 지정하고자 할 때는 long 데이터 형을 이용하면 된다.
# 파이썬에서는 4가지의 데이터형을 제공한다.
# 파이썬에서 제공하는 데이터형
# int (plain integers) : 정수
# long (long integers) : int 보다 범위가 큰 정수
# float (floating point numbers) : 실수
# complex (complex numbers) : 복소수


firstInput, secondInput = map(int, input().split())
print(firstInput + secondInput)



# [40]

# 입력된 정수의 부호를 바꿔 출력해보자.


signInt = int(input())
print(signInt * -1)

#출제자 답안 
intConv = -int(input())
print( intConv )


# [41]

# 영문자 1개를 입력받아 그 다음 문자를 출력해보자.

# 영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다.

# Tip::

# 아스키 코드를 이용하면 된다.
# 'A' == 97(1000001), 'B' == 98(1000010) 이므로 아스키 코드로 변환된 숫자에 1을 더한 뒤 아스키 문자로 재변환 해주면 된다.


inputEng = ord(input())
inputEng = inputEng + 1
print(chr(inputEng))



# [42]

# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

# Tip::

# 산술 연산자 '/'는 정확히 나눈 후의 값을 반환한다. ex) 1/3 >> 0.33333
# 산술 연산자 '//'는 나눈 후의 몫만 반환한다. ex) 1/3 >> 0


a, b = map(int, input().split())
print( a // b )



# [43]

# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.


a, b = map(int, input().split())
print( a % b )



# [44]

# 정수를 1개 입력받아 1만큼 더해 출력해보자.



inputInt = int(input())
print(inputInt + 1)



# [45]

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.

# 첫 줄에 합  
# 둘째 줄에 차,  
# 셋째 줄에 곱,  
# 넷째 줄에 몫,  
# 다섯째 줄에 나머지,  
# 여섯째 줄에 나눈 값을 순서대로 출력한다.  
# (실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)  


a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(round(a / b, 2))

# [46]

# 정수 3개를 입력받아 합과 평균을 출력해보자.

# 합과 평균을 줄을 바꿔 출력한다.
# 평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.


a, b, c = map(int, input().split())
print(a + b + c)
print(round((a + b + c) / 3, 1))


