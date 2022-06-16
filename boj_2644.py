# 촌수계산

# 예제 답변은 나오지만 틀린 풀이
import sys
read = sys.stdin.readline

n = int(input()) # 전체 사람 수
a, b = map(int, read().split()) # 문제에서 요구하는 두 사람의 촌수
m = int(input()) # 부모 자식들 간 관계 개수


dic={}
for i in range(n):
    dic[i+1] = set()
for j in range(m):
    x, y = map(int,read().split())
    dic[x].add(y)
    dic[y].add(x)

# print(dic)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(b, dic)
# print(b)
# print(visited) # 3부터 출발하여 체크한 사람들 수


visited = sorted(visited)
visited.remove(b)
rel = 0

# print(visited)
# print(a)

if a not in visited: # a가 체크한 리스트에 없으면 관계가 없으므로 바로 -1
    print(-1)

else:
    for visit in visited:    
        if visit != a:
            rel += 1

        else:
            rel += 1
            print(rel)
            break



# 참고 풀이 (72ms): dfs 함수 부분에 연결될 때마다 num 더해주고, num을 별도로 저장하는 게 달랐다.
# 입력값 받는 부분
N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

print(graph)
# [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

# dfs
def dfs(v, num):
  num += 1
  visited[v] = True

  if v == B:
    result.append(num)

  for i in graph[v]:
    if not visited[i]:  
        dfs(i, num)

dfs(A, 0)
if len(result) == 0: # 촌수가 없으면 -1 출력
  print(-1)
else:
  print(result[0]-1) # 촌수에 자기자신 제외