# 성적 통계
# 최대 점수, 최소 점수, 성적 내림 차순으로 정렬 했을 때 가장 큰 점수 차이를 구하는 프로그램

# Ver.1 : 예시 넣으면 맞게 출력되나 틀림
# import sys
# input = sys.stdin.readline
ttl_class_num = int(input())

def largest_gap(score):
    max_gap = 0
    score = sorted(score, reverse = True)
    for i in range(len(score)-1):
        if max_gap < score[i] - score[i+1]:
            max_gap = score[i] - score[i+1]
    return max_gap

for i in range(ttl_class_num):
    score = list(map(int, input().split()))
    class_num = i + 1
    max_score = max(score[1:])
    min_score = min(score[1:])
    gap = largest_gap(score[1:]) # 리스트 슬라이싱 안되서 틀렸던 것!!!
    print(f"Class {class_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {gap}")


# ver2. 일괄출력 해보기?? => 예시 넣으면 맞게 출력되나 틀림
import sys
input = sys.stdin.readline
ttl_class_num = int(input())

scores = []
class_num = []
result_list = [] # max_num, min_num, gap 

def largest_gap(score):
    max_gap = 0
    score = sorted(score, reverse = True)
    for i in range(len(score)-1):
        if max_gap < score[i] - score[i+1]:
            max_gap = score[i] - score[i+1]
    return max_gap

for i in range(ttl_class_num):
    scores.append(list(map(int, input().split())))
    class_num.append(i + 1)
    result_list.append([max(scores[i][1:]), min(scores[i][1:]), largest_gap(scores[i])])

for i in range(ttl_class_num):
    print(f"Class {class_num[i]}")
    print(f"Max {result_list[i][0]}, Min {result_list[i][1]}, Largest gap {result_list[i][2]}")

# print(class_num)
# print(result_list)

# Ver.3: 이중 for문으로 하니 맞았다..

import sys
input = sys.stdin.readline
ttl_class_num = int(input())
gap_list = []

for i in range(ttl_class_num):
    score = list(map(int, input().split()))
    class_num = i + 1
    max_score, min_score = max(score[1:]), min(score[1:])
    sorted_score = sorted(score[1:])

    for j in range(len(sorted_score)-1):
        gap = sorted_score[j+1] - sorted_score[j]
        gap_list.append(gap)
        max_gap = max(gap_list)

    print(f"Class {class_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {max_gap}")
    gap_list.clear()



