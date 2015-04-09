#Get Bit!
import random
from time import time
from get_bit_bots import Random_Robot

class Game(object):
    def __init__(self, *robots):
        self.robots = list(robots)
        for robot in self.robots:
            robot.game = self
        random.shuffle(self.robots)
        self.n_robots = len(robots)
        self.hands = {robot:list(range(self.n_robots+1)) for robot in self.robots}
        self.limbs = {robot:4 for robot in self.robots}
        self.out = open("log_{}_{}.txt".format(",".join(sorted([r.name for r in self.robots])), str(int(time()))), 'w')

    def get_order(self):
        return [robot.name for robot in self.robots]

    def get_move(self, robot):
        move = -1
        try:
            move = robot.get_move()
        except:
            pass
        if move not in self.hands[robot]:
            return -1
        return move

    def move_to_front(self, robot):
        self.robots.remove(robot)
        self.robots.append(robot)

    def play_round(self,get_bit=True):
        moves = []
        getting_bit = set([])
        for robot in self.robots:
            move = self.get_move(robot)
            if move == -1:
                getting_bit.add(robot)
            else:
                moves.append((move,robot))
        moves.sort(key = lambda x:x[0])
        no_move = set([])
        for move in moves:
            self.out.write(move[1].name)
            if move[0] in self.hands[move[1]]:
                self.hands[move[1]].remove(move[0])
            for other_move in moves:
                if other_move == move:
                    continue
                if other_move[0] == move[0]:
                    no_move.add(move)
                    no_move.add(other_move)
            if move in no_move:
                self.out.write(",x");
            else:
                self.out.write(",m");
            self.out.write(",{}\n".format(move[0]))
        for move in no_move:
            moves.remove(move)
        for move in moves:
            self.move_to_front(move[1])
        if get_bit:
            getting_bit.add(self.robots[0])
        for robot in getting_bit:
            self.out.write("{},b\n".format(robot.name))
            self.limbs[robot] -= 1
            if self.limbs[robot] <= 0:
                self.robots.remove(robot)
            else:
                self.move_to_front(robot)
                self.hands[robot] = list(range(self.n_robots+1))
        for robot in self.robots:
            if len(self.hands[robot]) < 2:
                self.hands[robot] = list(range(self.n_robots+1))

    def play_game(self):
        for robot in self.robots:
            robot.game_start()
            self.out.write(robot.name+",")
        self.out.write("\n")
        self.play_round(False)
        while len(self.robots) > 2:
            self.play_round()
        self.out.write(str(self.robots[1].name))
        self.out.close()
        return self.robots[1]

#h0 = Human_Robot("Eliot")
h1 = Random_Robot("Alice")
h2 = Random_Robot("Bob")
h3 = Random_Robot("Carol")
h4 = Random_Robot("Dave")
h5 = Random_Robot("Matthew")
g = Game(h1,h2,h3,h4,h5)
#g.play_game()
print(str(h5.get_hands()))
print(g.play_game().name + " wins!")
