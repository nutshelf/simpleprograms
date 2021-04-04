def move_disks(n, pegs, fr, th, to, moves=0):
    """
    Function moves N disks from FR through TH to TO, where three last are indexes of pegs list: 0,1,2.
    """
    if n == 1:
        pegs[to].append(pegs[fr].pop())
        moves += 1
        print("move №", moves, *pegs)
        return moves
    moves = move_disks(n - 1, pegs, fr, to, th, moves)
    moves = move_disks(1, pegs, fr, th, to, moves)
    moves = move_disks(n - 1, pegs, th, fr, to, moves)
    return moves


def main():
    n = 5  # amount of disks
    pegs = [[x for x in range(n, 0, -1)],
            [],
            []]
    print(*pegs)
    moves = move_disks(n, pegs, 0, 1, 2)
    print("moves = ", moves)
    return


main()
