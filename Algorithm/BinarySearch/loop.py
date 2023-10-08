def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


# n = 배열의 개수
# target = 찾고자 하는 숫자
n, target = map(int, input().split())

# 배열 데이터
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
print("index:", result)
