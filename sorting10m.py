"""
Дан массив размер 10кк элементов типа int, все элементы массива  > 0, расставлены в произвольном порядке, значения
элементов могут повторятся, значения произвольны. Найти все простые числа. Записать их по порядку в другой массив, можно
 не упорядочивать.

 Считаем, что повторы не надо.
"""


from random import random as rnd


def is_prime(x: int):
    if x % 2 == 0 and x != 2:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True


def add(a: list, x: int):
    for i in range(len(a) - 1, -1, -1):
        if x > a[i]:
            a.insert(i + 1, x)
            return
    a.insert(0, x)
    return


def print_a(a: list):
    print(a[0], end=" ")
    i = 1
    while i < len(a):
        print(a[i], end=" ")
        i += 1
        if i % 10 == 0:
            print()
    return


def main():
    a = []
    max = 0
    for i in range(1000000):
        x = int(rnd() * 10 ** (rnd() * 5)) + 2
        if x > max:
           max = x
        #print(x, end=" ") #output all numbers
        if not (x in a) and is_prime(x):
            add(a, x)
    print("max num at all:", max)
    if a:
        #print("All prime numbers in ascending order:")
        #print_a(a)
        print("Quantity of numbers", len(a))
    else:
        print("There were no prime numbers")
    return


main()
