def binary_search_left(a: list, x):
    assert a
    left = -1
    right = len(a)

    while True:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid
        else:
            right = mid

    return -1


def binary_search_right(a: list, x):
    assert a
    lb = 0
    ub = len(a) - 1
    return 0


def main():
    a = [0, 1, 2, 2, 3]
    x = 1.1
    left = binary_search_left(a, x)
    right = binary_search_right(a, x)
    print(a, "is a list")
    print(x, "is a value to find in list")
    if right == 0:
        print(x, "isn't found")
        print("0 is position at which value can be inserted: before first element", a[0])
    elif left == len(a) - 1:
        print(x, "isn't found")
        print(left, " is position at which value can be inserted: at the end of list.")
    elif right - left == 1:
        print(x, "isn't found")
        print(right, f" is position at which value can be inserted. Between {a[left]} and {a[right]}")
    elif right > left:
        print("Was found", right - left - 1, "times.")
        print(left + 1, "is it's first position")
        print(right - 1, "is it's last position")
        print(right, "is a position value can be inserted at.")
    return


main()
