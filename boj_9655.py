# 돌 게임
# 1개 또는 3개만 가져갈 수 있음 (상근SK가 먼저 시작)
# 마지막에 가져가는 사람이 이긴다.

# 3a + b = N
# Ver.1 : fail

# N = int(input())

# def stone_game(N):
#     split_n = N // 3
#     remainder = N % 3
#     if (split_n + remainder) % 2 == 1:
#         return print("SK")
#     else:
#         return print("CY")

# stone_game(N)


# Ver.2 : 76ms
# 결국 돌멩이의 갯수가 짝수이냐 홀수이냐에 따라 마지막 사람 순서가 정해져서
# 홀수면 상근, 짝수면 창영이 이기는 게임

stone = int(input())

def stone_game(N):
    if stone % 2 == 1:
        return print("SK")
    else:
        return print("CY")

stone_game(stone)