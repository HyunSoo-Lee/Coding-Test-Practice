def solution(k,m,score):
    
    answer = 0
    devide = []

    score.sort(reverse=True)
    for i in range(0, len(score), m):
        devide.append(score[i:i+m])

    for i in range(len(devide)):
        if len(devide[i]) == m:
            answer += min(devide[i])*m

    return answer

score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	
k = 4
m = 3

print(solution(k,m,score))