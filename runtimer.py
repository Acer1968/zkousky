import random
import datetime
import time
import functools


def calculate_runtime_deltatime(myfunct):
    def wrap(*arg, **kwargs):
        start_time = datetime.datetime.now()
        result = myfunct(*arg, **kwargs)
        end_time = datetime.datetime.now()
        print(f"START čas: {start_time}")
        print(f"KONEC čas: {end_time}")
        result_time = end_time - start_time
        show_time_micro = result_time.microseconds
        show_time_sec = result_time.seconds
        print(f'=== {show_time_sec} seconds {show_time_micro} microseconds {"=" * 30}')
        return result
    return wrap


def calculate_runtime_monotonic(myfunct):
    @functools.wraps(myfunct)
    def wrap(*args, **kwargs):
        start_time = time.monotonic()
        result = myfunct(*args, **kwargs)
        end_time = time.monotonic()
        print(f"START čas: {start_time}")
        print(f"KONEC čas: {end_time}")
        result_time = end_time - start_time
        # save result
        # resulting_times[myfunct.__name__].append(taken_time)
        show_time = round(result_time * 10e6, 3)
        print(f'=== {show_time} microseconds {"=" * 30}')
        return result
    return wrap


@calculate_runtime_deltatime
def mybubble(array):
    sorted_array = [array[0]]
    for x in array[1:]:
        bigger_found = False
        for y in sorted_array:
            if x < y:
                sorted_array.insert(sorted_array.index(y), x)
                bigger_found = True
                break
        if not bigger_found:
            sorted_array.append(x)
    return sorted_array


@calculate_runtime_deltatime
def mybubble2(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - j - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]
    return array


@calculate_runtime_deltatime
def mybubble3(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - j - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    return array


arr = [random.choice(range(500)) for i in range(5000)]
# arr = [37, 34, 15, 12, 9, 26, 21, 39, 13, 5, 1, 37, 5, 37, 8, 43, 9, 43, 30, 10]
# print(arr)

sort_arr = mybubble(arr)
# print(sort_arr)

sort_arr2 = mybubble2(arr)
# print(sort_arr2)

sort_arr2 = mybubble2(arr)
# print(sort_arr2)
