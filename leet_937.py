# Reorder Log Files
# 로그의 가장 맨 앞 부분: 식별자
# 정렬 순서: 문자 로그 > 숫자 로그, 문자가 동일할 경우 식별자 순서로
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

# 식별자 구분을 위한 리스트 만들기
def reorder_log(logs):
    let = []
    dig = []

    for log in logs:
        if log.split()[1].isdigit(): # Return T/F
            dig.append(log)
        else:
            let.append(log)

    let.sort(key = lambda x: (x.split()[1:], x.split()[0])) # 정렬하고자 하는 기준이 1개 이상일 때 괄호로 묶어주기
    return let + dig

print(reorder_log(logs)) 

