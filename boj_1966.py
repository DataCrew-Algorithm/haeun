# 프린터 큐
# Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
# Queue FIFO

N = int(input())
result = []

for i in range(N):      
    n, m = map(int, input().split())      # 문서 수, 문서 위치 인덱스
    p = list(map(int, input().split()))   # 중요도 리스트
    idx = [i for i in range(n)]
    queue = [(pri, i) for pri, i in zip(p, idx)]

#     count = 0
#     if p[0] == max(p):               # 중요도 첫번째 자리가 가장 높은 중요도일때
#         count += 1                   
#         result.append(count)     # 바로 출력
#         break
#         p.pop(0)
#         idx.pop(0)

# for i in range(N):
#     print(result[i])


# 큐 문제 풀이 복습

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().strip().split()))
    queue = [(v, idx) for idx, v in enumerate(queue)]
#     # print(queue)
#     # print(max(queue)[0])
#     # print((queue)[0][0])
#     # print((queue)[0][1])

    count = 0
    while True:
        if max(queue)[0] == queue[0][0]:
            count += 1
            if queue[0][1] == M:  # 가장 중요한 문서가 현재 문서이면 바로 출력
                print(count)
                break
            else:
                queue.pop(0) 
        else: 
            queue.append(queue.pop(0)) # 현재 문서보다 더 중요한 문서일때 뒤로 재배치
