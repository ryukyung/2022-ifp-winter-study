a, b, c, d = map(int, input().split())
score = (a+b+c+d)//4
if 0<=a<=100 and 0<=b<=100 and 0<=c<=100 and 0<=d<=100:
    if score >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')