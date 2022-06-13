# a, b = map(int,input().split())
# seq = [] #sequence

# for i in range(b):
#     for _ in range(i):
#         seq.append(i)
#         s = sum(seq[a-1:b])

# print(s)

a, b = map(int,input().split())
seq = [] #sequence

for i in range(1, b):
    for _ in range(i):
        seq.append(i)
        
print(sum(seq[a-1:b]))