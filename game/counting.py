def sortowanie(desk):
    tab = [desk.dices[0].rank, desk.dices[1].rank, desk.dices[2].rank, desk.dices[3].rank, desk.dices[[4]].rank]
    for number in range(0, 5):
        smallest = tab[0]
        for i in range(number, 5):
            if tab[i] < tab[smallest]:
                smallest = i
        tab[smallest], tab[number] = tab[number], tab[smallest]
    return tab


def count(what, desk, move):
    sums = 0
    if what == 1 or what == 2 or what == 3 or what == 4 or what == 5 or what == 6:
        for i in range(1, 6):
            if desk.dices[i - 1].rank == what:
                sums = sums + what
        return sums
    if what == 7:
        pair = 0
        for i in range(1, 5):
            for j in range(i, 6):
                if desk.dices[i - 1].rank == desk.dices[j - 1].rank and desk.dices[i - 1].rank * 2 > pair:
                    pair = 2 * desk.dices[i - 1].rank
        if move == 1: return 2 * pair
        return pair
    tab = sortowanie(desk)
    if what == 8:
        if tab[0] == tab[1] and tab[2] == tab[3]:
            if move == 1: return 2 * (tab[0] + tab[1] + tab[2] + tab[3])
            return tab[0] + tab[1] + tab[2] + tab[3]
        elif tab[0] == tab[1] and tab[3] == tab[4]:
            if move == 1: return 2 * (tab[0] + tab[1] + tab[3] + tab[4])
            return tab[0] + tab[1] + tab[3] + tab[4]
        elif tab[1] == tab[2] and tab[3] == tab[4]:
            if move == 1: return 2 * (tab[1] + tab[2] + tab[3] + tab[4])
            return tab[1] + tab[2] + tab[3] + tab[4]
        else:
            return 0
    if what == 9:
        if tab[0] == tab[1] == tab[2] or tab[1] == tab[2] == tab[3] or tab[2] == tab[3] == tab[4]:
            if move == 1:
                return 6 * tab[2]
            else:
                return 3 * tab[2]
        else:
            return 0
    if what == 10:
        for num in range(1, 5):
            if tab[num - 1] != num: return 0
        return 15
    if what == 11:
        for num in range(2, 6):
            if tab[num - 1] != num: return 0
        return 20
    if what == 12:
        if tab[0] == tab[1] and tab[3] == tab[4] and (tab[2] == tab[1] or tab[2] == tab[3]):
            for _ in range(1, 6):
                sums += tab[_]
            return sums
        else:
            return 0
    if what == 13:
        if tab[1] == tab[2] == tab[3] and (tab[1] == tab[0] or tab[1] == tab[4]):
            return 4 * tab[1]
        else:
            return 0
    if what == 14:
        if tab[0] == tab[1] == tab[2] == tab[3] == tab[4]:
            if move == 1: return 50 + 10 * tab[0]
            return 50 + 5 * tab[0]
        else:
            return 0
    if what == 15:
        for _ in range(1, 6):
            sums += tab[_]
        return sums
