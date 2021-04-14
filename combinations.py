def generate_all_combinations(v: list, doubles: list, test_combination, m=-1, comb_indexes=[]):
    """
    Generating all available combinations of elements from vocabulary v. Elements placed in combination by their
    indexes in "comb_indexes" list. Combinations with swapped equal elements are not included. Additional list used
    for this purpose.
    """
    assert v
    if m == -1:
        # for first call without m parameter
        m = len(v)
    if m == 0:
        if len(comb_indexes) == len(v):
            # if there is no new elements for combining, print this combination
            for i in comb_indexes:
                # print(str(v[i]) + "(" + str(i) + ")", end="")
                print(v[i], end="")
            if test_combination == comb_indexes:
                print(" found 1 test combination", end="")
            print()
        # else: some elements skipped due to repeated(equal) elements, so no new combination can be generated.
        return
    for i in range(len(v)):
        if not (i in comb_indexes):
            # if element v[i] not used before, then it can be added to combination.
            can_be_added = True
            if doubles[i] > 0:
                # v[i] has doubles, try to find doubles in current combination via comb_indexes list
                for j in comb_indexes:
                    if (v[j] == v[i]) and (j > i):
                        can_be_added = False
                        # j > i  means that equal elements can be placed only in ascending order of their index. For
                        # example elements "a", "b", "a" can be combinated via indexes in order 0, 1, 2, but can not be
                        # combinated in order 2, 1, 0 because this order will not generate new combination. Algorithm
                        # generate combinations with ascending order indexes before combinations with other orders.
            if can_be_added:
                # if element v[i] has no equal doubles
                # and equal v[j] has, just add it finally.
                comb_indexes.append(i)
                generate_all_combinations(v, doubles, test_combination, m - 1, comb_indexes)
                comb_indexes.pop()
    return


def doubles_find(v: list, doubles: list):
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i] == v[j]:
                doubles[i] += 1
                doubles[j] += 1
    return


def main():
    vocabulary = ["a", "a", "a"]
    doubles = [0] * len(vocabulary)  # doubles elements quantity list
    doubles_find(vocabulary, doubles)
    print(vocabulary, doubles)
    test_combination = [2, 1, 0]
    generate_all_combinations(vocabulary, doubles, test_combination)


main()
