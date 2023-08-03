def solution(numbers, hand):
    answer = ''
    
    Lpoint = 10
    Rpoint = 10

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            Lpoint = i
            answer += 'L'
        if i == 3 or i == 6 or i == 9:
            Rpoint = i
            answer += 'R'

        if i == 2 or i == 5 or i == 8 or i == 0:
            if i == 0: i = 11
            
            Ldistance = abs(Lpoint - i)
            Rdistance = abs(Rpoint - i)         
            
            #세로의 경우
            if Ldistance == 3:
                Ldistance = 1
            if Ldistance == 4 or Ldistance == 6:
                Ldistance = 2
            if Ldistance == 7 or Ldistance == 5 or Ldistance == 9:
                Ldistance = 3
            if i == 11:
                if Ldistance == 10 or Ldistance == 8:
                    Ldistance = 4
            if Lpoint == 10 and i == 2:
                Ldistance = 4

            if Rdistance == 3:
                Rdistance = 1
            if Rdistance == 4 or Rdistance == 6:
                Rdistance = 2
            if Rdistance == 7 or Rdistance == 5 or Rdistance == 9:
                Rdistance = 3
            if i == 11:
                if Rdistance == 10 or Rdistance == 8:
                    Rdistance = 4
            if Rpoint == 10 and i == 2:
                Rdistance = 4

            if Ldistance < Rdistance:
                Lpoint = i
                answer += 'L'
            elif Ldistance > Rdistance:
                Rpoint = i
                answer += 'R'
            else:
                if hand == "right":
                    Rpoint = i
                    answer += 'R'
                else:
                    Lpoint = i
                    answer += 'L'
        
    return answer