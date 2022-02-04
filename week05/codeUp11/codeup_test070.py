# 월이 입력될 때 계절 이름이 출력되도록 해보자.
month = int(input())
# 1
if month == 12 or month == 1 or month == 2:
    print('winter')
elif month == 3 or month == 4 or month == 5:
    print('spring')
elif month == 6 or month == 7 or month == 8:
    print('summer')
else:
    print('fall')

# 2
if month in [12, 1, 2]:
    print('winter')
elif month in [3, 4, 5]:
    print('spring')
elif month in [6, 7, 8]:
    print('summer')
else:
    print('fall')
