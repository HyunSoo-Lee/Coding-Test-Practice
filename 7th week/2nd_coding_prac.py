import math

def solution(progresses, speeds):
    answer = []
    remain_days = []
    for i in range(len(progresses)):
        remain_percent = 100 - progresses[i]
        remain_days.append(math.ceil(remain_percent/speeds[i]))
    # print(remain_days)
    biggest = remain_days[0]
    lst_start = 0
    for i in range(len(remain_days)+1):
        lst = remain_days[lst_start:i]
        if lst:
            # print(i, len(remain_days), max(lst), biggest)
            # print(lst, 'max :', biggest)
            # print('-----------')
            if max(lst) > biggest:
                # print('===============')
                # print(lst)
                # print('===============')
                lst_start = i - 1
                biggest = max(lst)
                answer.append(len(lst) - 1)
            if i == len(remain_days):
                lst = remain_days[lst_start:i]
                # print('end', lst, lst_start)
                answer.append(len(lst))
    return answer

print(solution(	[93, 30, 55], [1, 30, 5]))
print('++++++++++++++++')
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([1, 1, 50],[100, 2, 1]))

#최대값이 나오면
#최대값 이전까지의 길이를
#answer에 append
#최대값부터 다시 리스트 시작
