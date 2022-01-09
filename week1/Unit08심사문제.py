#Unit08
#입력받은 점수가
#국어는 90점이상, 영어는 80점초과, 수학은 85점초과, 과학은 80점이상
#일 때 합격(한 과목이라도 조건에 만족하지 않으면 불합격)이며
#합격이면 True, 불합격이면 False가 출력되게 작성
korean, english, mathematics, science = map(int, input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)
