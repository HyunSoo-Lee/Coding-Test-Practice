def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            absolutes[i] = absolutes[i] * (1)
        else:
            absolutes[i] = absolutes[i] * (-1)
    return sum(absolutes)

absolutes = [1,2,3]
signs = [False,False,True]

print(solution(absolutes, signs))