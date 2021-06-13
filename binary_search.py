def binary_search_left(a: list, x):
    """
    Return NEAREST PREVIOUS index of occurrence of X (or possible occurrence of X) in list.
    Ex:
        binary_search_left([2, 4, 5, 6], 3) = 0
        binary_search_left([2, 2, 3, 3], 3) = 1
    """
    assert a
    left = -1
    right = len(a)
    mid = 0
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid
        else:
            right = mid
    return left


def binary_search_right(a: list, x):
    """
    Return NEAREST NEXT index of X occurrence (possible occurrence) in list.
    Ex:
        binary_search_right([2, 4, 5, 6], 3) = 1
        binary_search_right([2, 2, 3, 3], 3) = 4
    """
    assert a
    left = -1
    right = len(a)
    mid = 0
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid
        else:
            right = mid
    return right


def main():
    a = [-12, -1, 333, 344, 554]
    x = 111
    left = binary_search_left(a, x)
    right = binary_search_right(a, x)

    print(a, "is a list")
    print(x, "is a value to find in list")
    if right == 0:
        print(x, "wasn't found")
        print("i=0 is position at which value can be inserted: before first element", a[0])
    elif left == len(a) - 1:
        print(x, "wasn't found")
        print(f"i={right} is position at which value can be inserted: at the end of list.")
    elif right - left == 1:
        print(x, "wasn't found")
        print(f"i={right} is position at which value can be inserted. Between {a[left]} and {a[right]} values.")
    elif right > left:
        print("Was found", right - left - 1, "times.")
        print(left + 1, "is it's first position")
        print(right - 1, "is it's last position")
        print(f"i={right} is a position value can be inserted at.")
    return


main()
