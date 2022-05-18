# Card Game 1
# ver1. 92ms
from collections import deque
N = int(input())
card_q = deque([i for i in range(1, N+1)])
dump = [] # 버리는 카드

for i in range(N-1): # 카드 1개 남을 때 까지 반복 전체 수-1
    dump.append(card_q.popleft()) # 가장 첫번째 카드 (가장 위에 있는) 버리기
    card_q.append(card_q.popleft()) # 그다음 카드 카드 순서 가장 뒤로
final_card = list(card_q) # deque를 다시 list로 바꾸기
result = dump + final_card
print(*result)

# ver2. 76ms
n = int(input())
queue = list(range(1, n+1))

while len(queue) > 1: # 카드가 1개 남을 때까지 반복
    print(queue.pop(0), end=" ") # 버리는 거 바로 출력
    queue.append(queue.pop(0)) # 버리고 바로 가장 첫번째 원소를 가장 끝으로 더하기
    
print(queue[0])