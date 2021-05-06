from random import random


def merge_sort(a, lb=None, ub=None):
    """
    Recursive merge sort inside in a[]. For temporarily usage there is b[]. Memory is len(b[])=len(a[])
    """
    if lb is None or ub is None:
        lb = 0
        ub = len(a) - 1
    n = ub - lb + 1
    n2 = n // 2
    if n < 2:
        return

    merge_sort(a, lb, lb + n2 - 1)  # half(n//2 elements) for even,
    #  less part for odd, incl. n=3 (n//2 elements)
    merge_sort(a, lb + n2, ub)  # half(n//2 elements) for even,
    #  greater part for odd, incl. n=3 (n - n//2 elements)
    # merging into b[]:
    i = j = k = 0
    b = [None] * n  # length = n
    while i < n2 and j < (n - n2):
        if a[lb + i] <= a[lb + n2 + j]:
            b[k] = a[lb + i]
            i += 1
        else:
            b[k] = a[lb + n2 + j]
            j += 1
        k += 1
    while i < n2:
        b[k] = a[lb + i]
        i += 1
        k += 1
    while j < (n - n2):
        b[k] = a[lb + n2 + j]
        j += 1
        k += 1
    # move back from b[] to a[]
    k = 0
    for k in range(len(b)):
        a[lb + k] = b[k]
    # print(f"merged [{lb}:{ub}]", a[lb:ub+1])
    return


def quick_sort(a: list, lo=None, up=None):
    """
    Recursive Toni Hoar's sorting with three-part partitioning with median of 3 elements: at beginning, middle,
    end of array. Assume a[lo] is first element, a[up] is last element of array part to sort or whole array.
    """
    if lo is None or up is None:
        lo = 0
        up = len(a) - 1

    # base case: list consist of <=1
    if up - lo <= 0:
        return

    if a[lo] > a[up]:
        a[lo], a[up] = a[up], a[lo]  # 1 of 3 swap (look about median later)
    if up - lo == 1:  # base case 2 elements. Complete
        return

    mid = (lo + up) // 2
    if a[lo] > a[mid]:
        a[mid], a[lo] = a[lo], a[mid]  # 2 of 3 swap (look about median later). a[lo] now is the smallest of 3
    if up - lo == 2:
        if a[mid] > a[up]:
            a[mid], a[up] = a[up], a[mid]  # Now a[lo] <= a[mid] <= a[up]. Base case of 3 elements complete.
        return
    if a[mid] < a[up]:
        a[mid], a[up] = a[up], a[mid]  # 3 of 3 swap for median.
    # Three IF and swap operators used for finding median and swapping elements in ascending order except last two,
    # example of right swapping: [1,3,2]. Last "2" is pivot element.
    # It is partitioning. Choosing median from 3 elements from start, middle, end of array and place Median to end.
    # Simultaneously swap operation on elements used for base cases of recursion.

    i = lo
    j = up - 1
    # ["_"+str(a[i])+"_" if (i >= 1 and i<= 3) else str(a[i]) for i in range(len(a))]
    # print(f"first non private call of recursion. list={a}, ind={lo}..{up}, i={i}, j={j}, pivot a[{up}]={a[up]}")
    while True:
        while a[i] < a[up]:
            i += 1
        while a[j] >= a[up]:
            j -= 1
            if j <= i:
                # print(f"break. list={a}, ind={lo}..{up}, i={i}, j={j}, pivot a[{up}]={a[up]}")
                break
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
    a[i], a[up] = a[up], a[i]
    # Now pivot is at a[j+1]
    # print(a, "pivot index =", j + 1, end=" ")
    # print(f"-left part[{lo}:{i-1}]")
    quick_sort(a, lo, i-1)
    # print(f"-right part[{i+1}:{up}]")
    quick_sort(a, i+1, up)
    return


def main():
    #n = 2
    #a = [int(random() * 10 + 5) for i in range(n)]
    a = [1, 2, 1, 1]
    b = list(a)
    print("source:\t\t", a)
    merge_sort(a)
    print("merge sort:\t", a)
    quick_sort(b)
    print("quick_sort:\t", b)
    return


main()
