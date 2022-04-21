# 배수와 약수
# ver.1 틀림
# def num_relation(n1, n2):
#     try:
#         if n2 % n1 == 0:
#             return print("factor")
#         elif n1 % n2 == 0:
#             return print("multiple")
#         else:
#             return print("neither")
#     except ZeroDivisionError:
#         pass

# for _ in range(4):
#     n1, n2 = map(int, input().split())   
#     num_relation(n1, n2)


# Ver2 : 반복문 제거 - 틀림
# def num_relation(n1, n2):
#     try:
#         if n2 % n1 == 0:
#             print("factor")
#         elif n1 % n2 == 0:
#             print("multiple")
#         else:
#             print("neither")
#     except ZeroDivisionError:
#         pass
# n1, n2 = map(int, input().split())   
# num_relation(n1, n2)

# Ver 3. : 언제 반복이 끝나는지 모르니까 While로 변경, 0과 0 일때는 break로 명시하여 종료 (72ms)
while True:
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0:
        break
    if n2 % n1 == 0:      # 첫번째 수가 두번째 수의 약수일 때
        print("factor")
    elif n1 % n2 == 0:    # 첫번째 수가 두번째 수의 배수일 때
        print("multiple")
    else:                 # 약수, 배수 관계가 아닐 때
        print("neither")
    
    


