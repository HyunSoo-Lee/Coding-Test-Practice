#프로그래머스 - 연습문제 - 문자열 나누기

def solution(string):
    not_x = 0
    cnt = 0
    answer = 1
    i = 0
    while True:
        #기본 조건 : 루프문은 문자열 사이즈만큼 돌고 break
        if i == len(string): break
        #x는 첫 글자
        x = string[0]
        #x가 나온 횟수
        if string[i] == x:
            cnt += 1
            print(cnt)
        #x이외의 글자가 나온 횟수
        else:
            not_x += 1
            print(not_x)
        #두 횟수가 같아지면
        if cnt == not_x:
            #문자열 분리
            string = string[i+1:]
            print(string)
            i = 0
            #이때 주의 : 다음 분해할 문장이 없으면 빠져나가기
            if string == '':break
            #문자열의 개수가 늘어남
            answer += 1
            print(answer)
            continue
        i += 1
    return answer


string = "banana"
#string = "abracadabra"
answer = solution(string)
print(answer)

        