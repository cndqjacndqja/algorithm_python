# 이진 탐색 구현

# def binary_search(data, target):
#     start = 0
#     end = len(data)-1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return mid
#         if data[mid] < target:
#             start = mid + 1
#         elif data[mid] > target:
#             end = mid - 1
#     return None

def binary_search(start, end, target, data):
    if start > end:
        return None
    mid = (start+end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        binary_search(mid+1, end, target, data)
    elif data[mid] > target:
        binary_search(start, mid-1, target, data)

