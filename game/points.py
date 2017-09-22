from game.switch import switch
from game.switch import case


class Points:
    first = "is null"
    second = "is null"
    third = "is null"
    fourth = "is null"
    fifth = "is null"
    sixth = "is null"
    pair = "is null"
    two_pair = "is null"
    three = "is null"
    small_street = "is null"
    big_street = "is null"
    full = "is null"
    carriage = "is null"
    poker = "is null"
    chaince = "is null"
    name = " "

    def rename(self, name):
        Points.name=name

    def out(self):
        print(Points.name)
        print("Your points:: \nFirst: " + str(Points.first))
        print("Second: " + str(Points.second))
        print("Third: " + str(Points.third))
        print("Fourth: " + str(Points.fourth))
        print("Fifth: " + str(Points.fifth))
        print("Sixth: " + str(Points.sixth))
        print("Pair: " + str(Points.pair))
        print("Two pair: " + str(Points.two_pair))
        print("Three: " + str(Points.three))
        print("Small street: " + str(Points.small_street))
        print("Big Street: " + str(Points.big_street))
        print("Full: " + str(Points.full))
        print("Carriage:" + str(Points.carriage))
        print("Poker: " + str(Points.poker))
        print("Chaince: " + str(Points.chaince))

    def add(self, what: int, how_much: int):
        while switch(what):
            if case(1):
                Points.first = how_much
                break
            if case(2):
                Points.second = how_much
                break
            if case(3):
                Points.third = how_much
                break
            if case(4):
                Points.fourth = how_much
                break
            if case(5):
                Points.fifth = how_much
                break
            if case(6):
                Points.sixth = how_much
                break
            if case(7):
                Points.pair = how_much
                break
            if case(8):
                Points.two_pair = how_much
                break
            if case(9):
                Points.three = how_much
                break
            if case(10):
                Points.small_street = how_much
                break
            if case(11):
                Points.big_street = how_much
                break
            if case(12):
                Points.full = how_much
                break
            if case(13):
                Points.carriage = how_much
                break
            if case(14):
                Points.poker = how_much
                break
            if case(15):
                Points.chaince = how_much
                break
            break

    def sums(self):
        sums = Points.first + Points.second + Points.third + Points.fourth + Points.fifth + Points.sixth
        if 63 > sums:
            sums -= 50
        sums = sums + Points.pair + Points.two_pair + Points.three + Points.small_street + Points.big_street + Points.full + Points.carriage + Points.poker + Points.chaince
        return sums

