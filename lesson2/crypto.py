import re
from timer import timedcall
from itertools import permutations


def solve(puzzle):
    n = len(get_first_letters(puzzle))
    return next(translate(puzzle, comb)
                for comb in permutations(range(10), len(get_alphabet(puzzle)))

                # we can not use 0 as a first digit like 023
                if 0 not in comb[:n]

                if eval(translate(puzzle, comb))
                )


def get_alphabet(puzzle):
    first_letters = get_first_letters(puzzle)
    a = set(''.join(re.findall(r'\w+', puzzle))) - set(first_letters)

    # we don't really have to sort but it's convenient
    return first_letters + ''.join(sorted(a))


def get_first_letters(puzzle):
    return ''.join(set([word[0] for word in re.findall(r'\w+', puzzle)]))


def translate(puzzle, comb):

    # comb is a tuple (0, 1, 2, 3, 4)
    # we have to transform it to string
    comb_str = ''.join([str(s) for s in comb])

    table = str.maketrans(get_alphabet(puzzle), comb_str)
    return puzzle.translate(table)


def main():
    puzzle = "ODD + ODD == EVEN"
    print(timedcall(solve, puzzle))


if __name__ == '__main__':
    main()
