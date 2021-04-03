# Наибольший общий делитель НОД
# Greatest Common Divider GCD
# Euclidean Recursive algorithm & with FOR cycle


def gcd_incycle(a: int, b: int):
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


def gcd_recursive(a: int, b: int, depth=1):
    """
    In mind a > b, otherwise one additional recursive call for args changing will be done
    """
    if b == 0:
        print("recursive calls =", depth)
        return a
    return gcd_recursive(b, a % b, depth + 1)


def main1():
    a = 18
    b = 15

    gcd1 = gcd_incycle(a, b)
    gcd2 = gcd_recursive(a, b)
    if gcd1 == gcd2:
        print("Results in both methods are EQUAL. GCD is", gcd1)
    else:
        print("Results in two methods are not equal!\n",
              "In cycle method:", gcd1, "\n",
              "Recursive method:", gcd2)


main1()
