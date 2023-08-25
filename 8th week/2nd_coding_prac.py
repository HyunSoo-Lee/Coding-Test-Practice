import heapq

scovillle = [10,12,1,2,3,9]
k = 7

def solution(scovillle, k):
    cnt = 0
    while min(scovillle) < k and len(scovillle) >= 2:
        heapq.heapify(scovillle)
        n = heapq.heappop(scovillle)
        m = heapq.heappop(scovillle)
        heapq.heappush(scovillle, n + (m * 2))
        cnt += 1
        if len(scovillle) == 2 and n + (m * 2) < k:
            cnt = -1
            break
    return cnt

print(solution(scovillle,k))


# 23