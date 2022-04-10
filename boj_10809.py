# 소문자별 인덱스 체크
# 알파벳은 26글자, 단어 길이 수 1~100 까지 있다!
# word = input() # 입력 받은 단어 스펠링을 오름차순으로 정렬

word = 'baekjoon'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
order_lists = [-1]*26 # 철자 인덱스가 0부터 시작함 & 알파벳이 없다는 전제로 출발

'''
# Ver1.

for cha in word:                                  # 단어의 길이만큼 cha 1개씩 찾음   
    for i, alp in enumerate(alphabet):            # 알파벳 철자별 인덱스와 함께 출력 (enumerate 함수)
        if cha  == alp :                          # 인풋 철자와 알파벳이 같으면 
            if order_lists[i] == -1:              # 순서 리스트의 위치 값이 초깃값과 같은가?
                order_lists[i] = word.index(cha)  # 순서 리스트의 위치에 단어의 해당 철자 인덱스를 넣음

for i in order_lists:
    print(i, end = " ")
'''

for alp in alphabet:
    i = word.find(alp) # 인풋받은 단어에서 철자의 인덱스를 찾음
    if i != -1 :       # 해당 알파벳이 있으면 (없으면 -1이 나옴; find 함수 특성*)
        if order_lists[alphabet.index(alp)] == -1: # 초깃값 -1이 아니면 (중복 character 경우 중복 입력 방지)
            order_lists[alphabet.index(alp)] = i   # 순서 리스트의 철자 인덱스 위치에 인덱스를 넣음

for i in order_lists:
    print(i, end = " ")


