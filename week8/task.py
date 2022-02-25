#서울에서 김서방 찾기
#String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아,
#"김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
#seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
#
#
#index()로 리스트 내 특정 값의 주소를 확인
#format()으로 string내 변수 값을 넣을 수 있다
def solution(seoul):
    answer = '김서방은 {}에 있다'.format(seoul.index("Kim"))    
    return answer

#정수 num이 짝수일 경우 "Even"을 반환하고
#홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
def solution(num):
    if num % 2 == 0:
        answer = 'Even'
    elif num % 2 == 1:    #else: 로 바꾸면 좀 더 깔끔
        answer = 'Odd'
    return answer

#대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
#s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,
#다르면 False를 return 하는 solution를 완성하세요.
#'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
#단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
#
#
#lower() 함수로 문자열을 모두 소문자로 바꾼 뒤,
#count() 집계함수로 p와 y의 개수를 세서 비교한다.
#T/F 판별까지 된다.
def solution(s):
    return s.lower().count('p') == s.lower().count('y')