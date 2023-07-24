# def solution(X, Y):
#     answer = '0'
#     lst = []
#     for i in range(len(x)):
#         j = 0
#         while(True):
#             if x[i] == y[j]:
#                 lst.append(int(y[j]))
#                 y = y[:j] + y[j+1:]
#             if j < len(y) - 1:
#                 j += 1
#             else:
#                 break
#     if not lst:
#         answer = '-1'
#     else:
#         lst.sort(reverse=True)
#         answer = ''.join(str(i) for i in lst)
#     return answer
from collections import Counter

x = '12321'
y = '42531'
answer = '0'
lst = []
cnt_x = Counter(x)
cnt_y = Counter(y)
# print(cnt_x)
# print(cnt_y)
for i in ('0','1','2','3','4','5','6','7','8','9'):
    if not cnt_y[i] or not cnt_x[i]:
        continue
    print('=>', i)
    print(cnt_y[i]) 
    print(cnt_x[i])
    if cnt_y[i] > cnt_x[i]:
        for j in range(cnt_x[i]):
            lst.append(i)
    elif cnt_x[i] > cnt_y[i]:
        for j in range(cnt_y[i]):
            lst.append(i)
    elif cnt_x[i] == cnt_y[i]:
        for j in range(cnt_x[i]):
            lst.append(i)


if not lst:
    answer = '-1'
else:
    lst.sort(reverse=True)
    answer = ''.join(lst)
    if int(answer) == 0:
        answer = '0'
print(answer)