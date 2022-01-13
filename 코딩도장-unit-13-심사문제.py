price = int(input())
coupon = input()
if coupon == 'Cash3000':
    price = price-3000
if coupon == 'Cash5000':
    price = price-5000
print(price)