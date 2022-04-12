# 소트인사이드
# 자리 수를 내림차순하여 정렬한 수 출력
# 입력 값: 정수화, reverse를 이용한 내림차순 정렬 -> 바로 출력

# Ver.1: sort 함수 이용 (72ms)
num = list(map(int,input()))
num.sort(reverse = True)
print(*num, sep="")

# Ver.2: 구현 (76ms)
num = list(map(int, input()))
sorted_num = []                  # 분류된 리스트를 새로 생성

for i in range(len(num)):        # 전체 숫자 자리수만큼 반복
    max_num = max(num)           # 최댓값 기준으로 인덱스 0부터 리스트에 넣기 위해 max 함수 활용
    sorted_num.append(max_num)   # 최댓값을 sorted_num에 넣고,
    num.remove(max_num)          # 분류가 끝난 값은 기존 리스트에서 제거
print(sorted_num)