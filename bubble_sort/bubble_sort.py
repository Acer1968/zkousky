import random
import datetime

def timed_test(func):
    def timed(*arg, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*arg, **kwargs)
        end_time = datetime.datetime.now()
        print(f"START čas: {start_time}")
        print(f"KONEC čas: {end_time}")
        return result
    return timed

@timed_test
def mybubble(array):
    sorted_array = [array[0]]
    for x in array[1:]:
        bigger_found = False
        for y in sorted_array:
            if x < y:
                sorted_array.insert(sorted_array.index(y),x)
                bigger_found = True
                break
        if not bigger_found:
            sorted_array.append(x)
    return sorted_array

@timed_test
def mybubble2(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - j - 1):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]
    return array

@timed_test
def mybubble3(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - j - 1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array


arr = [random.choice(range(50)) for i in range(500)]
#arr = [37, 34, 15, 12, 9, 26, 21, 39, 13, 5, 1, 37, 5, 37, 8, 43, 9, 43, 30, 10]
print(arr)

sort_arr = mybubble(arr)
print(sort_arr)

sort_arr2 = mybubble2(arr)
print(sort_arr2)

sort_arr2 = mybubble2(arr)
print(sort_arr2)