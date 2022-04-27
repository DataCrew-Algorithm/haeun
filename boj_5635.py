# 생일
# 가장 나이가 적은 사람의 이름, 가장 많은 사람의 이름을 출력해라
# 학생 수 1 ≤ n ≤ 100, 1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31


# 연도 비교 (최대, 최소) -> 중복이면 월 비교, 일 비교하는 조건문으로 하려고 했는데
# 개별 리스트 만드는 것도 데이터가 많으면 조건 비교하고 하는데 시간 초과 될까봐 짜보다가 멈춤

# n = int(input())
# id_info = [input().split() for i in range(n)]
# year_list = [int(id_info[i][3]) for i in range(n)]
# month_list = [int(id_info[i][2]) for i in range(n)] 
# day_list = [int(id_info[i][1]) for i in range(n)]
# name_list = [id_info[i][0] for i in range(n)]
# print(year_list)
# print(month_list)
# print(day_list)
# print(name_list)

# import time
import sys
# start_time = time.time()
input = sys.stdin.readline

n = int(input())
id_list  = []

for i in range(n):
    name, day, month, year = input().split() 
    # 한 자리수 날짜, 월 앞에 0 더하기
    if len(day) == 1:
        day = '0' + day
    if len(month) == 1:
        month = '0' + month
    
    # 1개 리스트로 만들 때 생년월일을 붙여서 정렬만 하면 찾을 수 있게 함
    id_list.append((name, year + month + day))

# 오름차순, 내림차순 외 특정 데이터로 sorting 가능한지 검색하여 찾음
# 생년월일 기준으로 오름차순 정렬 됐는지 확인
# print(sorted(id_list, key = lambda x: int(x[1])))
id_list = sorted(id_list, key = lambda x: int(x[1]))
print(id_list[-1][0]) # 가장 나이 어린 사람 이름
print(id_list[0][0])  # 가장 나이 많은 사람 이름

# end_time = time.time()
# print("time: ", end_time - start_time)
