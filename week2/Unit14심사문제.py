#Unit14
#국어, 영어, 수학, 과학 점수를 입력받고
#네 과목 평균 점수가 80점 이상일 때 합격
#평균 점수에 따라 '합격', '불합격'을 출력하는 프로그램 작성
#점수가 0점에서 100점까지만 입력 받을 수 있으며
#범위를 벗어나면 '잘못된 점수'를 출력하고
#합격, 불합격 여부를 출력하지 않는다
korean, english, mathematics, science = map(int, input().split())
if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathematics <= 100 and 0 <= science <= 100:
    if (korean + english + mathematics + science) / 4 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')