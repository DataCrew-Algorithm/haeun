# 쉽게 푸는 문제
# Ver.1 (120ms)
start, end = map(int, input().split())

num_list = []
for i in range(1, 1001): # 1000번째 자리까지 가능하므로
    for j in range(i): # 입력 수(i)만큼 반복하여 i를 리스트에 넣기
        num_list.append(i)

# 구간 합 출력
# 3~7 구간 합이면, 3, 4, 5, 6, 7 => 인덱스 순서 3번째가 2이므로 start-1
print(sum(num_list[start-1 : end]))


# Ver.2 _반복 수를 줄여도 됨 (더 효율적!)
start, end = map(int, input().split())

num_list = []
for i in range(1, 46): # 1000번째 위치하는 수는 45이므로..
    for j in range(i): # 입력 수(i)만큼 반복하여 i를 리스트에 넣기
        num_list.append(i)

print(sum(num_list[start-1 : end]))


# Ver.3 _코드 참조, 리스트에 이어서 붙이기

l = []
answer = 0

for i in range(1, 46):
    l_sub = [i]*i
    l += l_sub

a, b = map(int, input().split())

for j in range(a, b+1):
    answer += l[j-1]
print(anser)
