#Unit13
#가격(정수)과 쿠폰 이름을 입력받고
#쿠폰에 따라 할인된 가격을 출력하는 프로그램 작성
#Cash3000 쿠폰은 3000원, Cash5000 쿠폰은 5000원
price = int(input())
coupon = input()
if coupon == 'Cash3000':
    price -= 3000
if coupon == 'Cash5000':
    price -= 5000
print(price)