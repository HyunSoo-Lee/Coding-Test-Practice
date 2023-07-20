#프로그래머스 - 연습문제 - 햄버거

def solution(ingredient):
    answer = 0
    while True:
        string = ''.join(map(str, ingredient))
        loc = string.find('1231')
        if loc != -1:
            del ingredient[loc:loc + 4]
            answer += 1
        else:
            break
    return answer

#ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
answer = solution(ingredient)
print(answer)