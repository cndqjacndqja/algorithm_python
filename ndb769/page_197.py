n = int(input())

data1 = list(map(int, input().split()))

m = int(input())
data2 = list(map(int, input().split()))




def binary_search(graph, target, start, end):
    if start > end:
        return None
    mid = (end + start) // 2

    if graph[mid] == target:
        return mid
    elif graph[mid] > target:
        return binary_search(graph, target, start, mid - 1)
    elif graph[mid] < target:
        return binary_search(graph, target, mid + 1, end)


for i in data2:
    if binary_search(data1, i, 0, len(data1) - 1) is not None:
        print("yes")
    else:
        print("no")
