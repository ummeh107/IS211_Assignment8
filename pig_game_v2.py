import random
import time
import argparse



class Roll():
    def __init__(self):
        self.roll=0

    def rolled(self):
        self.roll = random.randint(1,6)    
        return self.roll

class Player():

    def __init__(self, name):
        self.sum_score = 0
        self.turn_score = 0
        self.name = name
        self.status = 0
        print(name)

class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self, name="Computer")

class PlayerFactory():

    def player_category(self, category):
        # print('pf {}'.format(category))
        if category.lower() == 'h':
            return Player("Human")
        elif category.lower() == 'c':
            return ComputerPlayer()            

class Game():
    def __init__(self, player1="Player1",player2="Player2"):
        game_Players = PlayerFactory()
        self.player_1 = game_Players.player_category(args.player1)
        self.player_2 = game_Players.player_category(args.player2)
        self.roll = Roll()
        self.start_play(self.player_1)

    def start_play(self, player):
        print('{} playing..'.format(player.name))
        player.status = 0
        while player.sum_score < 100:
            if args.timed :
                self.time_check()
            rolled = self.roll.rolled()
            if rolled == 1:
                player.turn_score = 0
                print("player {} has rolled 1, next player's turn".format(player.name))
                self.player_change()
            else:
                player.turn_score += rolled
                print('player {} rolled a {} and total score {}'.format(player.name, rolled, player.sum_score))
                self.player_choice(player)
        print('Player {} won the game with score {}.'.format(player.name, player.sum_score))                

    def player_change(self):
        if self.player_1.status == 0:
            self.player_1.status = 1
            self.start_play(self.player_2)
        else:
            self.player_2.status = 1
            self.start_play(self.player_1)    

    def player_choice(self, player):
        if player.name == 'Computer':
            score = 100- player.sum_score
            if score > 25:
                score = 25
            if player.turn_score >= score:
                player.sum_score += player.turn_score
                if player.sum_score >= 100:
                    print('player {} wins the game score {}'.format(player.name, player.sum_score))    
                    raise SystemExit
                else:
                    player.turn_score = 0
                    self.player_change()
            else:
                self.start_play(player)  
        next_roll = input('Hold/Roll? h/r :')
        if next_roll.lower() == 'r':
            self.start_play(player)
        elif next_roll.lower() == 'h':
            player.sum_score =+ player.turn_score
            if player.sum_score >= 100:
                print('Player {} wins and score {}'.format(player.name, player.sum_score))
                raise SystemExit
            else:
                player.turn_score = 0
                self.player_change()                                                              

class TimedGameProxy(Game):
    def __init__(self):
        self.time_start = time.time()
        Game.__init__(self, 'Player1', 'Player2')

    def time_check(self):
        if time.time() - self.time_start >= 60:
            if self.player_1.sum_score > self.player_2.sum_score :
                print("Time is up, {} player wins the game score is {}".format(self.player_1.name, self.player_1.sum_score))
            else:
                print("Time is up, {} player wins the game score is {}".format(self.player_2.name, self.player_2.sum_score))
            raise SystemExit
        else:
            print("{} seconds remain..".format(time.time() - self.time_start))    



# 
parser = argparse.ArgumentParser()
parser.add_argument('--player1', help="Choose a 'h' or  'c' player type.")
parser.add_argument('--player2', help="Choose a 'h' or 'c' player type.")
parser.add_argument('--timed', help="Time for limited duration!")
args = parser.parse_args()


def main():
    if args.timed:
        TimedGameProxy()
    else:
        Game()

if __name__ == "__main__":
    main()        