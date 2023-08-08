# 49점따리
# def solution(n,k,enemy):
#     #기본적으로 푸는 법
#     answer = k
#     enemy.sort(reverse=True)
#     #print(enemy)
#     while True:
#         #print(n, enemy[k], answer)
#         if k == len(enemy) or n < enemy[k]:
#             break
#         if k == len(enemy) - 1 and n > enemy[-1]:
#             answer += 1
#             break
#         n = n - enemy[k]
#         answer += 1
#         k += 1
#     #print(answer)
#     return answer



def solution(n,k,enemy):
    answer = 0
    # 무적권 없이

    while n >= 0:
        print('killed enemy :', answer, n)
        n = n-enemy[answer]
        answer += 1
    
    # 무적권 사용
    skill = enemy[:answer]
    skill.sort(reverse = True)
    print('remain enemy : ', skill, n)
    if len(skill) >= k:
        for i in range(k):
            print('for', i)
            n += skill[i]
        print(n)
    return answer

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

print(solution(n,k,enemy))