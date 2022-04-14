# 저항
# Ver.1: fail 
# ==> black일때 1인데 문제에서 원하는 답은 문자로 찍는 형태 말고 정수형인 것을 알게 됨
# 예시에 나오지 않는 경우의 수도 직접 넣어서 해보는 게 빠른 것 같다. (그리고 저항값이라서 정수 자료형으로 힌트를 준 듯)

# color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
# num = []

# for _ in range(3):
#     c = input()
#     idx = color.index(c)
#     num.append(idx)  

# if num[2] == 0:
#     print(str(num[0])+str(num[1])+"1")
# else:
#     print(str(num[0])+str(num[1])+num[2]*"0")

# Ver.2 (76ms)
# 1. 입력값인 색을 숫자로 변환, 연산해야 되므로 인덱스 찾고,
# 2. 출력값 형태인 값으로 (10a+b)*(10**c)로 바로 출력하여 답을 찾음

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'] # 저항의 색 리스트
num = [] # 인덱스를 저장할 리스트

for _ in range(3):
    c = input()
    idx = color.index(c)
    num.append(idx)  

print((10*num[0]+num[1])*(10 ** num[2]))    

