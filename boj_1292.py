# 쉽게 푸는 문제

start, end = map(int, input().split())

num_list = []
for i in range(1, 1001): # 1000번째 자리까지 가능하므로
    for j in range(i): # 입력 수(i)만큼 반복하여 i를 리스트에 넣기
        num_list.append(i)

# 구간 합 출력
# 3~7 구간 합이면, 3, 4, 5, 6, 7 => 인덱스 순서 3번째가 2이므로 start-1
print(sum(num_list[start-1 : end]))