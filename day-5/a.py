class Supplies():

    def __init__(self):
        self.top_crates = ''

    def __str__(self):
        return('The crates on top of all the stacks are as follows' +
               self.top_crates + '.')
               