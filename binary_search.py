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
        Return NEAREST NEXT index of X possible occurrence in list.
        Ex:
            binary_search_left([2, 4, 5, 6], 3) = 1     # mean a[2] is possible X occurrence
            binary_search_left([2, 2, 3, 3], 3) = 1     # mean a[1+1] is possible X occurrence
        """
    assert a
    left = -1
    right = len(a)
    mid = 0
    while left != mid:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid
        else:
            right = mid
    return left


def main():
    a = [3]
    x = 5
    left = binary_search_left(a, x)
    right = binary_search_right(a, x)
    #
    # print(a, "is a list")
    # print(x, "is a value to find in list")
    # if right == 0:
    #     print(x, "isn't found")
    #     print("0 is position at which value can be inserted: before first element", a[0])
    # elif left == len(a) - 1:
    #     print(x, "isn't found")
    #     print(left, " is position at which value can be inserted: at the end of list.")
    # elif right - left == 1:
    #     print(x, "isn't found")
    #     print(right, f" is position at which value can be inserted. Between {a[left]} and {a[right]}")
    # elif right > left:
    #     print("Was found", right - left - 1, "times.")
    #     print(left + 1, "is it's first position")
    #     print(right - 1, "is it's last position")
    #     print(right, "is a position value can be inserted at.")
    return


main()
