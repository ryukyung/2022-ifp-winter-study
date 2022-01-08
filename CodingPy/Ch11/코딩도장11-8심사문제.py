# 표준 입력으로 숫자 또는 문자열 여러 개가 입력되어 리스트 x에 저장됩니다(입력되는 숫자 또는 문자열의 개수는 정해져 있지 않음). 
# 다음 소스 코드를 완성하여 리스트 x의 마지막 요소 5개를 삭제한 뒤 튜플로 출력되게 만드세요.
# ex)
# >>> 1 2 3 4 5 6 7 8 9 10
# ('1', '2', '3', '4', '5')
# >>> oven bat pony total leak wreck curl crop space navy loss knee
# ('oven', 'bat', 'pony', 'total', 'leak', 'wreck', 'curl')
# 문제 제출 코딩도장 Python
# 답안 제출 2022/01/05 17:55 경준현

x = input().split()
del x[-5:]
print(tuple(x))

# del x[-5:]로 마지막 요소 5개를 삭제한 후, tuple로 출력함.