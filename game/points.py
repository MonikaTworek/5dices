from game.switch import switch
from game.switch import case


class Points:
    def __init__(self):
        self.first = "is null"
        self.second = "is null"
        self.third = "is null"
        self.fourth = "is null"
        self.fifth = "is null"
        self.sixth = "is null"
        self.pair = "is null"
        self.two_pair = "is null"
        self.three = "is null"
        self.small_street = "is null"
        self.big_street = "is null"
        self.full = "is null"
        self.carriage = "is null"
        self.poker = "is null"
        self.chaince = "is null"
        self.name = " "

    def rename(self, name):
        self.name=name

    def out(self):
        print(self.name)
        print("Your points:: \nFirst: " + str(self.first))
        print("Second: " + str(self.second))
        print("Third: " + str(self.third))
        print("Fourth: " + str(self.fourth))
        print("Fifth: " + str(self.fifth))
        print("Sixth: " + str(self.sixth))
        print("Pair: " + str(self.pair))
        print("Two pair: " + str(self.two_pair))
        print("Three: " + str(self.three))
        print("Small street: " + str(self.small_street))
        print("Big Street: " + str(self.big_street))
        print("Full: " + str(self.full))
        print("Carriage:" + str(self.carriage))
        print("Poker: " + str(self.poker))
        print("Chaince: " + str(self.chaince))

    def add(self, what: int, how_much: int):
        while switch(what):
            if case(1):
                self.first = how_much
                break
            if case(2):
                self.second = how_much
                break
            if case(3):
                self.third = how_much
                break
            if case(4):
                self.fourth = how_much
                break
            if case(5):
                self.fifth = how_much
                break
            if case(6):
                self.sixth = how_much
                break
            if case(7):
                self.pair = how_much
                break
            if case(8):
                self.two_pair = how_much
                break
            if case(9):
                self.three = how_much
                break
            if case(10):
                self.small_street = how_much
                break
            if case(11):
                self.big_street = how_much
                break
            if case(12):
                self.full = how_much
                break
            if case(13):
                self.carriage = how_much
                break
            if case(14):
                self.poker = how_much
                break
            if case(15):
                self.chaince = how_much
                break
            break

    def sums(self):
        sums = self.first + self.second + self.third + self.fourth + self.fifth + self.sixth
        if 63 > sums:
            sums -= 50
        sums = sums + self.pair + self.two_pair + self.three + self.small_street + self.big_street + self.full + self.carriage + self.poker + self.chaince
        return sums

