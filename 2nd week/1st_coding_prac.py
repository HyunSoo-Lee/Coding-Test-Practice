def solution(lottos, win_nums):
    score = {
        6 : 1,
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }

    answer = []
    potential = 0
    origin = 0
    for i in range(6):
        if lottos[i] == 0:
            potential += 1
        for j in range(6):
            if lottos[i] == win_nums[j]:
                origin += 1
    answer.append(score[potential+origin])
    answer.append(score[origin])
    return answer

lottos = [45, 4, 35, 20, 3, 9]	
win_nums = [20, 9, 3, 45, 4, 35]

answer = solution(lottos, win_nums)

print(answer)