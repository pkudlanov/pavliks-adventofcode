class RockPaperScissors():

    def __init__(self, *args, **kwargs):
        self.score = 0

    def __str__(self):
        return 'The total score is ' + str(self.score) + '.'

    def wl_x(self, *args, **kwargs):
        op = kwargs['opponent']
        if(op == 'A'):
            self.score += 3
        elif(op == 'B'):
            self.score += 0
        elif(op == 'C'):
            self.score += 6
        else:
            raise Exception('Opponent was not Rock, Paper, or Scissors!')

    def wl_y(self, *args, **kwargs):
        op = kwargs['opponent']
        if(op == 'A'):
            self.score += 6
        elif(op == 'B'):
            self.score += 3
        elif(op == 'C'):
            self.score += 0
        else:
            raise Exception('Opponent was not Rock, Paper, or Scissors!')

    def wl_z(self, *args, **kwargs):
        op = kwargs['opponent']
        if(op == 'A'):
            self.score += 0
        elif(op == 'B'):
            self.score += 6
        elif(op == 'C'):
            self.score += 3
        else:
            raise Exception('Opponent was not Rock, Paper, or Scissors!')

    def wl(self, *args, **kwargs):
        me = kwargs['me']
        if(me == 'X'):
            self.wl_x(**kwargs)
            self.score += 1
        elif(me == 'Y'):
            self.wl_y(**kwargs)
            self.score += 2
        elif(me == 'Z'):
            self.wl_z(**kwargs)
            self.score += 3


game = RockPaperScissors()


with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        game.wl(me=line[2], opponent=line[0])

print(game)
