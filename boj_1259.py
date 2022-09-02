# 1. 펠린드롬 수 변형
# 2개의 자연수 n, m이 주어질 때 n이상 m 이하 자연수 중 펠린드롬 숫자의 개수를 return 하도록 솔루션 함수를 완성해라
# ex. (1, 100) -> 18, (100, 300) -> 20

def solution(n, m):
    answer = 0

    for i in range(n, m+1):
        i = str(i)
        if i[::-1] == i:
            answer +=1

    return answer

n, m = 100, 300
print(solution(n, m))


# 백준 문제: 뒤집어서 바로 yes, no 판별!
# num = input()

# while num != '0':

#     if num[::-1] == num: 
#         print('yes')
#     else:
#         print('no')
    
#     num = input() 
 
    