import itertools
import timer


houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))
first, middle = 1, 3


def imright(h1, h2):
    "house h1 is immediately right to house h2"
    return h1 - h2 == 1


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle():
    return [(WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            if imright(green, ivory)  # 6

            for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
            if Englishman == red  # 2
            if Norwegian == first  # 10
            if nextto(Norwegian, blue)  # 15

            for (dog, snails, fox, horse, ZEBRA) in orderings
            if (Spaniard == dog)

            for (coffee, tea, milk, oj, WATER) in orderings
            if (Ukrainian == tea)  # 5
            if (milk == middle)  # 9
            if (coffee == green)  # 4

            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if (LuckyStrike == oj)
            if (OldGold == snails)
            if (Kools == yellow)
            if (nextto(Chesterfields, fox))
            if (nextto(Kools, horse))
            if (Japanese == Parliaments)
            ]


def main():
    print timer.timedcalls(0.02, zebra_puzzle)

if __name__ == '__main__':
    main()
