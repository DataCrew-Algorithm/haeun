# 1. 5의 배수이면 5로 나눈 몫이 최솟값
# 2. 5의 배수가 아니면 3으로 빼고, 그 값을 5로 다시 나눠줌 (3으로 뺄 때 마다 1 추가)
# 3. 0보다 작게 되면 -1로 출력 (ex. input: 4)

sugar_kg = int(input()) # 설탕 무게 입력값
min_sum = 0             # 최소 봉지 갯수의 합

while True: 
    if sugar_kg % 5 == 0:
        min_sum += sugar_kg // 5
        print(min_sum)
        break

    sugar_kg -= 3
    min_sum += 1    
    if sugar_kg < 0:
        print(-1)
        break







