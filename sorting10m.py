"""
There are 10'000'000 int numbers, all greater then null. Array of this numbers is not sorted. Numbers can repeat
in array. Task is to find prime numbers and put then in ascending order in new array. Prime numbers in new array
must not repeat.

Исходный текст (отличающийся по условиям), из которого родился алгоритм ниже:
"Дан массив размер 10кк элементов типа int, все элементы массива  > 0, расставлены в произвольном порядке, значения
элементов могут повторятся, значения произвольны. Найти все простые числа. Записать их по порядку в другой массив, можно
 не упорядочивать."
"""

import time
from math import sqrt as sqrt
from random import random as rnd


def is_prime(x: int):
    if x == 1:
        return False
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


def print_fw(list1, row_width, rest_width=None):
    """
    Prints strings with fixed max length(width).
    First arg is List or String
    Function return rest_width - number of symbols in last output row to print to fixed width 'row_width'
    """
    if type(list1) is str:
        list1 = [list1]
    if rest_width is None:
        rest_width = row_width

    for i in range(0, len(list1)):
        elem_length = len(str(list1[i]))
        if elem_length > rest_width:
            print()
            rest_width = row_width
        rest_width -= elem_length + 1
        print(list1[i], end=" ")
    return rest_width


def binary_search(a: list, x):
    """
    Function for search in sorted in increasing order list of elements.
    Output is [True/False, int]. Last one is index where to insert x. Sorted order will be saved after inserting.
    ['exact', i]        if a[i] == x
    ['range', i]        if a[i-1] < x < a[i], inserting at a[i]
    ['lower', 0]        if x < a[0]
    ['upper', len(a)]   if x > a[-1]
    """
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

    if a[lb] < x < a[ub]:
        output = ['range', ub]
    elif x < a[lb]:
        output = ['low', 0]
    elif x > a[ub]:
        output = ['upper', len(a)]
    elif x == a[lb]:
        output = ['exact', lb]
    elif x == a[ub]:
        output = ['exact', ub]
    else:
        raise ValueError('Error in func binary_search')
    return output


def main(num=10 * 1000 * 1000):
    a = []
    start_time = time.time()
    time_prime_total = 0.0
    time_find_duplicates_total = 0.0
    time_add_list_total = 0.0

    exact_total_count = 0
    range_total_count = 0
    low_total_count = 0
    upper_total_count = 0
    low_numbers = []
    upper_numbers = []

    for i in range(num):
        x = int(rnd() * 1000000000 + 1)  # [1, 1'000'000'000]

        time1 = time.time()
        is_prime_bool = is_prime(x)
        time_prime_total += time.time() - time1

        time2 = time.time()
        x_in_a_result = binary_search(a, x)
        x_in_a_bool = x_in_a_result[0] == 'exact'
        time_find_duplicates_total += time.time() - time2

        if x_in_a_result[0] == 'exact':
            exact_total_count += 1

        time3 = time.time()
        if not x_in_a_bool and is_prime_bool:
            if x_in_a_result[0] == 'range':
                range_total_count += 1
            elif x_in_a_result[0] == 'low':
                low_total_count += 1
                low_numbers.append(x)
            elif x_in_a_result[0] == 'upper':
                upper_total_count += 1
                upper_numbers.append(x)
            add(a, x, x_in_a_result[1])
        time_add_list_total += time.time() - time3

    print(f"Num of source numbers: {num:_}")
    print(f"Num of prime numbers: {len(a):_}")
    print(f"Total time FOR x {num:_}: {time.time() - start_time:.4}s")
    print(f" time for prime checking: {time_prime_total:.3}s")
    print(f" time for finding duplicates in a: {time_find_duplicates_total:.3}s")
    print(f"  binary search result: exact - {exact_total_count}")
    print(f"  binary search result: range - {range_total_count}")
    print(f"  binary search result: low - {low_total_count}")
    print(f"   lower numbers:", low_numbers)
    print(f"  binary search result: upper - {upper_total_count}")
    print(f"   upper numbers:", upper_numbers)
    print(f" time for adding results to list: {time_add_list_total:.3}s")

    if len(a) > 101:
        rest_width = print_fw((a[0:50]), 100)
        rest_width = print_fw("...", 100, rest_width)
        print_fw(a[-50:], 100, rest_width)
    else:
        print_fw(a, 100)
    print()
    return


main()
