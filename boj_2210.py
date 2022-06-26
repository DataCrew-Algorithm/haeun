# Number Board (88ms)
# 숫자판의 임의의 위치에서 시작해서 만들수 있는 6자리수의 개수 (시작점: 완전탐색)
# 방문했던 곳을 또 갈 수 있다!

import sys
read = sys.stdin.readline

def dfs(x, y, number):

    if len(number) == 6:
        answer.add(number) # set에 데이터 넣을 때 add
        return

    else:
        for i in range(4):
            r = x + dx[i]
            c = y + dy[i]
            if  0 <= r < 5 and 0 <= c < 5:
                dfs(r, c, number + board[r][c])
                # 숫자 이어가면서 재귀함수 호출

board = [list(read().split()) for _ in range(5)] # 숫자연산이 아니라서 string 타입 그대로!
# print(board)

# 4가지 방향으로 이동 가능
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = set() # 중복 제거를 위해 set 사용

# 모든 시작점을 체크하면서 6자리 수 찾기
for i in range(5):
    for j in range(5):
        number = board[i][j]
        dfs(i, j, number)

# print(answer) 경우의 수 확인
print(len(answer))
