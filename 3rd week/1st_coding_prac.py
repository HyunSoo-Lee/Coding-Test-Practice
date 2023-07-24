# def solution(k, score):
#     answer = []
#     return answer

score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
lst = []
answer = []
k = 4
min = 0
for i in range(len(score)): 
    if score[i] < min:
        score[i] = min
    lst.append(score[i])
    lst.sort()
    answer.append(lst[0])
    if len(lst) == k:
        min = lst[0]
        del lst[0]

print(answer)