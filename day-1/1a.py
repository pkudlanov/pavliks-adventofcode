class TopElf():

    def __init__(self):
        self.top_elf = 0
        self.top_cal = 0

    def __str__(self):
        return ('The elf carrying the most calories is elf ' +
                str(self.top_elf) +
                ', with a total of ' +
                str(self.top_cal) +
                ' calories.')

    def compare_cal(self, calories, elf):
        if self.top_cal < calories:
            self.top_cal = calories
            self.top_elf = elf


top_elf = TopElf()

with open('1a-input.txt') as f:
    lines = f.readlines()
    current_cal = 0
    current_elf = 1
    for line in lines:
        if line != '\n':
            current_cal += int(line)
        else:
            top_elf.compare_cal(calories=current_cal, elf=current_elf)
            current_cal = 0
            current_elf += 1

    top_elf.compare_cal(calories=current_cal, elf=current_elf)

print(top_elf)
