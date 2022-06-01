# Deque (104ms)
import sys
from collections import deque

N = int(input())

orders = []
q = deque()

for _ in range(N):
    order = sys.stdin.readline().rstrip() # \n 줄바꿈 제외하고 값을 받고 싶을 때
    orders.append(order)

for i in orders:
    if i[:10] == "push_front":
        q.appendleft(i[11:])
    elif i[:9] == "push_back":
        q.append(i[10:])
    elif i == "pop_front":
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif i == "pop_back":
        if len(q) != 0:
            print(q.pop())
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