from game.points import Points
from game.move import Move
from game.counting import count

if __name__ == '__main__':
    game = []
    number_of_players = int(input("How many are the players? "))
    for i in range(1, number_of_players + 1):
        a = Points()
        name = "Player " + str(i)
        a.rename(name)
        game.append(a)
        print(name)

    for i in range(1, number_of_players + 1):
        print(game[i - 1].name)

        # for i in range(1, number_of_players + 1):
        #     for _ in range (1, 15):
        #         TODO: czyszczenie terminala
        # game[i-1].out()
        # move = Move
        # score = count(move[0], move[1], move[2])
        # game[i-1].add(move[0], score)
