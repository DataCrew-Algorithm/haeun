# 성 지키기 (76ms)
# 모든 행과 열에 최소 경비원 1명이 있어야 한다.
# 값을 입력 받은 상태에서 이중 for문으로 한번에 해보려고 했으나 안되서
# 1차적으로 경비원이 없는 위치만 조건을 걸기 위해 리스트 초기화 => 있으면 1로 처리
# 행과 열을 구분한 리스트에 필요한 경비원의 수를 넣어 계산하고, 2개 중 최댓값이 꼭 필요한 경비원의 수인 것을 발견함

r, c = map(int, input().split())
guard_status = []
row = [0] * r
column = [0] * c

for i in range(r):
    guard_status.append(input())

for i in range(r):
    for j in range(c):
        if guard_status[i][j] == "X" : # 행에 경비원이 있는지 확인
            row[i] = 1        # 있으면 행 리스트에 1로 찍기
            column[j] = 1     # 있으면 열 리스트에 1로 찍기

# 행과 열에 필요한 경비원을 세기 위해 변수 지정
# 행과 열 리스트 원소 값이 0이면 1개씩 더해주고, 마지막에 최댓값을 구함
row_count = 0
column_count = 0

for i in range(r):
    if row[i] == 0:
        row_count += 1
for j in range(c):
    if column[j] == 0:
        column_count += 1
print(max(row_count, column_count))
