from typing import List


def is_value_in_list(li: List[int], value: int) -> bool:
    left = 0
    right = len(li) - 1
    while right >= left:
        middle = (right + left) // 2
        if li[middle] == value:
            return True
        elif li[middle] > value:
            right = middle - 1
        elif li[middle] < value:
            left = middle + 1

    return False


if __name__ == '__main__':
    array = [1, 3, 4, 5, 7, 10, 15, 18, 20]
    is_5 = is_value_in_list(array, 5)
    is_6 = is_value_in_list(array, 6)
    is_12 = is_value_in_list(array, 12)
    is_15 = is_value_in_list(array, 15)
    is_20 = is_value_in_list(array, 20)
    print(is_5)
    # true
    print(is_6)
    # false
    print(is_12)
    # false
    print(is_15)
    # true
    print(is_20)
    # true
