"""
Дан массив размер 10кк элементов типа int, все элементы массива  > 0, расставлены в произвольном порядке, значения
элементов могут повторятся, значения произвольны. Найти все простые числа. Записать их по порядку в другой массив, можно
 не упорядочивать.

 Считаем, что повторы не надо.
"""

import time
from math import sqrt as sqrt
from random import random as rnd


def is_prime(x: int):
    if x % 2 == 0:
        if x != 2:
            return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def add(a: list, x: int, i):
    # for i in range(len(a) - 1, -1, -1):
    #     if x > a[i]:
    #         a.insert(i + 1, x)
    #         return
    a.insert(i, x)
    # a.append(x) # simple appending
    return


def print_a(a: list, num_in_row):
    i = 0
    while i < len(a):
        print(a[i], end=" ")
        i += 1
        if i % num_in_row == 0 and i > 0:
            print()
    return


def item_in_list_binary_search(a: list, x):
    """
    Function for search in sorted list of increasing elements
    output is f[0]=string and f[1]=index to insert x. Sorted order will be saved
    ['exact', i]  if a[i] == x
    ['range', i]  if a[i-1] < x < a[i], inserting at a[i]
    ['lower', 0]  if x < a[0]
    ['upper', len(a)]  if x > a[-1]
    """
    time0 = time.time()
    lb = 0
    ub = len(a) - 1
    if not a:  # no elements in list
        return [['upper', 0], [time.time() - time0, 0, 0]]
    if ub == 0:  # one element in list
        if x < a[0]:
            output = ['low', 0]
        elif x > a[0]:
            output = ['upper', 1]
        else:
            output = ['exact', 0]
        return [output, [time.time() - time0, 0, 0]]
    time1 = time.time()
    while not (lb + 1 == ub):
        mid = int((lb + ub) / 2)
        if x < a[mid]:
            ub = mid
        else:
            lb = mid
    time2 = time.time()
    if x < a[lb]:
        output = ['low', 0]
    elif x > a[ub]:
        output = ['upper', len(a)]
    elif x == a[lb]:
        output = ['exact', lb]
    elif a[lb] < x < a[ub]:
        output = ['range', ub]
    elif x == a[ub]:
        output = ['exact', ub]
    else:
        raise ValueError('Some local error')
    return [output, [time.time() - time2, time2 - time1, time1 - time0]]


# def item_in_list_binary_search_r(a: list, x, lb=None, ub=None):
#
#     if not a:
#         return ['upper', 0]
#     if (lb is None) or (ub is None):  # default lower & upper bounds
#         lb = 0
#         ub = len(a) - 1
#     if (lb + 1 == ub) or (lb == ub):
#         if x < a[lb]:
#             return ['low', 0]
#         if x > a[ub]:
#             return ['upper', len(a)]
#         if x == a[lb]:
#             return ['exact', lb]
#         if a[lb] < x < a[ub]:
#             return ['range', ub]
#         if x == a[ub]:
#             return ['exact', ub]
#
#     # one or more elements between lb and ub
#     mid = int((lb + ub) / 2)
#     if x < a[mid]:
#         res = item_in_list_binary_search(a, x, lb, mid)
#     else:
#         res = item_in_list_binary_search(a, x, mid, ub)
#     return res


def main(num=1 * 1000 * 1000):
    a = []
    start_time = time.time()
    time_prime_total = 0.0
    time_find_duplicates_total = 0.0
    time_add_list_total = 0.0
    x_in_a_time1 = 0.0
    x_in_a_time2 = 0.0
    x_in_a_time3 = 0.0
    for i in range(num):
        x = int(rnd() * (10 ** (rnd() * 5)) + 2)
        #print(x, a)

        time1 = time.time()
        is_prime_bool = is_prime(x)
        time_prime_total += time.time() - time1

        time2 = time.time()
        x_in_a_result = item_in_list_binary_search(a, x)
        x_in_a_bool = x_in_a_result[0][0] == 'exact'
        x_in_a_time1 += x_in_a_result[1][0]
        x_in_a_time2 += x_in_a_result[1][1]
        x_in_a_time3 += x_in_a_result[1][2]
        time_find_duplicates_total += time.time() - time2

        time3 = time.time()
        if not x_in_a_bool and is_prime_bool:
            add(a, x, x_in_a_result[0][1])
        time_add_list_total += time.time() - time3

    print(f"Num of source numbers: {num:_}")
    print(f"Num of prime numbers: {len(a):_}")
    print(f"Total time FOR x {num:_}: {time.time() - start_time:.3}s")
    print(f"Total time for prime checking: {time_prime_total:.3}s")
    print(f"Total time for finding duplicates in a: {time_find_duplicates_total:.3}s")
    print(f"- special cases checking: {x_in_a_result[1][0]:.3}s")
    print(f"- binary searching: {x_in_a_result[1][1]:.3}s")
    print(f"- choice selecting: {x_in_a_result[1][2]:.3}s")
    print(f"Total time for adding results to list: {time_add_list_total:.3}s")
    # 1m elements => 32s
    # 2m elements binary search => 30s

    # print_a(a, 30)
    print()
    return


main()
