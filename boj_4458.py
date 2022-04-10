# 첫 글자를 대문자로 바꾸기
# 문자열 전체를 대문자로 바꾸는 'upper'함수 대신 앞글자만 대문자로 바꾸는 'capitalize'함수 사용

# Ver.1
line_num = int(input())

for i in range(line_num):
    sentence = input()
    print(sentence[0].capitalize()+sentence[1:])


# Ver.2 리스트 형
line_num = int(input())
new_sentences = []

for i in range(line_num):
    sentence = input()
    new_sentences.append(sentence[0].capitalize()+sentence[1:])
print(*new_sentences, sep = "\n")


