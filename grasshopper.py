from random import random


def main():
    """
    Grasshoper jumps from point 1 to point n from in one direction.
      |-|---|-|-...-|
    0-1-2-x-4-5-...-n
    Available jumps: 1 interval, 2 intervals, 3 intervals between points.
    Point i=0 is not available for visiting.
    Some points are not available for jumps (ap[i] == False)
    Each point have cost of visiting c[i].
    Program:
     - returns maximum number of allowed trajectories at each point of grasshopper path (p:list).
     - returns minimum cost of going from start to each other (s:list) where c[i] is cost of visiting point p[i].
    """
    n = 10  # >= 3 necessarily
    p = [0, 1, 1, 2] + [0] * (n - 3)  # generate list for n points
    ap = [False] + [True] * n  # availability of points - all are av beside 0
    ap[4] = ap[7] = ap[9] = False  # some unavailable points
    c = [int(random() * 5) + 1 if ap[i] else 0 for i in range(n+1)]  # cost of visiting point
    ct = [0, c[1], c[2] + c[1], c[1] + c[3]] + [0] * (n - 3)  # cost total from 1 to i

    for i in range(4, n + 1):
        if ap[i]:
            p[i] = p[i - 1] + p[i - 2] + p[i - 3]
            # Total cost of path from p[1] to p[i] consist of cost of p[i] and min cost of tree left point:
            #    ct[i] = c[i] + min( c[i-1], c[i-2], c[i-3] )
            ct[i] = min(ct[i - j] for j in range(1, 4) if ap[i-j]) + c[i]
    # print(*list(map(lambda x: " " + str(x) + " " if x != 0 else "00", p)))
    print("Indexes of points          :", [i for i in range(n + 1)])
    print("Availability of points     :", list(map(int, ap)))
    print("Num of trajectories        :", p)
    print()
    print("Cost of visiting each point:", c)
    print("Min cost to come to point  :", ct)

    return


main()
