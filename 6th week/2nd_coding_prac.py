def repeat(x):
    global string
    if x//3 == 0:
        string += str(x%3)
    else : 
        if x % 3 == 0:
            string += '4'
            repeat(x//3 - 1)
        else:
            string += str(x%3)
            repeat(x//3)
    return string

def solution(n):
    answer = repeat(n)[::-1]
    #print(string)
    while True:
        if answer[0] == '0':
            answer = answer[1:]
        else: break
    return answer

string = ''