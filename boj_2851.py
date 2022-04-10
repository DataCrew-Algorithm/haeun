# 슈퍼 마리오
# 점수의 합을 최대한 100 가깝게: 누적합과의 차이가 최솟값일 때, 최솟값이 3개일 확률은 낮지만 혹시 몰라서 2개 이상으로 조건문 만듦.
# 동일한 최소 gap을 가진 수가 여러 개일 경우 max.값으로 출력

# ver.1 : 72ms
scores = [int(input()) for i in range(10)]
sum_list = []
sum_num = 0
gap_list = []

for i in range(10):
    sum_num += scores[i]
    sum_list.append(sum_num)
    gap = abs(sum_list[i] - 100)
    gap_list.append(gap)   

min_num = min(gap_list)
idx = gap_list.index(min_num)

if gap_list.count(min_num) >= 2:                  # 최솟값이 2개 이상이면
    print(max(sum_list[idx], sum_list[idx+1]))    # 2개 누적 합 중에 최댓값을 출력
else:
    print(sum_list[idx])





# print(gap_list[min(gap_list)]) #IndexError: list index out of range
# print(sum_list[idx])

# scores = [int(input()) for i in range(10)]

# for i in range(len(scores)):
#     sum_num += scores[i]
#     sum_list.append(sum_num)
#     gap_list = abs(sum_list[i] - target)
#     print(gap_list)
#     if gap_list[i] < min_gap:
#         min_gap = gap_list[i]
#         min_count += 1
#         min_idx.append(min_count)
        
#     if min_count >= 2:
#         print(max(sum_list[idx], sum_list[idx+1]))
#     else:
#         print(sum_list[idx])

# def MarioScore(target, scores):
#     target = 0
#     min_gap = 99 # 양의 정수이므로 최솟값 비교 초기값은 가장 큰 99로 설정
#     min_count = 0
#     min_idx = []


MarioScore(100, scores)
