from typing import List


def get_max_schedule_section(start_times: List[int], end_times: List[int]) -> int:
    num_of_schedule = len(start_times)

    current_end_time = 0
    schedule_count = 0
    for i in range(num_of_schedule):
        end_sorted_index = end_times.index(sorted(end_times)[i])
        if start_times[end_sorted_index] < current_end_time:
            continue

        schedule_count += 1
        print(start_times[end_sorted_index], end='~')
        print(end_times[end_sorted_index])
        current_end_time = end_times[end_sorted_index]

    return schedule_count


if __name__ == '__main__':
    start = [9, 10, 11, 13, 15, 19]
    end = [16, 12, 15, 19, 18, 23]

    print(get_max_schedule_section(start, end))
    # 10~12
    # 15~18
    # 19~23
    # 3