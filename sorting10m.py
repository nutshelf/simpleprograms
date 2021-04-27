"""
Дан массив размер 10кк элементов типа int, все элементы массива  > 0, расставлены в произвольном порядке, значения
элементов могут повторятся, значения произвольны. Найти все простые числа. Записать их по порядку в другой массив, можно
 не упорядочивать.

 Считаем, что повторы не надо записывать.
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
    a.insert(i, x)
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
    Function for search in sorted list of elements in increasing order
    output is [string, index to insert x]. Sorted order will be saved
    ['exact', i]        if a[i] == x
    ['range', i]        if a[i-1] < x < a[i], inserting at a[i]
    ['lower', 0]        if x < a[0]
    ['upper', len(a)]   if x > a[-1]
    """
    time0 = time.time()
    lb = 0
    ub = len(a) - 1
    if not a:  # no elements in list
        return ['upper', 0]
    if ub == 0:  # one element in list
        if x < a[0]:
            output = ['low', 0]
        elif x > a[0]:
            output = ['upper', 1]
        else:
            output = ['exact', 0]
        return output
    while not (lb + 1 == ub):
        mid = int((lb + ub) / 2)
        if x < a[mid]:
            ub = mid
        else:
            lb = mid
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
        raise ValueError('Error in func item_in_list_binary_search')
    return output


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
    for i in range(num):
        x = int(rnd() * 10000 + 2)

        time1 = time.time()
        is_prime_bool = is_prime(x)
        time_prime_total += time.time() - time1

        time2 = time.time()
        x_in_a_result = item_in_list_binary_search(a, x)
        x_in_a_bool = x_in_a_result[0] == 'exact'
        time_find_duplicates_total += time.time() - time2

        time3 = time.time()
        if not x_in_a_bool and is_prime_bool:
            add(a, x, x_in_a_result[1])
        time_add_list_total += time.time() - time3

    print(f"Num of source numbers: {num:_}")
    print(f"Num of prime numbers: {len(a):_}")
    print(f"Total time FOR x {num:_}: {time.time() - start_time:.3}s")
    print(f" time for prime checking: {time_prime_total:.3}s")
    print(f" time for finding duplicates in a: {time_find_duplicates_total:.3}s")
    print(f" time for adding results to list: {time_add_list_total:.3}s")
    # 10m => 70s

    print_a(a[0:50], 30)
    print("...", end="")
    print_a(a[-50:], 30)
    print()
    return


main()
