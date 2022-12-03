class TopElves():

    def __init__(self):
        self.top_elf = 0
        self.top_cal = 0
        self.sec_elf = 0
        self.sec_cal = 0
        self.thrd_elf = 0
        self.thrd_cal = 0
        self.total_cal = 0

    def __str__(self):
        return ("The elves carrying the most calories are elves:\n" +
                str(self.top_elf) + " with a total of " + str(self.top_cal) + " calories,\n" +
                str(self.sec_elf) + " with a total of " + str(self.sec_cal) + " calories,\n" +
                str(self.thrd_elf) + " with a total of " + str(self.thrd_cal) + " calories.\n" +
                "The combined total of calories for all three elves is " + str(self.total_cal) + " calories.")

    def compare_cal(self, calories, elf):
        if self.top_cal < calories:
            self.sec_cal = self.top_cal
            self.sec_elf = self.top_elf
            self.top_cal = calories
            self.top_elf = elf
        elif self.sec_cal < calories:
            self.thrd_cal = self.sec_cal
            self.thrd_elf = self.sec_elf
            self.sec_cal = calories
            self.sec_elf = elf
        elif self.thrd_cal < calories:
            self.thrd_cal = calories
            self.thrd_elf = elf

        self.cal_sum()

    def cal_sum(self):
        self.total_cal = sum([self.top_cal, self.sec_cal, self.thrd_cal])


top_elves = TopElves()

with open('1a-input.txt') as f:
    lines = f.readlines()
    current_cal = 0
    current_elf = 1
    for line in lines:
        if line != "\n":
            current_cal += int(line)
        else:
            top_elves.compare_cal(calories=current_cal, elf=current_elf)
            current_cal = 0
            current_elf += 1

    top_elves.compare_cal(calories=current_cal, elf=current_elf)

print(top_elves)
