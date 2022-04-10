# 수 정렬하기
# Ver.1 (108ms)

# line_num = int(input())
# arr = [int(input()) for _ in range(line_num)]
# arr = sorted(arr)
# print(*arr, sep="\n")



# Ver.2 (퀵 정렬) 런 타임 에러??

num = int(input())
arr = [int(input()) for _ in range(num)]
new_arr = []

def AscendingSort(arr):
    if len(arr) < 1:
        return arr

    # 비교점
    compare_point = arr[0]
    others = arr[1:]
    left_side = [i for i in others if i <= compare_point]
    right_side = [i for i in others if i > compare_point]
    new_arr = left_side+ [compare_point] + right_side
    
    return new_arr

print(*new_arr, sep="\n")
