# 지능형 기차
# people = []    # 인풋 사람 수 저장
# station = []   # 기차역 별 총 사람의 수
# start_num = 0  # 기차역에 있는 사람 초깃값

# for i in range(4):                                      # 문제에서 주어지는 기차역 4곳 = 4회 반복                       
#     people.append(list(map(int, input().split(" "))))   
#     ttl = start_num + people[i][1] - people[i][0]
#     start_num = ttl
#     station.append(start_num)

# print(max(station))

# people = []    # 인풋 사람 수 저장
station = []   # 기차역 별 총 사람의 수
start_num = 0  # 기차역에 있는 사람 초깃값

for i in range(4):                                      # 문제에서 주어지는 기차역 4곳 = 4회 반복                       
    people = list(map(int, input().split(" ")))   
    start_num = start_num + people[1] - people[0]
    station.append(start_num)

print(max(station))