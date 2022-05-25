# Reverse Words

# Ver1. 72ms
N = int(input())
sequence = []

for i in range(N):
    case = input().split()
    sequence.append(case[::-1]) # 뒤집은 문자열 추가

num = 0
for i in range(len(sequence)):
    num += 1
    print(f"Case #{num}:", " ".join(sequence[i]))


# Ver2. 68ms
N = int(input())

for i in range(N):
    i += 1
    case = input().split()
    print(f"Case #{i}:", " ".join(case[::-1])) # 뒤집은 문자열로 출력