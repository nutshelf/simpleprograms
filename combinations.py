def generate_all_av_combinations(v: list, m: int, ind=[]):
    """
    Generation all available combinations of m elements from vocabulary v.
    """
    if m == 0:
        for i in ind:
            print(str(v[i]) + "(" + str(i) + ")", sep="-", end="")
        print()
        return
    for i in range(len(v)):
        if not (i in ind):
            ind.append(i)
            generate_all_av_combinations(v, m - 1, ind)
            ind.pop()
    return


vocabulary = ["мама", "собака", "мама"]
generate_all_av_combinations(vocabulary, 3)
