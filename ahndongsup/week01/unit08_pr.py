# ◼ 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 
# 과학은 80점 이상일 때 합격이라고 정했습니다
# (한 과목이라도 조건에 만족하지 않으면 불합격). 
# 다음 소스 코드를 완성하여 합격이면 True, 
# 불합격이면 False가 출력되게 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).

# _________
# 입력 : 90 81 86 80
# 출력 : true

# 정답
korean, english, mathematics, science = map(int, input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)