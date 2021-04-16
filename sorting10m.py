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
    for i in range(3, int(sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True


def add(a: list, x: int):
    for i in range(len(a) - 1, -1, -1):
        if x > a[i]:
            a.insert(i + 1, x)
            return
    a.insert(0, x)
    # a.append(x) # simple appending
    return


def print_a(a: list, num_in_row):
    print(a[0], end=" ")
    i = 1
    while i < len(a):
        print(a[i], end=" ")
        i += 1
        if i % num_in_row == 0:
            print()
    return


def item_in_list_binary_search(a: list, x, lb=None, ub=None):
    if lb == None:
        lb = 0
    if ub == None:
        ub = len(a)
    mid = int((lb + ub) / 2)
    #desc order list
    if a[0] < a[-1]:
        mn = 1
    elif a[0] > a[-1]:
        mn = -1
    else: # a[0] == a[-1] --> len = 1


        if a[mid] < x:
            res = item_in_list_binary_search(a, x, mid, ub)
        elif x < a[mid]:
            res = item_in_list_binary_search(a, x, lb, mid)
        else:
            return [mid]



    # old slowest algorithm
    # for i in range(len(a)):
    #     if a[i] == x:
    #         return True
    # return False


def main(num=1*100*1):
    a = []
    start_time = time.time()
    time_prime_total = 0.0
    time_find_dupls_total = 0.0
    time_add_list_total = 0.0
    for i in range(num):
        x = int(rnd() * (10 ** (rnd() * 5)) + 2)

        time1 = time.time()
        is_prime_bool = is_prime(x)
        time_prime_total += time.time() - time1

        time2 =  time.time()
        x_in_a_bool = item_in_list_binary_search(a, x)
        time_find_dupls_total += time.time() - time2

        if not x_in_a_bool and is_prime_bool:
            time3 = time.time()
            add(a, x)
            time_add_list_total += time.time() - time3

    print(f"Num of source numbers: {num:_}")
    print(f"Num of prime numbers: {len(a):_}")
    print(f"Total time FOR x {num}: {time.time() - start_time:.3}s")
    print(f"Total time for prime checking: {time_prime_total:.3}s")
    print(f"Total time for finding duplicates in a: {time_find_dupls_total:.3}s")
    print(f"Total time for adding results to list: {time_add_list_total:.3}s")
    # 1m elements => 32s

    print_a(a, 30)
    print()
    return


main()
