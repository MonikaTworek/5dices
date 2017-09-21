from game.points import Points
from game.move import Move
from game.counting import count

if __name__ == '__main__':
    game = []
    number_of_players = int(input("How many are the players? "))
    for i in range(1, number_of_players + 1):
        game.append(Points())
#        game[i-1] = Points()
        name = "Player " + str(i)
        game[i-1].name = name
    for i in range(1, number_of_players + 1):
        for _ in range (1, 15):
            move = Move
            score = count(move[0], move[1], move[2])
            game[i-1].add(move[0], score)