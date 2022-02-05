from typing import List


def is_partial_sum_bit_search(num: int, sum: int, numbers: List[int]) -> bool:
    
    for bit in range(1 << num):
        candidate = 0
        for i in range(num):
            if bit & 1 << i:
                candidate += numbers[i]
        
        if candidate == sum:
            return True
    
    return False


def is_partial_sum_recursive(num: int, sum: int, numbers: List[int]) -> bool:

    if num == 0 and sum == 0:
        return True
    elif num == 0 and sum != 0:
        return False

    return is_partial_sum_recursive(num - 1, sum - numbers[0], numbers[1:]) \
        or is_partial_sum_recursive(num - 1, sum, numbers[1:])


if __name__ == '__main__':
    # true
    print(is_partial_sum_bit_search(5, 10,  [1, 2, 4, 5, 11]))
    # false
    print(is_partial_sum_bit_search(4, 10, [1, 5, 8, 11]))
    # true
    print(is_partial_sum_recursive(5, 10,  [1, 2, 4, 5, 11]))
    # false
    print(is_partial_sum_recursive(4, 10, [1, 5, 8, 11]))

