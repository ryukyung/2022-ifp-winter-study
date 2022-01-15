#Unit18
#정수 두 개를 입력받고
#첫 번째 입력 값은 두 번째 입력 값보다 항상 작다
#첫 번째 정수와 두 번째 정수 사이의 숫자 중
#3으로 끝나지 않는 숫자가 출력되게 프로그램 작성
start, stop = map(int, input().split()) 
i = start 
while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=' ')
    i += 1