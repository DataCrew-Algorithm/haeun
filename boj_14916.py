# 거스름돈
# 1. 5의 배수이면 5로 나눈 몫이 최솟값
# 2. 5의 배수가 아니면 5로 빼고, 그 값을 2로 다시 나눠줌 (뺄 때 마다 코인 개수 1 추가)
# 3. 거스름돈이 없으면 -1로 출력 (ex. input: 1,2,3,4)

# ver. 1 : 틀림
# money = int(input()) # 거스름돈 액수 입력값
# min_sum = 0          # 최소 코인 갯수의 합

# if money < 0:
#     print(-1)
 
# while money > 0:
#     if money % 5 == 0:
#         min_sum += money // 5
#         break
#     else:
#         money -= 2 
#         min_sum += 1
#         if money % 2 == 0:
#             min_sum += money // 2
#             break
# print(min_sum)

# ver. 2 : 틀림 
# money = int(input()) 
# min_sum = 0          

# while True: 
#     if money % 5 == 0:
#         min_sum += money // 5
#         break
        
#     elif money % 5 != 0:
#         money -= 5
#         min_sum += 1

#         if money % 2 == 0:
#             min_sum += money // 2
#             break

#     if money < 2:
#         print(-1)
#         break

# print(min_sum)


# 1과 3의 반례 때문에 에러가 났음: 그래서 5가 아니라 2로 빼야 함!!!
# Ver.3

money = int(input()) 
min_sum = 0          

while True: 
    if money % 5 == 0:
        min_sum += money // 5
        print(min_sum)
        break

    money -= 2
    min_sum += 1

    if money < 0:
        print(-1)
        break




