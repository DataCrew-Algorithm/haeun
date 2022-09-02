# 코데 데모, 직사각형 만들기 (https://school.programmers.co.kr/learn/courses/18/lessons/1878)

# 직사각형을 만드는데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한점의 좌표를 구하려고함
# 좌표를 v 배열에 담아서 준다. 직사각형은 x, y축에 평행하며 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어짐
# v는 3개 좌표가 들어있는 2차원 배열
# v는 각 원소는 [x축좌표, y축좌표], 좌표값은 1이상 10억 이하의 자연수
v = [[1, 4], [3, 4], [3, 10]] #-> [1, 10]
# v = [[1, 1], [2, 2], [1, 2]] -> [2, 1]

# def solution(v):
#     answer = []

#     for loc in list(zip(*v)):
#         print(loc)
#         # x, y = loc[0], loc[1]


#     return answer

# length = []
# for i in range(len(v)-1):
#     print(v[i], v[i][0], v[i][1] )
#     print(v[i+1], v[i+1][0], v[i+1][1])


# 길이로 푸는게 아니라 중복여부를 파악하면 빠르게 풀 수 있다.

def solution(v):
    x = []
    y = []

    for i in v:
        if i[0] not in x:
            x.append(i[0])
        else:
            x.remove(i[0])
        
        if i[1] not in y:
            y.append(i[1])
        
        else:
            y.remove(i[1])
    
    answer = x + y

    return answer

print(solution(v))