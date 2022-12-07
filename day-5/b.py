class Supplies():

    def __init__(self):
        self.stacks = {}

    def __str__(self):
        return('Part B:\n' +
               'The crates on top of all the stacks are as follows ' +
               self.last_crates() + '.\n')

    def stack_crate(self, *args, **kwargs):
        if kwargs['stack'] in self.stacks:
            self.stacks[kwargs['stack']][:0] = kwargs['crate']
        else:
            self.stacks[kwargs['stack']] = []
            self.stacks[kwargs['stack']][:0] = kwargs['crate']

    def build_stacks(self, *args, **kwargs):
        with open(kwargs['f']) as f:
            lines = f.readlines()
            for line in lines:
                clean_line = line.splitlines()[0]
                if any([char.isdigit() for char in clean_line]):
                    break
                for index, char in enumerate(clean_line):
                    if char.isalpha():
                        # Get proper stack number from text file character index
                        proper_stack_num = (index + 3) / 4
                        self.stack_crate(stack=str(int(proper_stack_num)), crate=char)

    def move_crates(self, *args, **kwargs):
        crates = self.stacks[kwargs['from_stack']][-kwargs['crates_amount']::]
        del self.stacks[kwargs['from_stack']][-kwargs['crates_amount']::]
        self.stacks[kwargs['to_stack']].extend(crates)

    def last_crates(self, *args, **kwargs):
        i = 0
        top_crates = ''
        while i < len(self.stacks):
            top_crates += self.stacks[str(i + 1)][-1]
            i += 1

        return top_crates

    def run_procedure(self, *args, **kwargs):
        with open(kwargs['f']) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('move'):
                    ls = line.split()
                    procedure_dict = dict(zip(ls[::2], ls[1::2]))
                    self.move_crates(
                        crates_amount=int(procedure_dict['move']),
                        from_stack=procedure_dict['from'],
                        to_stack=procedure_dict['to'])
