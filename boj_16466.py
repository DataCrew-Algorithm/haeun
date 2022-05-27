# Concert
# Ver1: 시간초과
# import sys
# input = sys.stdin.readline()

# N = int(input())
# tickets = list(map(int, input().split()))
# max_num = max(tickets)
# min_num = min([i for i in range(1, max_num) if i not in tickets])
# print(min_num)

# Ver2: 시간초과
# N = int(input())
# tickets = list(map(int, input().split()))
# all_tickets = [i for i in range(1, max(tickets)+1)]


# for i in tickets:
#     all_tickets.remove(i)
# print(min(all_tickets))


# Ver3: 정렬하고 인덱스를 비교하자! => 런타임 에러
# N = int(sys.stdin.readline())
# tickets = sorted(list(map(int, sys.stdin.readline().split())))
# available = []
# for i in range(1, N+1):
#     if tickets[i-1] != i:
#         available.append(i)
# print(min(available))


# Ver4. 참고 풀이
import sys

N = int(sys.stdin.readline())
sold = sorted(list(map(int, sys.stdin.readline().split())))

# 1 2 4 7 8
# 1 2 3 4 5 두 배열의 각 원소를 순서대로 비교해나감. 서로 값이 다를 경우 해당 순서의 자리가 빈 것
for i in range(1, N+1) :
    if(sold[i-1] != i) :
        print(i)
        sys.exit() # break와 같이 바로 종료함

#배열 중간에 빈 자리가 없는 경우 => 티켓 숫자가 연속해서 판매 되었을 경우 바로 다음 티켓부터 2차가 진행됨!
# 이 경우의 수를 놓쳐서 헤맸다.
print(N+1)


