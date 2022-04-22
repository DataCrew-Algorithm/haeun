# 이탈리아에서 아이스크림 사먹는 한윤정
# N: 아이스크림 종류 수, M: 섞어먹으면 안되는 조합의 갯수, (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)
# M 조합을 피해 섞어 먹을 수 있는 조합의 수

# Set 자료형 -> 메모리 초과
from itertools import combinations

n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
combination_set = list(map(set, combinations(data, 3)))
# print(combination_set)
# print(type(combination_set[0]))
not_com = []

for _ in range(m):
    input_set = set(map(int, input().split()))
    not_com.append(input_set)

result = 0
for i  in range(len(combination_set)):
    if len(combination_set[i]-not_com[0]) == 1:
        print(combination_set)
        result += 1
print(result)

# print(not_com)
# print(not_com[0])
# print(combination_set[1])
# print(len(combination_set[3]-not_com[0]))


# 함수형: 메모리 초과
from itertools import combinations

def find_list(x, y, list_com):
    new_list =[]
    for combi in enumerate(list_com):
        if x in combi and y in combi:
            pass
        else:
            new_list.append(combi)
    return new_list

n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
combination_set = list(map(list, combinations(data, 3)))

not_com = []
for _ in range(m):
    input_set = list(map(int, input().split()))
    not_com.append(input_set)

for i in range(m):
    x = not_com[i][0]
    y = not_com[i][1]
    temp_list = find_list(x, y, combination_set)

print(len(temp_list))

# 테스트
for i in range(len(combination_set)):
    for j in range(len(not_com)):
        if not_com[j][0] in i and not_com[j][1] in i:
            combination_set.remove(combination_set[i])
        print(combination_set)

# ==> 시간 초과
result = 0
for i  in range(len(combination_set)):
    for j in range(len(not_com)):
        if not_com[j][0] not in combination_set[i] and not_com[j][1] not in combination_set[i]:
            result += 1
print(result)

# ==> 시간 초과
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
combination_list = list(map(list, combinations(range(n), 3)))
not_com = [list(map(int, input().split())) for i in range(m)]

result = 0
for i  in range(len(combination_list)):
    for j in range(m):
        if not_com[j][0] not in combination_list[i] and not_com[j][1] not in combination_list[i]:
                result += 1
print(result)
