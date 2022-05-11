# Ver.1 리스트 풀이 (4000ms)
K = int(input())

new_nums = []

for i in range(K):
    num = int(input())
    if num == 0:
        new_nums.pop()
    else:
        new_nums.append(num)    # 0이 아닐때만 포함
print(sum(new_nums))

# Ver2. deque  걸린 시간은 오히려 리스트 보다 더 걸림 (4168ms)
# deque : 리스트 자료형과 다르게 슬라이싱, 인덱싱 기능은 사용 x
# 연속적으로 나열된 데이터의 시작부분, 끝부분에 데이터를 삽입하거나 삭제할 때 매우 효과적
# 스택과 큐 기능 모두 포함 // 파이썬에서 스택을 이용할 때 별도의 라이브러리를 사용할 필요 x

from collections import deque

K = int(input())

data = ([])

for i in range(K):
    num = int(input())
    if num == 0:
        data.pop()  
    else:
        data.append(num)      # 0이 아닐때만 포함
print(sum(data))
