# Print Stars : 규칙 찾을 때 조금 더 큰 그림을 보자!

def draw(n, idx):
    if n == 1:
        starMap[idx][idx] = '*'
        return ;
    l = 4 * n -3
    
    for i in range(idx, l+idx):
    	#위 아래
        starMap[idx][i] = '*'
        starMap[idx+l-1][i] = '*'
        
        #양 옆
        starMap[i][idx] = '*'
        starMap[i][idx+l-1] = '*' 
 
    return draw(n-1, idx+2)
    
    
n = int(input())
lens = 4 * n -3

starMap = [[' '] * lens for _ in range(lens)]

draw(n,0)

for i in range(lens):
    for j in range(lens):
        print(starMap[i][j], end="")
    print()


# 재귀함수 없이 푸는 풀이 참고 (by 요셉)
N = int(input())
result = ['*']
for _ in range(N-1):
    result.insert(0, '* ' + ' '*len(result[0]) + ' *')
    result.insert(0, '*'*len(result[0]))
    result.append(result[1])
    result.append(result[0])
    for i, line in enumerate(result[2:-2]):
        result[2+i] = '* ' + line + ' *'

for i in result:
    print(i)



# 리스트 형태로 *을 찍어서 합치고 출력하는 풀이 참고! (by 수현)
def plus_stars(lst): # 이전 번(n-1)의 원소 앞 뒤에 '* ' ' *'를 추가하는 함수
    for j in range(len(lst)):
        lst[j] = '* '+ lst[j] + ' *' # 원래 리스트에 추가해서 담음
    return lst

def stars(n):
    if n == 1:
        return ['*']
    else:
        add1 = '*' * (4 *(n-1)+1)               # 위 아랫줄에 추가 4(n-1) + 1
        add2 = '*' + ' '*(4 * (n-1)-1) + '*'
        return [add1, add2] + plus_stars(stars(n-1)) + [add2, add1]

N = int(input())
print(*stars(N), sep = '\n')

