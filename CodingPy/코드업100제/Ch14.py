# [93] 이상한 출석 번호 부르기1

langList = int(input())
randNumber = list(0 for i in range(0, langList))
numberList = list(map(int, input().split()))

for i in range(0, langList):
    randNumber[i] = numberList[i]

listLangList = [0 for _ in range(23)]
for i in randNumber:
    # i는 listNumber의 배열값이고, listNumber가 1이면 lsitLangList에는 0번에 들어가야하기때문에 -1을 해준다.
    listLangList[i-1] += 1

#아스타리스크를 사용하면 배열을 뜯고 출력 가능하다.
print(*listLangList)

# [94] 이상한 출석 번호 부르기2

#출제자 답안에서 n번은 왜 조건으로 넣은 지 모르겠다, n을 쓰질 않던데?
langList = int(input())
randNumber = list(0 for i in range(0, langList))
numberList = list(map(int, input().split()))
#범위를 정하여 생성한 랜드넘버리스트와 범위를 정하지않고 입력받은 리스트 넘버리스트를 랭 리스트만큼 대입하여 랜드넘버리스트에 넣어준다.
#따라서, 지정한 범위만큼 입력받은 넘버가 들어간다.
for i in range(0, langList):
    randNumber[i] = numberList[i]

#리버스로 순서를 뒤집어준다.
numberList.reverse()
print(*numberList)

# [95] 이상한 출석 번호 부르기3

langList = int(input())
randNumber = list(0 for i in range(0, langList))
numberList = list(map(int, input().split()))

for i in range(0, langList):
    randNumber[i] = numberList[i]

print(min(randNumber))