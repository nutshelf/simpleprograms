def pow(a, n, depth=1):
    """
    Recursive algorithm with O(log2 (N)) complexity
    """
    if n == 1:
        print("depth=", depth)
        return a
    if n % 2 == 1:
        return pow(a, n-1, depth + 1) * a
    else:  # n % 2 = 0
        return pow(a * a, n // 2, depth + 1)


def main1():
    a = 1.01
    n = 365
    print(pow(a, n))
    print(a ** n)


main1()