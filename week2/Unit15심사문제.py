#Unit15
#입력받은 나이에 따라
#교통카드 잔액이 차감한뒤 출력하는 프로그램 작성
#입력 값은 7이상
age = int(input())
balance = 9000   #교통카드 잔액
if 7 <= age <= 12:
    balance = balance-650
elif 13 <= age <= 18:
    balance = balance-1050
elif 19 <= age:
    balance = balance-1250
print(balance)