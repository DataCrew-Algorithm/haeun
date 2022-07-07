# Diameter of the tree
# 지름: 2개의 노드를 선택했을 때 트리의 모든 경로 중 가장 긴 길이

# import sys

# v = int(input())
# # 부모 테이블 초기화
# parent = [0] * (v+1)
# for i in range(1, v+1):
#     parent[i] = i

# # find 연산: 특정 원소가 속한 집합 찾기
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x]) # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     return parent[x]

# # union 연산: 2개 원소가 속한 집합 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
# edges = []
# total_cost = 0

# # 간선 정보 주어지고 비용을 기준으로 정렬
# for _ in range(v-1):
#     a, b, cost = map(int, input().split()) # 부모, 자식, 가중치
#     edges.append((cost, a, b))

# # 간선 정보 비용 기준으로 오름차순 정렬
# edges.sort()

# # 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
# for edge in edges:
#     cost, a, b = edge

#     # find 연산 후, union 연산 수행 사이클이 발생하지 않는 경우에만 -> 최소 신장 트리에 포함!
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         print(edge)
#         print(cost)
#         total_cost += cost

# print(total_cost) 최소 총비용 (모든 트리 간선의 합)

# 최소 신장 트리까지 그리는 것은 알겠는데 최대 길이가 나오는 노드 2개를 pick하는 게 생각이 안 남...

# 참고 풀이 (96ms): 트리의 모든 간선을 탐색하면서 길고 짧은 것을 비교, 큰 값으로 계속 업데이트
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def dimt(idx):
    global R
    if tree[idx]:
        large = 0
        small = 0
        for i, d in tree[idx]:
            now_distance = dimt(i)+d
            if now_distance > large:
                small = large
                large = now_distance
            elif now_distance > small:
                small = now_distance
        R = max(large + small, R)
        return large
    else:
        return 0


N = int(input())
tree = [[] for _ in range(N+1)]
N -= 1
R = 0
while N:
    parent, child, distance = map(int, input().split())
    tree[parent].append([child, distance])
    N -= 1
dimt(1)
print(R)