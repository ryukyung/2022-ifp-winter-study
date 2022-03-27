# 월이 입력될 때 계절 이름이 출력되도록 해보자.
# 예)
# [월 : 계절 이름]
# 12, 1, 2 : winter
# 3, 4, 5 : spring
# 6, 7, 8 : summer
# 9, 10, 11 : fall
# 내 풀이)
weather = int(input())
if weather == 12 or weather == 1 or weather == 2:
    print('winter')
elif weather == 3 or weather == 4 or weather == 5:
    print('spring')
elif weather == 6 or weather == 7 or weather == 8:
    print('summer')
elif weather == 9 or weather == 10 or weather == 11:
    print('fall')
# 강의 풀이)
# 1
month = int(input())
if month==12 or month==1 or month==2:
  print('winter')
elif month==3 or month==4 or month==5:
  print('spring')
elif month==6 or month==7 or month==8:
  print('summer')
else:
  print('fall')
# 2
if month in [12,1,2]:
  print('winter')
elif month in [3,4,5]:
  print('spring')
elif month in [6,7,8]:
  print('summer')
else:
  print('fall')