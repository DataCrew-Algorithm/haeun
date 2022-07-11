# The Game of Death
# 처음 시작하는 사람이 임의의 자연수 K를 말할 때, 시작한 사람부터 지목한 사람을 따라가다 K번째 지목한 사람이 걸림
# 희현: 1번, 주경: N번 // 희현이부터 게임 시작!, 자기 자신을 지목할 수 있음
# 주경이 걸리지 않으면 0 출력

# ver.1: 50%까지 되고 틀림
# import sys
# read = sys.stdin.readline

# cnt = 0

# def find_k(num_list):
#     global cnt

#     for num in nums:
#         if num != N:
#             cnt += 1

#         if num == N:
#             cnt += 1
#             return cnt

#         if cnt == 0:
#             return 0

# T = int(input()) # 테이트 케이스 수
# N = int(input()) # 플레이어 숫자

# nums = []

# for _ in range(T):
#     for i in range(N):
#         num = int(read().rstrip())
#         nums.append(num)
#     print(find_k(nums))
# # print(nums)

# 최소숫자 k, dfs로 풀어보자: 아래 풀이 런타임ERROR

# import sys
# read = sys.stdin.readline

# def dfs(node):
#     for n in graph[node]:
#         # print(n) 시작점 index에 있는 원소: 예시에서는 2 (1번이 2번 지목!)
#         if check[n] == 0:               
#             check[n] = check[node] + 1  # 간선 1이라서 1일씩 업데이트
#             # print(check[n]) 
#             dfs(n)

# T = int(input()) # 테이트 케이스 수

# for _ in range(T):
#     N = int(input()) # 플레이어 숫자
#     graph = [[] for _ in range(N+1)]

#     for i in range(1, N+1):
#         num = int(read())
#         graph[i].append(num)
#     # print(graph)
#     check = [0] *(N+1)
#     dfs(1) # 1번부터 시작

# print(check[N] if check[N] > 0 else 0) ==> Indentation 주의!!


def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
for _ in range(int(input())):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        v = int(input())
        graph[i].append(v)
    check = [0]*(N+1)
    dfs(1)
    print(check[N] if check[N] > 0 else 0)