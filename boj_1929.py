# 소수 구하기 
# M 이상 N이하의 소수를 모두 출력

# ver1. (488ms)
# 에라스토스의 체

def erastosSieve(end): # 시작, 끝 범위 수 입력 (0 ~ n까지)
    erastos = [True] * (end + 1) # 소수 판별 여부를 담는 리스트
    erastos[0], erastos[1] = False, False # 0과 1은 소수가 아니므로 False로 초기화
    
    for i in range(2, int(end ** 0.5) + 1): # 시간 단축하기 위해 제곱근 사용
        if erastos[i] == True: # i가 소수인 경우
            j = 2
            while i * j <= end:
                erastos[i * j] = False # i를 제외한 i의 모든 배수 지우기
                j += 1
                
    return erastos

start, end = map(int, input().split())

for i, v in enumerate(erastosSieve(end)):
    if i>= start and v:
        print(i)


# ver2. math 라이브러리 사용 안 했을때 (400ms) -> 사용 했을 때 (396ms) 크게 차이 x

def erastosSieve(start, end): # 시작, 끝 범위 수 입력
    import math

    erastos = [True] * (end + 1) # 소수 판별 여부를 담는 리스트 (0 ~ n까지)
    erastos[0], erastos[1] = False, False # 0과 1은 소수가 아니므로 False로 초기화
    
    for i in range(2, int(math.sqrt(end)) + 1): # 시간 단축하기 위해 제곱근 사용
        if erastos[i] == True: # i가 소수인 경우
            j = 2
            while i * j <= end:
                erastos[i * j] = False # i를 제외한 i의 모든 배수 지우기
                j += 1
    
    for i in range(start, end + 1):
        if erastos[i]:
            print(i)

start, end = map(int, input().split())
erastosSieve(start, end)
