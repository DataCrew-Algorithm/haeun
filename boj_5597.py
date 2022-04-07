# 과제 안 낸 학생(68ms)
# 비교를 위해 전체 학생 넘버 리스트 생성
all_nums = [i for i in range(1, 31)]
nums = [int(input()) for i in range(28)]

# 입력 학생 번호가 전체 리스트에 없으면 해당 번호 출력
for i in range(len(all_nums)):
    if all_nums[i] not in nums:
        print(all_nums[i])



