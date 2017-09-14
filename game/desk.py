from random import randrange


class Dice:
    rank = int

    def __init__(self):
        self.rank = randrange(1,6)

    def moves(self):
        self.rank = randrange(1,6)


class Desk:
    A = Dice()
    B = Dice()
    C = Dice()
    D = Dice()
    E = Dice()

    def move(Desk, dices: int):
        i=16
        if (dices > i):
            Desk.E.moves()
            dices-=i
        i=i/2
        if (dices > i):
            Desk.D.moves()
            dices-=i
        i=i/2
        if (dices > i):
            Desk.C.moves()
            dices-=i
        i=i/2
        if (dices > i):
            Desk.B.moves()
            dices-=i
        i=i/2
        if (dices > i):
            Desk.A.moves()
            dices-=i