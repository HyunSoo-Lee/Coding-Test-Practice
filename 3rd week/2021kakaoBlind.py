import re
new_id = "...!@B-a_T#*..y.abcdefghijklm..."

# 1. 대문자 -> 소문자
new_id = new_id.lower()

# 2. 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
new_id = re.sub('[^0-9a-z-_.]','',new_id)

# 3. (.)가 2번 이상 연속된 부분을 하나로 치환
new_id = re.sub('\.+','.',new_id)

# 4. (.)가 처음이나 끝에 위치한다면 제거
new_id = new_id.strip('.')

# 5. 빈 문자열, "a"를 대입
if not new_id:
    new_id = 'a' 

# 6. 첫 15개의 문자를 제외한 나머지 문자들 제거
new_id = new_id[:15]

# 제거 후 (.)가 처음이나 끝에 위치한다면 제거
new_id = new_id.strip('.')

# 7. 마지막 문자를 new_id의 길이가 3이 될 때까지 붙임.
while len(new_id) < 3:
    new_id += new_id[-1]