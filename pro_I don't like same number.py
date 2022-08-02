# 중복 숫자를 제거하고, 그 숫자 순서 그대로 출력하기
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12906

# ver.1 : 다른 수일 때만 치환해서 answer에 담아줌
def solution(arr):
    answer = []
    j = -1
    for i in arr:
        if i != j:
            j = i
            answer.append(i)

    return answer

# arr = [4, 4, 4, 3, 3]
arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr)) # [1, 3, 0, 1]


# ver.2: 슬라이싱을 이용하여 같은 값인지 비교
def not_continuous(arr):
    a = []
    for i in arr:
        print(a[-1:])
        # print([i])
        if a[-1:] == [i]: continue
        a.append(i)
    return a

arr = [1, 1, 3, 3, 0, 1, 1]
print(not_continuous(arr)) # [1, 3, 0, 1]

# li = [1, 2, 3, 4]
# print(li[-1])
# print(li[-1:])
# print(li[:-1])

# new = []
# for x in li:
#     print(new[-1:])
#     if new[-1:] == [x]: continue
#     new.append(x)
#     print(new)