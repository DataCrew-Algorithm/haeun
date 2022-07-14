# Kevin's Bacon (132ms)
import sys
read = sys.stdin.readline
INF = int(1e9) # 무한대를 10억으로 정의
N, M = map(int, input().split())

graph = [[INF]*(N+1)  for _ in range(N+1)] # 그래프 표현


for _ in range(M):
  a, b = map(int, read().split())

  # 노드 연결 하기
  graph[a][b] = 1
  graph[b][a] = 1

# print(graph)

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

bacons = []
for i in range(1, N+1):
    # print(graph[i][1:]) # 자리 수 맞춰주려고 [i][1:]
    bacons.append(sum(graph[i][1:])) # 번호별 친구 관계 다 더한게 베이컨이므로 sum하여 추가
# print(bacons) # [6, 8, 5, 5, 8]

print(bacons.index(min(bacons)) + 1) # 베이컨 수가 가장 적은 사람이면서 여러 명일 때는 앞 번호니까 index 함수 활용


