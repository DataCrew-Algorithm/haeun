a = [[0]*3 for _ in range(3)] # 3 X 3 행렬 만들 때
# print(a)

# 다른 a = [[0]*3]*3으로 절대하지 말것! 저장 위치가 같아져서 데이터 변경 시 같이 바뀜

V, E = map(int, input().split()) # V, E 정점 수, 간선 수
adj_mat = [[0]*(V+1) for _ in range(V+1)] # 0으로 채워진 8 X 8 틀 만들기! 

for i in range(E):
    start, end = map(int, input().split()) # 만약 1, 2를 인풋 받으면
    adj_mat[start][end] = 1 # 일단은 adj_mat[1][2] = 1
    adj_mat[end][start] = 1 # 무향 그래프이기 때문에 파트너도 넣어줌

for _ in range(V+1):
    print(adj_mat[_])

visited = [] # 방문했던 정점을 기록
stack = [1]    # 1번에서 시작

while stack: # 스택이 빌 때까지 돌아랏!! 리스트가 비면 False로 봐서 끝남
    current = stack.pop()
    if current not in visited: # 그 점을 방문하지 않았으면 추가함
        visited.append(current)

    for destination in range(V+1):
        if adj_mat[current][destination] == 1 and destination not in visited: # 이어져 있고 +  방문하지 않았을 때
            stack.append(destination) # 종착지를 stack에 추가함

print(visited)
