"""
There are 10'000'000 int numbers, all greater then null, numbers are random from [1, 10^6]. Array of this numbers
is not sorted. Numbers can repeat in array. Task is to find prime numbers and put then in ascending order in new array.
Prime numbers in new array must not repeat.

Исходный текст (отличающийся по условиям), из которого родилась задача:
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


def binary_search(a: list, x):
    """
    Function for search in increasing order sorted list.
    Output is [True/False(string in prev version), int]. Last one is index where to insert x.
    Sorted order will be saved after inserting.
    [True/'exact', i]        if a[i] == x
    [False/'range', i]        if a[i-1] < x < a[i], inserting at a[i]
    [False/'lower', 0]        if x < a[0]
    [False/'upper', len(a)]   if x > a[-1]
    """
    lb = 0
    ub = len(a) - 1
    if not a:  # no elements in list
        return [False, 0]
        # return ['upper', 0]
    if ub == 0:  # one element in list
        if x < a[0]:
            output = [False, 0]
            # output = ['low', 0]
        elif x > a[0]:
            output = [False, 1]
            # output = ['upper', 1]
        else:
            output = [True, 0]
            # output = ['exact', 0]
        return output

    while not (lb + 1 == ub):
        mid = int((lb + ub) / 2)
        if x < a[mid]:
            ub = mid
        else:
            lb = mid

    if x == a[lb]:
        output = [True, lb]  
        # output = ['exact', lb]
    elif x == a[ub]:
        output = [True, ub]
        # output = ['exact', ub]
    elif a[lb] < x < a[ub]:
        output = [False, ub]
        # output = ['range', ub]
    elif x < a[lb]:
        output = [False, 0]
        # output = ['low', 0]
    elif x > a[ub]:
        output = [False, ub + 1]
        # output = ['upper', ub + 1]
    else:
        raise ValueError('Error in func binary_search')
    return output


def print_fw(list1, row_width, rest_width=None):
    """
    Prints strings with fixed max length(width).
    First arg is List or String
    Function return rest_width - number of symbols in last output row to print to fixed width 'row_width' - which
    can be used in next function call
    """
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


def main(num=10 * 1000 * 1000):
    a = []
    rnd_a = 1
    rnd_b = 1000*1000  # random from [a, b]
    start_time = time.time()
    
    # time_prime_total = 0.0
    # time_find_duplicates_total = 0.0
    # time_add_list_total = 0.0
    # 
    # exact_total_count = 0
    # range_total_count = 0
    # low_total_count = 0
    # upper_total_count = 0
    # low_numbers = []
    # upper_numbers = []

    for i in range(num):
        x = int(rnd() * rnd_b + rnd_a)  # [a, b]

        # time_prime = time.time()
        is_prime_bool = is_prime(x)
        # time_prime_total += time.time() - time_prime
        if is_prime_bool:

            # time_find = time.time()
            x_in_a = binary_search(a, x)
            # time_find_duplicates_total += time.time() - time_find
            # if x_in_a_result[0] == 'exact':
            #     exact_total_count += 1
            if not x_in_a[0]:
                # if x_in_a_result[0] == 'range':
                #     range_total_count += 1
                # elif x_in_a_result[0] == 'low':
                #     low_total_count += 1
                #     low_numbers.append(x)
                # elif x_in_a_result[0] == 'upper':
                #     upper_total_count += 1
                #     upper_numbers.append(x)

                # time_add = time.time()
                add(a, x, x_in_a[1])
                # time_add_list_total += time.time() - time_add

    print(f"Num of source numbers: {num:_}")
    print(f"Numbers from [{rnd_a}, {rnd_b:_}]")
    print(f"Num of prime numbers: {len(a):_}")
    print(f"Time total: {time.time() - start_time:.4}s")
    # print(f" time for prime checking: {time_prime_total:.3}s")
    # print(f" time for finding duplicates in a: {time_find_duplicates_total:.3}s")
    # print(f"  binary search result: exact - {exact_total_count}")
    # print(f"  binary search result: range - {range_total_count}")
    # print(f"  binary search result: low - {low_total_count}")
    # print(f"   lower numbers:", low_numbers)
    # print(f"  binary search result: upper - {upper_total_count}")
    # print(f"   upper numbers:", upper_numbers)
    # print(f" time for adding results to list: {time_add_list_total:.3}s")

    if len(a) > 101:
        print_fw(a[0:50] + ["..."] + a[-50:], 100)
    else:
        print_fw(a, 100)
    print()
    return


main()
