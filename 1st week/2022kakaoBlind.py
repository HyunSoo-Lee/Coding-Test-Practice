#2022 카카오 블라인드 recruitment - programmers

def solution(id_list, report, k):
    #신고자, 피신고자, 정지 리스트
    reporting = []
    reported = []
    result = []
    answer = []
    
    #중복 제거
    report_del = list(set(report))
    print(report_del)

    #신고자, 피신고자 리스트
    for i in range (len(report_del)):
        name = report_del[i].split()
        #리스트 묶음 끊기
        reporting.append(name[0])
        reported.append(name[1])
    
    print(reporting)
    print(reported)
    
    #메일 받을 사람 정리
    for id in id_list:
        cnt = reported.count(id)
        if cnt >= k:
            # reported - reporting 매칭
            for j in range (len(reported)):
                if reported[j] == id:
                    result.append(reporting[j])
    print(result)
    #id list 순서대로 메일 수 작성
    for id in id_list:
        cnt = result.count(id)
        answer.append(cnt)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
#id_list = ["con", "ryan"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
#report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

answer = solution(id_list, report, k)
print(answer)