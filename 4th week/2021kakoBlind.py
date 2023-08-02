def solution(s):
    dict = {
        '0' : 'zero',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine',
    }

    for key, val in dict.items():
        if s.find(val) != -1:
            s = s.replace(val, key)
    
    answer = int(s)
    
    return answer

s = 'one4seveneight'

print(solution(s))