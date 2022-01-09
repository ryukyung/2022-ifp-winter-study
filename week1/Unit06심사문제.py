#Unit06
# 50, 100, None 이 출력되게 작성
#_________
#_________
#_________
#print(a)
#print(b)
#print(c)
a = 50
b = 100
c = "None"

#국어, 영어, 수학, 과학 점수를 입력받아 평균 출력하는 프로그램 작성
korean, english, mathematics, science = map(int, input().split())
print((korean + english + mathematics + science) // 4)
