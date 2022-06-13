V, E = map(int, input().split())

adj_arr = [[0]*(V+1) for _ in range(V+1)]

for i in range(E):
    start, end = map(int, input().split())
    adj_arr[start][end] = 1
    adj_arr[end][start] = 1

visited = []
Queue = [1]

while Queue:
    current = Queue.pop(0)
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if adj_arr[current][destination] and destination not in visited:
            Queue.append(destination)
            
print(visited)
