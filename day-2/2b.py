class RockPaperScissors():

    def __init__(self, *args, **kwargs):
        self.score = 0

    def __str__(self):
        return 'The total score is ' + str(self.score) + '.'

    def lose_x(self, *args, **kwargs):
        op = kwargs['opponent']
        if(op == 'A'):
            self.score += 3
        elif(op == 'B'):
            self.score += 1
        elif(op == 'C'):
            self.score += 2
        else:
            raise Exception('Opponent was not Rock, Paper, or Scissors!')

    def draw_y(self, *args, **kwargs):
        op = kwargs['opponent']
        if(op == 'A'):
            self.score += 4
        elif(op == 'B'):
            self.score += 5
        elif(op == 'C'):
            self.score += 6
        else:
            raise Exception('Opponent was not Rock, Paper, or Scissors!')

    def win_z(self, *args, **kwargs):
        op = kwargs['opponent']
        if(op == 'A'):
            self.score += 8
        elif(op == 'B'):
            self.score += 9
        elif(op == 'C'):
            self.score += 7
        else:
            raise Exception('Opponent was not Rock, Paper, or Scissors!')

    def wl(self, *args, **kwargs):
        me = kwargs['me']
        if(me == 'X'):
            self.lose_x(**kwargs)
        elif(me == 'Y'):
            self.draw_y(**kwargs)
        elif(me == 'Z'):
            self.win_z(**kwargs)


game = RockPaperScissors()


with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        game.wl(me=line[2], opponent=line[0])

print(game)
