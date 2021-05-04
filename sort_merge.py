from random import random


def merge_sort(a, lb=None, ub=None):
    """
    Recursive merge sort inside in a[]. For temporarily usage there is b[].
    """
    if lb is None or ub is None:
        lb = 0
        ub = len(a) - 1
    n = ub - lb + 1
    n2 = n // 2
    if n >= 2:
        merge_sort(a, lb, lb + n2 - 1)  # half(n//2 elements) for even,
                                        #  less part for odd, incl. n=3 (n//2 elements)
        merge_sort(a, lb + n2, ub)      # half(n//2 elements) for even,
                                        #  greater part for odd, incl. n=3 (n - n//2 elements)
        # merging into b[]:
        i = j = k = 0
        b = [None] * n # length = n
        while i < n2 and j < (n - n2):
            if a[lb + i] // 1 <= a[lb + n2 + j] // 1:
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
        print(f"merged [{lb}:{ub}]", a[lb:ub+1])
    else:  # n = <1
        return
    return


def main():
    n = 10
    a = [int(random() * 10 + 5)/10 for i in range(n)]
    print("source:\t\t", a)
    merge_sort(a)
    #print("merge sort:\t", a)
    return


main()

