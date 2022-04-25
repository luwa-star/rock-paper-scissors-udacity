import random
import sys

moves = ['rock', 'paper', 'scissors']


def beats(one, two, score1, score2):
    while True:
        if one == 'rock':
            if two == 'rock':
                break

            elif two == 'paper':
                break

            elif two == 'scissors':
                break

        elif one == 'paper':
            if two == 'paper':
                break

            elif two == 'rock':
                break

            elif two == 'scissors':
                break

        elif one == 'scissors':
            if two == 'scissors':
                break

            elif two == 'rock':
                break

            elif two == 'paper':
                break


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            break
        elif option == 'quit':
            break
    return option


class Player:
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self, p1):
        super().__init__()
        self.p1 = p1
        # to set initial computer value
        self.my_move = 'paper'

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        # to read the move of the opponent
        self.my_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        index = moves.index(self.my_move) + 1
        return moves[index % len(moves)]

    def learn(self, my_move, their_move):
        # to read my move
        self.my_move = my_move


class HumanPlayer(Player):
    def move(self):
        # play = input('Rock, paper, scissors? > ').lower()
        move = valid_input('Rock, paper, scissors? > ', moves)
        if move in moves:
            return move

        elif move == 'quit':
            sys.exit()

        else:
            return self.move()


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        beats(move1, move2, self.score1, self.score2)

        if move1 == 'rock':
            if move2 == 'rock':
                print('*** TIE ***')
                self.score1 += 0
                self.score2 += 0

            elif move2 == 'paper':
                print('***PLAYER TWO WINS***')
                self.score2 += 1
                self.score1 += 0

            elif move2 == 'scissors':
                print('***PLAYER ONE WINS***')
                self.score1 += 1
                self.score2 += 0

        elif move1 == 'paper':
            if move2 == 'paper':
                print('*** TIE ***')
                self.score1 += 0
                self.score2 += 0

            elif move2 == 'rock':
                print('***PLAYER ONE WINS***')
                self.score1 += 1
                self.score2 += 0

            elif move2 == 'scissors':
                print('***PLAYER TWO WINS***')
                self.score2 += 1
                self.score1 += 0

        elif move1 == 'scissors':
            if move2 == 'scissors':
                print('*** TIE ***')
                self.score1 += 0
                self.score2 += 0

            elif move2 == 'rock':
                print('***PLAYER TWO WINS***')
                self.score2 += 1
                self.score1 += 0

            elif move2 == 'paper':
                print('***PLAYER TWO WINS***')
                self.score1 += 1
                self.score2 += 0

        print(f"SCORE : PLAYER ONE {self.score1}, PLAYER TWO {self.score2}")

    def play_game(self):

        print("Game start!")
        print("""Please Note: There are five rounds in this game.
             After the fifth round, the game announces the winner.
             Type 'quit' to exit the game.
             Goodluck!""")
        print('Rock Paper Scissors. Go!')
        for round in range(5):
            print(f"Round {round}: --")
            self.play_round()

        print("Game over!")
        print(
            f"FINALSCORE : PLAYER ONE {self.score1}, PLAYER TWO {self.score2}")
        if self.score1 > self.score2:
            print('***PLAYER ONE WINS!!***')
        elif self.score1 == self.score2:
            print("***IT'S A TIE!!***")
            self.play_game()

        else:
            print('***PLAYER TWO WINS!!***')


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(HumanPlayer),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)

    game = Game(p1, p2)
    game.play_game()
