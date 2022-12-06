class CleanupAssignments():

    def __init__(self, *args, **kwargs):
        self.sum_assignment_pairs = 0

    def __str__(self):
        return('There are ' +
               str(self.sum_assignment_pairs) +
               ' assignment pairs where one range fully contains the other.')

    def range_inrange(self, *args, **kwargs):
        if ((args[0] <= args[2] <= args[1] and args[0] <= args[3] <= args[1]) or
           (args[2] <= args[0] <= args[3] and args[2] <= args[1] <= args[3])):
            return True
        else:
            return False

    def result(self, *args, **kwargs):
        with open(kwargs['f']) as f:
            lines = f.readlines()
            for line in lines:
                clean_line = line.splitlines()[0]
                ranges = clean_line.replace('-', ',').split(',')
                if self.range_inrange(int(ranges[0]), int(ranges[1]), int(ranges[2]), int(ranges[3])):
                    self.sum_assignment_pairs += 1

        return self.sum_assignment_pairs
