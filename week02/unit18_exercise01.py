#다음 소스 코드를 완성하여 0과 73 사이의 숫자 중 3으로 끝나는 숫자만 출력되게 만드세요.
#실행 결과
#3 13 23 33 43 53 63 73
i = 0
while True:
    if i>73:
        break
    if i%10 != 3:
        continue              
    print(i, end=' ')
    i += 1