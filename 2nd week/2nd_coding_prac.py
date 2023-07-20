import math
def solution(number, limit, power):
    answer = 0
    for num in range(number):
        divisor = 0
        num += 1

        #약수 구하는 코드
        for j in range(int(math.sqrt(num))):
            if (num%(j+1)) == 0:
                if j+1 != math.sqrt(num):
                    divisor += 2    
                else:
                    divisor += 1
            
            if divisor > limit:
                divisor = power
                break
        
        #답안에 합산하기
        answer += divisor
    return answer

print(solution(5,3,2))