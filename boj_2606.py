# Worm Virus

#Ver1. 스택/큐를 이용한 풀이 (96ms)
import sys
from collections import deque

graph={}
for i in range(int(input())):
    graph[i+1] = set()
for j in range(int(input())):
    a, b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

# print(graph)
# {1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

def dfs(graph, start_node):
     
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = deque([]), deque([])
 
    ## 시작 노드를 시정하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
            
    return len(visited)-1

print(dfs(graph,1))


# Ver2. defaultdict 함수 이용 (92ms)
from collections import defaultdict

# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    # 1번은 제외되어야 하기 때문에 -1
    return visited.count(True) - 1


N = int(input())
M = int(input())

# collections 모듈의 defaultdict 함수를 이용하여 딕셔너리의 value를 리스트로 default
graph = defaultdict(list)

# Key = 컴퓨터 번호, Value = Key 컴퓨터와 연결된 컴퓨터들
for _ in range(M):
    a, b = map(int, input().split())
    # defaultdict로 value가 리스트로 되어있기 때문에 append()를 통해 원소 추가
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(False: 미방문, True: 방문)
visited = [False] * (N+1)

print(dfs(graph, 1, visited))


# ver3: 재귀함수_수현님 풀이 68ms
from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

# print(dic)
# {1: {2, 5}, 2: {1, 3, 5}, 3: {2}, 4: {7}, 5: {1, 2, 6}, 6: {5}, 7: {4}}

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)
