# 학급회장 선발

N = int(input())
votes = []
frequency_2 = []
frequency_3 = []
scores = []

for _ in range(N):
    vote = list(map(int, input().split()))
    votes += vote

print(votes)

for i in range(3):
    scores.append(sum(votes[i:N*3:3]))             # 후보 별 점수 합산하여 리스트에 넣기
    frequency_2.append(votes[i:N*3:3].count(2))    # 후보 별 2점 빈도 구하여 리스트에 넣기
    frequency_3.append(votes[i:N*3:3].count(3))    # 후보 별 3점 빈도 구하여 리스트에 넣기

def find_president(scores):       # 최대값을 구하기 위한 함수
    max_score = scores[0]  # 리스트 첫 값을 최대값으로 기본 설정
    max_freq = frequency_3[0]
    max_freq2 = frequency_2[0]
    candidate_num = 0

    for i in range(1, 3): # 처음 값은 비교할 필요가 없으므로 1부터 반복문시작
        if max_score < scores[i]:
            max_score = scores[i]  # 비교후 max값 변경
            candidate_num = i
        if max_score == scores[i]:          # 첫번째 값과 이후의 값을 비교했을 때 같을 때
            if max_freq > frequency_3[i]:
                candidate_num = 1
            if max_freq == frequency_3[i]:
                max_freq2 > frequency_2[i]
                candidate_num = 1
                if max_freq2 == frequency_2[i]:
                    candidate_num = 0
                
    return candidate_num, max_score   # 후보 번호, max값을 반환

print(*(find_president(scores)))

