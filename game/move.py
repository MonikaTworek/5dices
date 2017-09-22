from game.desk import Desk


class Move:  # zwraca (co ktos ma, kosci, ktory ruch)
    desk = Desk()
    check = 1

    def move(self):
        while self.check != 4:
            print("Dices 1: " + str(self.desk.dices[0].rank) + " Dices 2: " + str(self.desk.dices[1].rank) + " Dices 3: " + str(self.desk.dices[2].rank)
                + " Dices 4: " + str(self.desk.dices[3].rank) + " Dices 5: " + str(self.desk.dices[4].rank))
            moves = int(input("What you want to do? \n [1]I have somethink and I want to write this \n [2] I want to throw my dices "))
            if self.check == 3 and moves == 2:
                print("You must writnig your score!")
                what = int(input("What do you have?"))
                return what, self.desk, moves
            if moves == 1:
                what = int(input("What do you have?"))
                return what, self.desk, moves
            if moves == 2:
                self.check += 1
                sum = 0
                for x in range(1, 6):
                    throw = input("Do you want to throw dices number " + str(x) + "? [1]YES [2]NO ")
                    throw = int(throw)
                    if throw == 1:
                        sum += pow(2, x - 1)
                self.desk.move(sum)
