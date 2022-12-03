class PackOrganizer():

    def __init__(self, *args, **kwargs):
        self.sum_priorities = 0
        self.threesome = []

    def __str__(self):
        return 'The sum of all the priorities is ' + str(self.sum_priorities) + '.'

    def add_priority(self, *args, **kwargs):
        item_alphabet = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.sum_priorities += item_alphabet.find(kwargs['common_item'])

    def find_common_item(self, *args, **kwargs):
        bags = kwargs['bags']

        common_item = ''.join(list(set(bags[0]) & set(bags[1]) & set(bags[2])))
        self.add_priority(common_item=common_item)

    def get_threesome(self, *args, **kwargs):
        self.threesome.append(kwargs['items'])
        if len(self.threesome) == 3:
            self.find_common_item(bags=self.threesome)
            self.threesome.clear()


pack = PackOrganizer()

with open('input.txt') as f:
    lines = f.readlines()

    for line in lines:
        items = line.splitlines()[0]
        pack.get_threesome(items=items)

print(pack)
