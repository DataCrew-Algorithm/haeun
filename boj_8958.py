t = int(input())            # 테스트 케이스 수

for i in range(t):              # 테스트 케이스 수 만큼 반복
    score = 0                   # 개별 퀴즈 점수 리스트
    f_score = []                # 개별 퀴즈 점수 누적
    ox_answer = list(input())   # OX 퀴즈 인풋값 리스트

    for i in range(len(ox_answer)): # OX 퀴즈 대답 길이 만큼 반복
        if ox_answer[i] == 'O':     # 'O'이 있으면 1점 추가, 최종 점수에 연속해서 스코어만큼 추가하고 누적 리스트에 넣기
            score += 1
            f_score.append(score)
        else:                       # if 조건이 아닐 때는 무조건 0
            score = 0
    print(sum(f_score))   # 케이스 별 점수 합계 출력