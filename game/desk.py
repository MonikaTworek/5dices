from random import randrange


class Dice:
    def __init__(self):
        self.rank = int

    def __init__(self):
        self.rank = randrange(1, 6)

    def moves(self):
        self.rank = randrange(1, 6)


class Desk:
    dices = [Dice() for _ in range(5)]

    def move(self, dices: int):
        i = 16
        if dices > i:
            Desk.dices[4].moves()
            dices -= i
        i = i / 2
        if dices > i:
            Desk.dices[3].moves()
            dices -= i
        i = i / 2
        if dices > i:
            Desk.dices[2].moves()
            dices -= i
        i = i / 2
        if dices > i:
            Desk.dices[1].moves()
            dices -= i
        i = i / 2
        if dices > i:
            Desk.dices[0].moves()
            dices -= i
