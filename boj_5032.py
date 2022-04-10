# # 탄산음료

# em_b, new_b, need_b = map(int, input().split())
# ttl = em_b + new_b
# get_b = 0

# while ttl >= need_b:                          # 빈 병이 교환에 필요한 병 보다 많을 때만 교환 가능)
#     get_b += ttl // need_b                    # 받는 탄산 수
#     ttl = (ttl // need_b) + (ttl % need_b)    # 새 병이 빈병이 됨+ 나머지 병이 전체 빈병 수
# print(get_b)


# 다른 풀이법
empty_1, empty_2, div = map(int, input().split())

quo = empty_1 + empty_2
quo_sum = 0 
residual = 0

while quo >= 1:    
    quo, residual = divmod((quo + residual), div) # 몫, 나머지 동시 출력
    print(quo, residual)
    quo_sum += quo # 초기값 제외 몫 다 더함

print(quo_sum)






# em_b, new_b, need_b = map(int, input().split())
# em_b = (em_b + new_b)
# get_b = 0

# if em_b >= need_b:                  # 새로 받은 병의 수가 교환에 필요한 병의 수 보다 클 때 (추가 교환 가능)
#     get_b += get_b // need_b
#     residual = em_b % need_b
#     em_b = get_b + residual
#     if em_b < need_b:
#         print(get_b)