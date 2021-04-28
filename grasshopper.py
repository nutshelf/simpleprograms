def main():
    """
    Grasshopper begins jumps from first point, ends at n point. Some points are not available for jumps
      |-|-|-|-...-|
    0-1-2-x-4-...-n
    available jumps: 1 section, 2 sections
    """
    n = 20  # >= 2
    nj = [None, 1, 1] + [0] * (n - 2)  # generate list for n points
    ap = [False] + [True] * n  # available points
    ap[4] = False
    for i in range(3, n + 1):
        if ap[i]:
            nj[i] = nj[i - 1] + nj[i - 2]
    print(nj)
    print(ap)
    return


main()
