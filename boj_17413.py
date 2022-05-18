# 단어 뒤집기 2
# 태그만 있으면 안에 문자만 바꿔서 출력

s = "baekjoon online judge"
# s = "one1 two2 three3 4fourr 5five 6six"

def reverse_word(s): # 동작 가능 -> 서브함수에 넣어보기
    s_list = s.split(" ")
    new_s = ""
    for i in range(len(s_list)):
        if i == len(s_list):
            new_s = s_list[i][::-1]
        else:
            new_s += s_list[i][::-1] + " "
    return new_s

print(reverse_word(s))


# s = "<   space   >space space space<    spa   c e>"
# idx_1 = s.find("<")
# idx_2 = s.find(">")
# dump1 = s[:(idx_2 - idx_1) +1]

# print(s.find("<"))
# print(s.find(">"))
# print(len(s))
# print(s[:(idx_2 - idx_1) +1]) # <   space   >
# print(s.split(dump1))         # ['', 'space space space<    spa   c e>']


# <   space   >space space space<    spa   c e>
# 124ms 리스트 풀이
s = list(input())
result = []
tmp = []
i = 0

while len(s) > i :
    if s[i] == '<':    # '<' 를 만났을때
        if len(tmp) != 0: # tmp의 길이가 0이 아닐때 = 뒤집어야 되는 단어가 있을때
            for j in range(len(tmp)): # tmp의 길이만큼 반복
                result.append(tmp.pop()) # tmp 리스트에서 pop해서 result 리스트에 append해줌
        result.append(s[i]) # '<'를 append해줌 
        i += 1
       
        while s[i] != '>':  # '>'를 만날때까지 반복
            result.append(s[i]) # 괄호안에 있는 문자들은 뒤집지 않기 때문에 바로 result 리스트에 append해줌
            i += 1
        result.append(s[i]) # '>'를 append해줌
        i += 1
    
    elif s[i] == ' ': # 공백일 때 (위 코드와 동일)
        count = len(tmp)
        for j in range(len(tmp)): 
            result.append(tmp.pop()) 
        result.append(s[i]) # 공백을 append해줌 
        i += 1

    # 그냥 평범한 글자일때 (=숫자, 문자일때)
    else:
        tmp.append(s[i]) # 뒤집어야되는 글자들이기 때문에 result가 아닌 tmp에 넣어줌
        i += 1

# 입력받은 문자열로 while문을 돌고 나왔을때
# tmp 길이가 0이 아니라는 것은 뒤집어야 되는 단어가 있다는 뜻
if len(tmp) != 0: # 위 코드와 동일
    for j in range(len(tmp)): 
        result.append(tmp.pop()) 

print(''.join(result))



