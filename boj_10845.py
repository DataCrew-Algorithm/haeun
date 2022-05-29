# Queue (80ms)
# pop 사용 시 바로 출력해야 추가 pop 되지 않음 주의!

import sys

N = int(input())

orders = []
q = []

for _ in range(N):
    order = sys.stdin.readline().rstrip() # \n 줄바꿈 제외하고 값을 받고 싶을 때
    orders.append(order)

for i in orders:
    if i[:4] == "push":
        if len(i) >= 4:
            q.append(i[5:])
    elif i == "pop":
        if len(q) != 0:
            print(q.pop(0))
        else:
            print(-1)
    elif i == "size":
        print(len(q))
    elif i == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif i == "front":
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    else:
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)


# q = [1, 2, 3, 4]
# q.pop(0)
# print(q.pop(0))
# print(q)
# q.pop(0)
# print(q.pop(0))
# print(q)
# print(len(q))
# print(q[len(q)])
# print(q[len(q)-1])
# print(q[-1])

# 정수 범위: 1 <= N <= 100,000
# q2 = ['push 1', 'push 20', 'push 300', 'push 4000', 'push 50000', 'push 600000']
# li = []
# for i in q2:
#     if len(i) >= 4:
#         print(i[5:])
#         li.append(i[5:])
# print(li)
