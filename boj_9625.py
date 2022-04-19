# BABBA
# 버튼 1번: A -> B, B-> BA

# s = "hihh"
# s = s.replace("h", "H")
# print(s.count("H"))

k = 3
s = "A"
# new_b = ""
# new_a = ""

# for _ in range(k):
#     if "B" in s:
#         s = s.replace("B", "BA")
        
#     elif "A" in s:
#         s = s.replace("A", "B")
#     print(s)
# -------------------------------------------------------------------------------------------------
# 피보나치 수열과 동일한 점화식 패턴으로 더해지는 것을 발견! replace하지 않아도 됨
# Ver.1 (메모리 초과)
# n = int(input())
# s0, s1 = "A", "B" # 초기 2개 값 설정
# s = ""

# if n == 1:
#     print(0, 1)
# elif n == 2:
#     print(1, 0)
# else:
#     for i in range(2, n+1): # n번째 까지 반복하고 문제에서 n번째 피보나치 수를 구하는 것이므로 n+1까지!
#         s = s0 + s1
#         result = s
#         s0 = s1
#         s1 = s
#     print(s.count("A"), s.count("B")) # 문자열 result 의 A, B의 갯수 출력

# Ver.2: 이것도 메모리 초과
# n = int(input())
# s0, s1 = "A", "B"

# if n == 1:
#     print(0, 1)

# else:
#     for i in range(2, n+1):
#         s = s0 + s1
#         result = s
#         s0 = s1
#         s1 = s
#     print(s.count("A"), s.count("B"))

# Ver3.
A, B = 0, 1 # 피보나치 수는 0과 1로 시작
ab_list = [0, 0] # 수열 생성에 사용할 리스트
for _ in range(2, int(input())+1):
    ab_list[0] = B              # index 0은 n 번째 피보나치 수열
    ab_list[1] = A + B   # index 1은 n+1 번째 피보나치 수열
    A, B = ab_list[0], ab_list[1] 
print(A, B)

# for i in range(2, 5):
#     l[i] = l[i-2]+l[i-1]
#     l.append(l[i])
#     print(l)

# n = int(input())