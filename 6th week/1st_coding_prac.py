def solution(n, lost, reserve):
    #lost와 reserve에 동시에 있는 사람 삭제
    n_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            n_lost.append(i)
    lost = n_lost

    #소팅 및 필요한 변수 설정, 전체 학생 수 lost 학생 수만큼 감소
    lost.sort()
    reserve.sort()
    psb = []
    n -= len(lost)

    #체육복 대여가 가능한 케이스 조사 및 가능한 경우 전체 학생 수 하나씩 증가
    for i in range(len(reserve)):
        psb.append(reserve[i] - 1)
        psb.append(reserve[i] + 1)
        #print(psb)
        for p in range(2):
            if psb[p] in lost:
                #print(psb[p])
                lost.remove(psb[p])
                n+=1
                break
        psb.clear()
    
    answer = n
    return answer

n = 5
lost = [2, 3, 5]
reserve = [2, 3, 4]
print(solution(n, lost, reserve))


#1, 3, 5, 24