from typing import List


def get_min_of_pushing_button(a: List[int], b: List[int]):
    i = len(a) - 1
    push_counter = 0

    while i >= 0:
        if a[i] % b[i] != 0:
            ith_push_num = b[i] - a[i] % b[i]
            push_counter += ith_push_num

            for j in range(i + 1):
                a[j] += ith_push_num

        i -= 1

    print(a)
    print(b)
    return push_counter


def get_min_of_pushing_button_v2(a: List[int], b: List[int]):
    i = len(a) - 1
    push_counter = 0

    while i >= 0:
        a[i] += push_counter
        if a[i] % b[i] != 0:

            ith_push_num = b[i] - a[i] % b[i]
            push_counter += ith_push_num
            a[i] += ith_push_num

        i -= 1

    print(a)
    print(b)
    return push_counter


if __name__ == '__main__':

    a_li = [13, 15, 17, 12, 18, 10, 19, 17]
    b_li = [2, 4, 6, 8, 3, 9, 4, 7]
    print(get_min_of_pushing_button(a_li, b_li))
    a_li = [13, 15, 17, 12, 18, 10, 19, 17]
    b_li = [2, 4, 6, 8, 3, 9, 4, 7]
    print(get_min_of_pushing_button_v2(a_li, b_li))

