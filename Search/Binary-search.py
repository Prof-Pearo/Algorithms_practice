from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11]

    target = 7

    result = binary_search(numbers, target)

    print(f"Target index: {result}")
