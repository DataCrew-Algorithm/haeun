# 프린터 큐
# Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
# Queue FIFO

N = int(input())
result = []

for i in range(N):      
    n, m = map(int, input().split())      # 문서 수, 문서 위치 인덱스
    p = list(map(int, input().split()))   # 중요도 리스트
    idx = [i for i in range(n)]
    idx[m] = 1
    count = 0

    while p:
        if p[0] == max(p):               # 중요도 첫번째 자리가 가장 높은 중요도일때
            count += 1                   
            if idx[0] == 1:              # 문서 위치 첫번째가 1일 때
                result.append(count)     # 바로 출력
                break
            p.pop(0)
            idx.pop(0)
        else:
            p.append(p.pop(0))
            idx.append(idx.pop(0))

for i in range(N):
    print(result[i])

