def solution(s):
    pCount = s.count('p')
    PCount = s.count('P')
    yCount = s.count('y')
    YCount = s.count('Y')
    
    pCount += PCount
    yCount += YCount
    
    if pCount == yCount:
        answer = True
    else:
        answer = False
    
    return answer