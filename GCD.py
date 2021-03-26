# Наибольший общий делитель НОД
# Greatest Common Divider GCD
# Euclidean Recursive algorithm & with FOR cycle

import time

def gcd_incycle(a, b):
    op = 0
    while True:
        op += 1
        if a > b:
            a = a % b
            if a == 0:
                return b
        else:
            b = b % a
            if b == 0:
                return a


def gcd_recursive(a, b, op=1):
    """
    In mind a > b, otherwise one recursive call will be done
    """
    if b == 0:
        print("количество вызовов рекурсивной функции =", op)
        return a
    return gcd_recursive(b, a % b, op + 1)


def main1():
    a = 49238281822
    b = 43347347727

    start_time = time.time()
    print("gcd_incycle =", gcd_incycle(a, b))
    print("t=", round(time.time()-start_time, 3))

    start_time = time.time()
    print("gcd_recursive =", gcd_recursive(a, b))
    print("t=", time.time() - start_time)


main1()