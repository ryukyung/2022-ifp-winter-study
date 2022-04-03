'''문자열 내 p와 y의 개수
대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 
다르면 False를 return 하는 solution를 완성하세요.
'p','y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
예를 들어 s가 "pPooogY"면 true를 return하고 "Pyy"라면 false를 return합니다.
제한 사항
 - 문자열 s의 길이 : 50 이하의 자연수
 - 문자열 s는 알파벳으로만 이루어져 있습니다.
입출력 예
    s     | answer  | 설명
"pPoooyY" | true    | p의 개수와 y의 개수가 2로 같아 true 
   "Pyy"  | flase   | p의 개수와 y의 개수가 1,2로 달라 false
'''
def solution(s):
    p=0                                # 0으로 초기화
    y=0                                # 0으로 초기화
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P': # p, P일 때
            p+=1                       # p+1
        if s[i] == 'y' or s[i] == 'Y': # y, Y일 때  
            y+=1                       # y+1
        if p == y:                     # p의 개수와 y의 개수가 같을 때  
            answer = True              # true
        else:                          # p의 개수와 y의 개수가 다를 때
            answer = False             # false  
    return answer