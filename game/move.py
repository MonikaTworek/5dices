from game.desk import Desk


class Move:  # zwraca (co ktos ma, kosci, ktory ruch)
    desk = Desk()
    check = 1

    def move(self):
        print("Dices 1: " + self.desk.dices[0] + " Dices 2: " + self.desk.dices[1] + " Dices 3: " + self.desk.dices[2]
            + " Dices 4: " + self.desk.dices[3] + " Dices 5: " + self.desk.dices[4])
        while self.check != 4:
            move = int(input("What you want to do? \n [1]I have somethink and I want to write this \n [2] I want to throw my dices "))
            if self.check == 3 and move == 2:
                print("You must writnig your score!")
                what = int(input("What do you have?"))
                return what, self.desk, move
            if move == 1:
                what = int(input("What do you have?"))
                return what, self.desk, move
            if move == 2:
                self.check += 1
                sum = 0
                for x in range(1, 5):
                    throw = input("Do you want to throw dices number " + str(x) + "? [1]YES [2]NO")
                    throw = int(throw)
                    if throw == 1:
                        sum += pow(2, x - 1)
                self.desk.move(sum)
