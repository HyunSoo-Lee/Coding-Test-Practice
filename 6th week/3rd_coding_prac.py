def solution(k, tangerine):
    answer = 0
    cnt = {}

    for i in range(len(tangerine)):
        if i >= 1:
            if not tangerine[i] in cnt.keys():
                cnt.setdefault(tangerine[i], tangerine.count(tangerine[i]))
        else:
            cnt.setdefault(tangerine[i], tangerine.count(tangerine[i]))

    selling = list(cnt.values())
    selling.sort(reverse=True)
    for i in range(len(selling)):
        if k <= selling[i]:
            answer = i+1
            break
        else:
            k -= selling[i]
    return answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

print(solution(k, tangerine))
