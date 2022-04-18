# 피보나치 수
# 피보나치 수식을 반복문으로 옮기되 start_num1,2 및 f_nums의 index 유의
n = int(input())
f_nums = [0] * (n+1) # 구하는 n번째 숫자만큼 리스트 초기화
f_nums[0] = 0
f_nums[1] = 1

for i in range(2, n+1): # n번째 까지 반복하고 문제에서 n번째 피보나치 수를 구하는 것이므로 n+1까지!
    f_nums[i] = f_nums[i-1] + f_nums[i-2] 
print(f_nums[n])




# list assignment index out of range
# n = int(input())
# f_nums = [0] * (n) => 갯수가 맞지 않아서 틀림 (n번째가 되려면 0부터 시작이니까 n+1개로 만들어야 함)

# for i in range(3, num+1):
#     f_nums[i] = f_nums[i-1] + f_nums[i-2] 
# print(f_nums[num])