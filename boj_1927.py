# 최소 힙
# heap = []            # creates an empty heap 초기 힙 세팅
# heappush(heap, item) # pushes a new item on the heap 힙에 새로운 원소 추가
# item = heappop(heap) # pops the smallest item from the heap 최솟값 출력
# item = heap[0]       # smallest item on the heap without popping it 제거하지 않고 최솟값 확인
# heapify(x)           # transforms list into a heap, in-place, in linear time 리스트-> 힙 변환
# item = heapreplace(heap, item) # pops and returns smallest item, and adds new item; the heap size is unchanged


import sys, heapq

# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례로 heap에 삽입
#     for value in iterable:
#         heapq.heappush(h, value)
#     # 힙에 삽입된 모든 원소를 차례로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))

#     return result


# N = int(input())

# nums = []
# for _ in range(N):
#     num = int(sys.stdin.readline().rstrip())
    
#     if num > 0:
#         nums.append(num)

#     else:
#         nums = heapsort(nums)
#         min_num = heapq.heappop(nums) # IndexError: index out of range
#         print(num)
        
#         if len(nums) == 0:
#             print(0)



N = int(input())

heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    
    if num == 0: # 0일 때 바로 최솟값을 출력하면서 제거해야 하거나 힙이 비었을 때 0 출력
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

    else:
        heapq.heappush(heap, num)  # 자연수일때 원소 추가

    