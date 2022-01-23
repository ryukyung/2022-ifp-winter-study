''' 6.6 연습문제
다음 소스 코드를 완성하여 정수 세 개를 입력받고 합계가 출력되게 만드세요
'''
a,b,c = map(int, input("정수 세 개를 입력하시오 : ").split())
# 입력받은 값을 공백을 기준으로 분리
print(a+b+c)
# a+b+c값을 출력

''' 6.7 심사문제
다음 소스 코드를 완성하여 50, 100, None이 각 줄에 출력되게 만드세요
'''
a,b,c= 50,100,None
print(a)
print(b)
print(c)

''' 6.8 심사문제
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
평균 점수를 출력하는 프로그램을 만드세요
(input에서 안내 문자열은 출력하지 않아야 합니다).
단, 평균 점수를 출력할 때는 소수점 이하 자리는 벌비니다(정수로 출력).
'''
korean, english, math, science = map(int, input()).split()
print((korean+english+math+science)//4)
