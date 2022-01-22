# [10]
# 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.

intVar = int(input())
print(intVar)


# [11]
# 문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력해보자.

# Tip::

# input()의 반환값은 기본으로 문자열로 정의된다.


charVar = input()
print(charVar)
#기본값 



# [12]
# 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력해보자.



floatVar = float(input())
print(floatVar)



# [13]
# 정수(int) 2개를 입력받아 그대로 출력해보자. (단, 띄어쓰기를 기준으로 입력한다.)
# 입력 : 1 5
# 출력 : 1 5

# Tip::

# 문자열의 메소드(함수)인 split()을 이용하면 문자열을 공백 기준으로 배열(iterable)로 만들어준다.
# 매핑함수인 map()을 이용하면 배열(iterable)의 모든 원소를 첫 번째 매개변수(parameter)로 변환할 수 있다. 정확히는 감싸준다는 표현이 맞다.
# 예 ) map(int, ['1', '2', '3']) >> [1,2,3]
# 매핑함수 map()의 반환값은 map객체이다. 따라서 육안으로 확인하기 위해서는 list()로 변환시켜줘야한다.


#1번답안
mapIntVar = list(map(int, input().split()))
print(mapIntVar[0], mapIntVar[1])
#변수를 두개 할당하지않고, 리스트에 담아서 출력하였다.

#2번답안
firstMapVar, secondMapVar = map(int, input().split())
print(firstMapVar, secondMapVar)
#번수를 두개 할당하여 스플릿된 값을 각각 배정받았다.


# [14]
# 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.

# 아스키 코드란?

# 컴퓨터가 문자를 읽을 수 있도록 문자에 대응하는 숫자들이 존재한다.
# 예 ) A => 1100001
# 이때의 문자가 '아스키 문자'이며, 숫자가 '아스키 코드'이다.


#문제의 의도가 문자의 위치를 바꾸는 것이므로, map을 사용할 필요가 없다.
mapCharVar = input().split()
print(mapCharVar[1], mapCharVar[0])



# [15]
# 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.

# Tip::

# 반올림 함수 round()를 이용하면 된다.


mapFloatVar = round(float(input()),2)
print(mapFloatVar)
#input , 몇번째 자리까지 출력할건지.



# [16]
# int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력해보자.



threeIntVar = int(input())
for i in range(1,4):
    print(threeIntVar, end=" ")
#for문으로 범위를 지정하였다, 1~3까지. 이후, print()문을 출력할때, end=" "를 이용하여 개행이 아닌 공백으로 처리하였다.



# [17]
# 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
# 콜론(:) 기호를 기준으로 두 수가 각 변수에 저장된다.

# 입력 : 3:15
# 출력 : 3:15

# Tip::

# split()의 매개변수로 문자열을 분할하기 위한 기준을 정의할 수 있다.
# 문자열의 메소드(함수)인 format()을 이용하면 문자열 내부에 변수값을 대입할 수 있다.

#답안
hour, minute = map(int, input().split(':'))
print(hour, ':', minute)

#출제자 답안
h, m = input().split(':')
print('{}:{}'.format(h, m))
#포멧함수를 이용하여 처리하였다.

# [18]
# 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

# 입력
# 연, 월, 일이 ".(닷)"으로 구분되어 입력된다.
# 출력
# 입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다.

# 입력 : 2020.2.9
# 출력 : 2020.02.09
# (단, m 혹은 d가 한 자리 수인 경우 앞에 0을 붙여 출력한다.)

year, month, day = map(int, input().split("."))
if month <= 9:
    month = "0" + str(month)
if day <= 9:
    day = "0" + str(day)
print("{}.{}.{}".format(year, month, day))
#if문을 이용하여 조건식을 작성하고, 포멧함수를 이용하여 출력하였다.



# [19]
# 주민번호는 다음과 같이 구성된다.

# XXXXXX-XXXXXXX

# 앞의 6자리는 생년월일(yymmdd)이고 뒤 7자리는 성별, 지역, 오류검출코드이다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.

# 입력
# 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력된다. (입력값은 가상의 주민번호이다.) ex)110011-0000000
# 출력
# '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

# 입력 : 000907-1121112
# 출력 : 0009071121112



socialNumber = list(input().split("-"))
print("{}{}".format(socialNumber[0], socialNumber[1]))
#문자열로 받아서 리스트로 나눠 출력



# [20]
# 1개의 문자열을 입력받아 그대로 출력해보자.



stringVar = input()
print(stringVar)



# [22]
# 공백이 포함되어 있는 한 문장이 입력된다. 단, 입력되는 문장은 여러 개의 단어로 구성되고, 엔터로 끝난다.



stringVar = input()
print(stringVar)



# [23]
# 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.

# 입력 :
# 1.435867

# 출력 :
# 1
# 435867



devideFloatVar = input().split(".")
print(devideFloatVar[0])
print(devideFloatVar[1])



# [24]
# 단어를 1개 입력받는다.
# 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력한다.
# (단, 단어의 문자(영어)를 하나씩 나누어 한 줄에 한 개씩 ' '로 묶어서 출력한다.)

# 입력 :
# 'Boy'

# 출력 :
# 'B'
# 'o'
# 'y'

# Tip::

# str도 List와 동일하게 배열과 같은 형식으로 접근가능하다. 문자열도 리스트와 같이 iterable 객체이기 때문이다.
# ex) '문자열'[0] >> '문'
# 반복문 for()를 이용하여 문자열의 길이만큼 반복한다.


strVar = input()
for i in range(len(strVar)):
    print("'{}'".format(strVar[i]))


# [25]
# 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

# 입력 :
# 75254

# 출력 :
# [70000]
# [5000]
# [200]
# [50]
# [4]

# Tip::

# 문자열 연산이 가능함을 잊지 말자.
# ex) '문자'*5 >> '문자문자문자문자문자'


numberDevide = input()
for i in range(len(numberDevide)):
    count = "0" * (len(numberDevide) - (i + 1))
    print("[{}]".format(numberDevide[i] + count))


# [26]
# 입력되는 시:분:초 에서 분만 출력해보자.


inputTime = list(input().split(":"))
print(inputTime[1])





# [27]
# 년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.

# 년월일(yyyy.mm.dd)를 입력받아,

# 일월년(dd-mm-yyyy)로 출력해보자.

# (단, 한 자리 일/월은 0을 붙여 두자리로 출력한다.)

# Tip::

# 조건문 if-else문을 파이썬의 3항 연산자(Chapter 10 참고) 기능을 이용하면 더 간단하게 작성할 수 있다. 이렇게 작성하는 것이 메모리 효율성면에서도 효과적이다. (18번 참고)



inputDateTime = list(input().split("."))
inputDateTime[2] = "0" + inputDateTime[2] if len(inputDateTime[2]) == 1 else inputDateTime[2]
inputDateTime[1] = "0" + inputDateTime[1] if len(inputDateTime[1]) == 1 else inputDateTime[1]
print("{}-{}-{}".format(inputDateTime[2], inputDateTime[1], inputDateTime[0]))


