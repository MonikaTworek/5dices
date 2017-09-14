from game.desk import Desk


class Move:
    desk = Desk()
    da = str(desk.A.rank)
    db = str(desk.B.rank)
    dc = str(desk.C.rank)
    dd = str(desk.D.rank)
    de = str(desk.E.rank)
    check = 1

    def start(self):
        print("Dices 1: " + self.da + " Dices 2: " + self.db + " Dices 3: " + self.dc + " Dices 4: " + self.dd + " Dices 5: " + self.de)
        while( self.check != 3):
            move = input("What you want to do? \n [1]I have somethink and I want to write this \n [2] I want to throw my dices \n")
            move = int(move)


