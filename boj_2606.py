# Worm Virus

#Ver1. 스택구조
import sys
from collections import deque

vert_list = [i for i in range(1, int(input()))]
edge_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(input()))]
print(vert_list)
print(edge_list)

adjac_list = [[] for vertex in vert_list]

for edge in edge_list:
    adjac_list[edge[0]].append(edge[1])

print(adjac_list)

# [[], [2, 5], [3], [], [7], [2, 6]]

def stack_graph(adjac_lst):
    stack = [1]
    visit_vert = []
    while stack:
        current = stack.pop()
        if current not in visit_vert: 
            visit_vert.append(current)
            stack.extend(adjac_list[current])

    return len(visit_vert)-1 # visit_vert는 확인, count만 result 값으로

print(stack_graph(adjac_list))


# # Ver2. 
# from collections import defaultdict

# # DFS 함수 정의
# def dfs(graph, v, visited):
#     # 현재 노드 방문 처리
#     visited[v] = True
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#     # 1번은 제외되어야 하기 때문에 -1
#     return visited.count(True) - 1


# N = int(input())
# M = int(input())

# # collections 모듈의 defaultdict 함수를 이용하여 딕셔너리의 value를 리스트로 default
# graph = defaultdict(list)

# # Key = 컴퓨터 번호, Value = Key 컴퓨터와 연결된 컴퓨터들
# for _ in range(M):
#     a, b = map(int, input().split())
#     # defaultdict로 value가 리스트로 되어있기 때문에 append()를 통해 원소 추가
#     graph[a].append(b)
#     graph[b].append(a)

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(False: 미방문, True: 방문)
# visited = [False] * (N+1)

# print(dfs(graph, 1, visited))


# # ver3: 수현님 풀이 68ms
# from sys import stdin
# read = stdin.readline
# dic={}
# for i in range(int(read())):
#     dic[i+1] = set()
# for j in range(int(read())):
#     a, b = map(int,read().split())
#     dic[a].add(b)
#     dic[b].add(a)

# # print(dic)
# # {1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

# def dfs(start, dic):
#     for i in dic[start]:
#         if i not in visited:
#             visited.append(i)
#             dfs(i, dic)
# visited = []
# dfs(1, dic)
# print(len(visited)-1)
