from game.points import Points
from game.move import Move
from game.counting import count

if __name__ == '__main__':
    game = []
    number_of_players = int(input("How many are the players? "))
    for i in range(1, number_of_players + 1):
        game.append(Points())
        name = "Player " + str(i)
        game[i - 1].rename(name)

    for _ in range(1, 16):
        for i in range(1, number_of_players + 1):

            # TODO: czyszczenie terminala
            game[i - 1].out()
            moves = Move()
            a, b, c = moves.move()
            score = count(a, b, c)
            game[i - 1].add(a, score)
