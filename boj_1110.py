# 더하기 사이클 (68ms)

# 0 <= N <= 99
# 26: 2 + 6 = 8 -> 68: 6 + 8 = 14 -> 84 : 8 + 4 = 12 -> 42: 4 + 2 = 6 -> 26
# 0: 0 + 0 = 0 -> 0
# 더한 값의 일의 자리 수가 새로운 숫자의 일의 자리가 되는데 나머지 값으로 구하면 됨

# N = int(input())
# tmp = N
# count = 0

# while True:
#     a = N // 10
#     b = N % 10
#     c = a + b
#     new_N = 10 * b + c % 10
#     count += 1
    
#     N = new_N

#     if new_N == tmp:
#         break

# print(count)


# 재귀함수를 이용한 풀이, 종료조건???
# count = 0

# def recursive_num(n):
#     global count
#     n1 = n
#     a = n1 // 10
#     b = n1 % 10
#     c = a + b
#     d = str(c).zfill(2)
#     e = 10 * b + int(d[1])
#     count += 1

#     if n == 0:
#         count = 1
#         return count

#     if a == b and b == int(d[1]):
#         return count

#     recursive_num(e)

# recursive_num(int(input()))

a = 5
b = 5 // 10
print(b)