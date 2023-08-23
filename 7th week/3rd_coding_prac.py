<<<<<<< HEAD
import math

# 시간 계산기
def fee_cal(arr, fees):
    time = 0
    fee = 0
    # 애초에 반복문을 두칸씩 뛰게 함 -> IN만 가리키게 되어있다.
    for i in range(0, len(arr), 2):
        # IN 시간과 OUT 시간 차이 계산
        if i != len(arr) - 1:
            h = abs(int(arr[i][0].split(':')[0]) - int(arr[i+1][0].split(':')[0])) 
            if arr[i][0].split(':')[1] == '00':
                m = int(arr[i+1][0].split(':')[1])
            else : m = 60 - int(arr[i][0].split(':')[1]) + int(arr[i+1][0].split(':')[1])
            if h != 0 and m != 0:
                h -= 1
            time += h*60 + m
        # 마지막이 가리켜지는 경우 -> IN으로 끝나는 케이스
        if i == len(arr) - 1 or len(arr) == 1:
            h = 23 - int(arr[i][0].split(':')[0])
            m = 59 - int(arr[i][0].split(':')[1])
            time += abs(h*60) + abs(m)
    print(time)
    if time <= fees[0]:
        fee = fees[1]
    else:
        fee = fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3]
    return fee

def solution(fees, records):
    # 정보 담은 2차원 리스트
    record_splt = []

    # 자동차 번호 -> 누적 주차 시간 계산중 필요한 변수
    car_num = 0

    # 번호에 따른 입/출차 기록을 따로 저장해두는 '임시 리스트'
    car_timestamp = []

    # 결과
    result = []

    # [시간, 번호, 출입] 형태의 2차원 리스트로 변환
    for i in range(len(records)):
        record_splt.append(records[i].split())
    record_splt.sort(key = lambda record_splt: record_splt[1])
    print(record_splt)
    print('------------')

    # 차 번호별로 누적 주차 시간 계산해서 fees 리스트에 저장 -> 시간당 요금으로 변환
    for i in range(len(record_splt)):
        # car_num 변수에 차 번호 저장, 새 번호 나오면 '임시 리스트' 초기화 후 result 한칸 넘김
        # 차 번호별로 시간을 나누어 저장하게 해주자
        if record_splt[i][1] != car_num:
            car_num = record_splt[i][1] # 차 번호 인덱스
            print(car_timestamp)
            result.append(fee_cal(car_timestamp, fees))
            car_timestamp.clear() # '임시 리스트' 초기화
        car_timestamp.append(record_splt[i])
    result.pop(0)
    print(car_timestamp)
    result.append(fee_cal(car_timestamp, fees))
    return result


fees = 	[1, 10, 1, 11]
records = ["00:00 1234 IN", "00:02 1234 OUT"]


print(solution(fees, records))
=======
import math

# 시간 계산기
def fee_cal(arr, fees):
    time = 0
    fee = 0
    # 애초에 반복문을 두칸씩 뛰게 함 -> IN만 가리키게 되어있다.
    for i in range(0, len(arr), 2):
        # IN 시간과 OUT 시간 차이 계산
        if i != len(arr) - 1:
            h = abs(int(arr[i][0].split(':')[0]) - int(arr[i+1][0].split(':')[0])) 
            if arr[i][0].split(':')[1] == '00':
                m = int(arr[i+1][0].split(':')[1])
            else : m = 60 - int(arr[i][0].split(':')[1]) + int(arr[i+1][0].split(':')[1])
            if h != 0 and m != 0:
                h -= 1
            time += h*60 + m
        # 마지막이 가리켜지는 경우 -> IN으로 끝나는 케이스
        if i == len(arr) - 1 or len(arr) == 1:
            h = 23 - int(arr[i][0].split(':')[0])
            m = 59 - int(arr[i][0].split(':')[1])
            time += abs(h*60) + abs(m)
    print(time)
    if time <= fees[0]:
        fee = fees[1]
    else:
        fee = fees[1] + math.ceil((time - fees[0])/fees[2]) * fees[3]
    return fee

def solution(fees, records):
    # 정보 담은 2차원 리스트
    record_splt = []

    # 자동차 번호 -> 누적 주차 시간 계산중 필요한 변수
    car_num = 0

    # 번호에 따른 입/출차 기록을 따로 저장해두는 '임시 리스트'
    car_timestamp = []

    # 결과
    result = []

    # [시간, 번호, 출입] 형태의 2차원 리스트로 변환
    for i in range(len(records)):
        record_splt.append(records[i].split())
    record_splt.sort(key = lambda record_splt: record_splt[1])
    print(record_splt)
    print('------------')

    # 차 번호별로 누적 주차 시간 계산해서 fees 리스트에 저장 -> 시간당 요금으로 변환
    for i in range(len(record_splt)):
        # car_num 변수에 차 번호 저장, 새 번호 나오면 '임시 리스트' 초기화 후 result 한칸 넘김
        # 차 번호별로 시간을 나누어 저장하게 해주자
        if record_splt[i][1] != car_num:
            car_num = record_splt[i][1] # 차 번호 인덱스
            print(car_timestamp)
            result.append(fee_cal(car_timestamp, fees))
            car_timestamp.clear() # '임시 리스트' 초기화
        car_timestamp.append(record_splt[i])
    result.pop(0)
    print(car_timestamp)
    result.append(fee_cal(car_timestamp, fees))
    return result


fees = 	[1, 10, 1, 11]
records = ["00:00 1234 IN", "00:02 1234 OUT"]


print(solution(fees, records))
>>>>>>> 64b63ffff40962bafb3e190004005c8dd044b77e
