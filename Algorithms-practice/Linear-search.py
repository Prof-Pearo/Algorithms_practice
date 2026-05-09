from typing import List


def linear_search(arr: List[int], target: int) -> int:
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    numbers = [4, 2, 7, 1, 9]

    target = 7

    result = linear_search(numbers, target)

    print(f"Target index: {result}")
