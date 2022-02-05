from typing import List


def find_secondary_small_num(numbers: List[int]) -> int:

    smallest, second_smallest = float('inf'), float('inf')

    for num in numbers:
        if num <= smallest:
            second_smallest, smallest = smallest, num
        elif num > smallest and num < second_smallest:
            second_smallest = num

    return second_smallest


if __name__ == '__main__':
    # returns 2
    print(find_secondary_small_num([1, 3, 5, 7, 3, 8, 2, 5]))