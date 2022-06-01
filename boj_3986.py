# Good Words
# 같은 문자 A, B끼리 교차하지 않는 쌍일때 '좋은 단어'
import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().rstrip()) for _ in range(N)] 
# print(words) # [['A', 'B', 'A', 'B'], ['A', 'A', 'B', 'B'], ['A', 'B', 'B', 'A']]
count = 0

for word in words:
    stk = []
    while word:
        w = word.pop()
        if not stk:
            stk.append(w)
        else:
            if stk[-1] == w:
                stk.pop()
            else:
                stk.append(w)
    if not stk:
        count += 1

print(count) 


# 다른 풀이 (from 요셉님)
# def goodOrBad(x):
#     for _ in range(int(len(x))):
#         x = x.replace('AA','').replace('BB','')
#     if len(x) == 0:
#         return 1
#     else:
#         return 0
        
# N = int(input())
# count = 0
# for _ in range(N):
#     count += goodOrBad(input())
# print(count)

