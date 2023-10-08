# array = 배열 데이터
# target = 찾고자 하는 숫자
# start = 시작점 인덱스
# end = 끝점 인덱스
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값인 경우
    if target == array[mid]:
        return mid
    # 원하는 값이 중간값보다 작을 경우
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간값보다 클 경우
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)


# n = 배열의 개수
# target = 찾고자 하는 숫자
n, target = map(int, input().split())

# 배열 데이터
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
print("index:", result)
