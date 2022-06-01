# 괄호(Parenthesis)
# 괄호 문자열(Valid PS, VPS) 찾기!
# 스택이 비어있는 것이 괄호의 짝이 맞는 것이라 yes, 아닐 때 no
# '('다음에 ')'이 올 경우 짝이 맞는거니까 pop으로 기존 스택을 초기화

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    string = input().rstrip()
    stk = []
    
    for i in string:
        if i == '(':
            stk.append(i)
        elif i == ')':
            if stk:
                stk.pop()
            else:
                print("NO")
                break
    else:            
        if not stk:                       
            print("YES")
        else:
            print("NO")
        
