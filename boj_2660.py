# 회장뽑기 (92ms)
# 회장: 점수가 가장 작은 사람
# print(점수, 회장 후보 수)
# print(회장 후보 오름차수)

import sys

read = sys.stdin.readline
INF = int(1e9) # 무한대를 10억으로 정의
N = int(input())

graph = [[INF]*(N+1)  for _ in range(N+1)] # 그래프 표현


while True:
  a, b = map(int, read().split())

  if a == -1 and b == -1:
    break
  
  # 노드 연결 하기
  graph[a][b] = 1
  graph[b][a] = 1

print(graph)

# 자기 자신으로 가는 비용 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

# 플루이드 워셜 알고리즘 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 둘 중 최솟값으로 업데이트

result = []
for i in range(1, N+1):
    # print(graph[i][1:]) # 자리 수 맞춰주려고 [i][1:]
    # print(max(graph[i][1:])) # 노드 별 친구 관계 점수 업데이트
    result.append(max(graph[i][1:])) # i번째부터 전체 노드까지 최소 거리
# print(result) # [3, 2, 2, 2, 3]

print(min(result), result.count(min(result)))
for i, score in enumerate(result):
    if score == min(result):
        print(i+1, end= " ")