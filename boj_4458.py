# 첫 글자를 대문자로 바꾸기
# 문자열 전체를 대문자로 바꾸는 'upper'함수 대신 앞글자만 대문자로 바꾸는 'capitalize'함수 사용
# 버전 3개 모두 68ms로 통과됨

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


# Ver.3 예빈님 코드 변형 // title 함수도 활용 가능하다.
# Capitalize함수, title 함수의 차이: "문장의 앞글자를 대문자화 나머지문자 소문자" / "모든 단어의 첫번째 글자를 대문자화"
line_num = int(input())
l = []
for _ in range(line_num):
    s = input()
    new_s = s[0].title() + s[1:] 
    print(new_s)