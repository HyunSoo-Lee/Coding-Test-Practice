def solution(survey, choices):
    type = {
        'R': 0,
        'T': 0, 
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0 
    }
    
    answer = ''
    point = []

    #설문조사 결과를 점수로 치환
    for i in range(len(choices)):
        score = 4-choices[i]
        point.append(score)
        #점수가 음수인 경우 -> 동의인 경우들
        if score <= 0:
            #두번째 글자에 해당하는 타입에 점수 플러스
            type[survey[i][1]] += abs(score)
        #점수가 양수인 경우 -> 비동의인 경우들
        else:
            #첫번째 글자에 해당하는 타입에 점수 플러스
            type[survey[i][0]] += abs(score)
    print(point)
    val = list(type.values())
    print(type)
    print(val)
    for i in (0,2,4,6):
        if val[i] > val[i+1]:
            answer += list(type.keys())[i]
        elif val[i] < val[i+1]:
            answer += list(type.keys())[i+1]
        elif val[i] == val[i+1]:
            answer += list(type.keys())[i]
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(choices)
answer = solution(survey, choices)
print(answer)