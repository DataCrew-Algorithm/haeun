# FBI 찾기 (68ms)
# FBI요원은 요원의 첩보원명에 FBI가 들어있다.
# 입력되는 첩보원 명 5개로 문제에서 주어짐
code = [input() for i in range(5)]
idx = []

# FOR문으로 FBI인지 5번 반복, 코드에 'FBI'글자 있으면 해당 코드 index를 1더하여 리스트에 넣고
for i in range(5):
    if "FBI" in code[i]:
        idx.append(i+1)

# 인덱스 리스트의 길이(첩보원 유무) 1이상이면 오름차순으로 공백 추가하여 출력, 아닐 시 도망쳤다 출력
if len(idx) >= 1:
    print(*sorted(idx), sep=" ")
else: 
    print("HE GOT AWAY!")

