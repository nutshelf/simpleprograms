def generate_all_combinations(v: list, duplicates: list, m=-1, comb_indexes=None):
    """
    Generating all available combinations of elements from vocabulary v. Elements placed in combination by their
    indexes in "comb_indexes" list. Combinations with swapped equal elements are not included. Additional list used
    for this purpose.
    """
    assert v
    num = 0
    comb_indexes = comb_indexes if comb_indexes else []

    if m == -1:
        # for first call without m parameter
        m = len(v)
    if m == 0:
        if len(comb_indexes) == len(v):
            # if there is no new elements for combining, print this combination:
            num = 1
            for i in comb_indexes:
                # print(str(v[i]) + "(" + str(i) + ")", end="")
                print(v[i], end=" ")
            print()
        # else: some elements skipped, lists will be different due to repeating elements,
        # so no new combination can be generated.
        return num
    for i in range(len(v)):
        if i in comb_indexes:
            continue
        # if element v[i] not used before, then it can be added to combination.
        can_be_added = True
        if duplicates[i] > 0:
            # v[i] has duplicates, try to find duplicates in current combination via comb_indexes list
            for j in comb_indexes:
                if (v[j] == v[i]) and (j > i):
                    can_be_added = False
                    # j > i  means that equal elements can be placed in combination only in ascending order of their
                    # index. For example elements "a", "b", "a" can be combinated via indexes in order 0, 1, 2, but can
                    # not be combinated in order 2, 1, 0 because this order will not generate new unique combination.
                    # Algorithm generate combinations with ascending order indexes before combinations with other orders
        if can_be_added:
            # if element v[i] has no equal duplicates
            # and equal v[j] has, just add it finally.
            comb_indexes.append(i)
            num += generate_all_combinations(v, duplicates, m - 1, comb_indexes)
            comb_indexes.pop()
    return num


def duplicates_find(v: list, duplicates: list):
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            if v[i] == v[j]:
                duplicates[i] += 1
                duplicates[j] += 1
    return


def main():
    v = [3, 3, 32, 3]
    duplicates = [0] * len(v)  # duplicates elements quantity list
    duplicates_find(v, duplicates)
    print("List of elements for combinating:", v,
          "\nList of duplicates quantity for each element:", duplicates,
          "\nCombinations:")
    num = generate_all_combinations(v, duplicates)
    print("Number of combinations:", num)


main()
