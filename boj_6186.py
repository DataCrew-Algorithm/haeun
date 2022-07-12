# Best Grass
# 잔디 구획 수 찾기 --> dfs + string type 문제

def dfs(x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < C) and (0 <= ny < R):
            if grass_map[ny][nx] == '#':
                grass_map[ny][nx] = '.'
                dfs(nx, ny)

while True:
    R, C = map(int, input().split())
    if C == 0 & R ==0:
        break
    else:
        grass_map = [list(input()) for i in range(R)]
        # print(grass_map)

        cnt = 0

        for y in range(R):
            for x in range(C):
                if grass_map[y][x] == '#':
                    dfs(x, y)
                    cnt += 1

        print(cnt)
        break # print 되고 입력 받으려고 기다리는 경우가 있어서 break 해줘야 EOFError (End Of File)런타임에러 안 난다.