# Golden Bach Number

# 테스트 케이스 T만큼 주어지는 짝수 n ( 4 <= n <= 10,000)
# 두 소수의 차이가 가장 작은 것으로 출력!

# T = int(input())
# nums = [int(input()) for i in range(T)]
# # print(nums)


# Ver1 (시간초과)

# def GoldenB(num): 
#     import math
#     from itertools import combinations_with_replacement # 중복 가능

#     erastos = [True] * (num + 1) # 소수 판별 여부를 담는 리스트 (0 ~ n까지)
#     erastos[0], erastos[1] = False, False # 0과 1은 소수가 아니므로 False로 초기화
    
#     for i in range(1, int(math.sqrt(num)) + 1): # 시간 단축하기 위해 제곱근 사용
#         if erastos[i] == True: # i가 소수인 경우
#             j = 2
#             while i * j <= num:
#                 erastos[i * j] = False # i를 제외한 i의 모든 배수 지우기
#                 j += 1
    
#     prime_numbers = []
#     for i in range(num):
#         if erastos[i]:
#             prime_numbers.append(i)

#     golden_b = []
#     gaps = []
#     pairs = list(combinations_with_replacement(prime_numbers, 2))
#     for pair in pairs:
#         a, b = pair[0], pair[1]
#         if a + b == num:
#             golden_b.append([a, b])
#             gaps.append(b-a)
    
#     if len(golden_b) > 1:
#         idx =gaps.index(min(gaps))
#         return golden_b[idx]

#     else:
#         return golden_b[0]

# for num in nums:
#     print(*GoldenB(num))



# Ver2 (투 포인터 버전)

# def GoldenB(num): 
#     import math

#     erastos = [True] * (num + 1) # 소수 판별 여부를 담는 리스트 (0 ~ n까지)
#     erastos[0], erastos[1] = False, False # 0과 1은 소수가 아니므로 False로 초기화
    
#     for i in range(1, int(math.sqrt(num)) + 1): # 시간 단축하기 위해 제곱근 사용
#         if erastos[i] == True: # i가 소수인 경우
#             j = 2
#             while i * j <= num:
#                 erastos[i * j] = False # i를 제외한 i의 모든 배수 지우기
#                 j += 1
    
#     prime_numbers = []
#     for i in range(num):
#         if erastos[i]:
#             prime_numbers.append(i)

#     # golden_b = []
#     # gaps = []
    
#     # 투 포인터
#     interval_sum = 0
#     end = 0

#     for start in range(len(prime_numbers)):
#         while interval_sum < num and end < len(prime_numbers):
#             interval_sum += prime_numbers[end]
#             end += 1

#         if interval_sum == num:
#             a, b = prime_numbers[start], prime_numbers[end]
#             print(a, b)
        
#         interval_sum -= prime_numbers[start]
#             # golden_b.append([a, b])
#             # gaps.append(b-a)
    
#     # if len(golden_b) > 1:
#     #     idx =gaps.index(min(gaps))
#     #     return golden_b[idx]

#     # else:
#     #     return golden_b[0]

# for num in nums:
#     # print(*GoldenB(num))
#     print(GoldenB(num))



# ver3 정답 참고 (688ms)

def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if is_prime(a) and is_prime(b): # 소수 일때만 출력!
            print(a, b)
            break
        else:
            a -= 1
            b += 1
