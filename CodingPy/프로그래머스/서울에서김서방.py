seoul = ["Jane", "Kim"]

#답안 1
def solution(seoul):
    count = 0
    for i in seoul:
        if i == "Kim":
            answer = "김서방은 "+str(count)+"에 있다"
        else:
            count += 1
    return answer

#답안 2
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 "+str(i)+"에 있다"
        else:
            pass
    return answer

print(solution(seoul))