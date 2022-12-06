class PackOrganizer():

    def __init__(self, *args, **kwargs):
        self.sum_priorities = 0

        with open(kwargs['f']) as f:
            lines = f.readlines()

            for line in lines:
                items = line.splitlines()[0]
                self.find_common_item(items=items)

    def __str__(self):
        return 'The sum of all the priorities is ' + str(self.sum_priorities) + '.'

    def add_priority(self, *args, **kwargs):
        item_alphabet = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.sum_priorities += item_alphabet.find(kwargs['common_item'])

    def find_common_item(self, *args, **kwargs):
        num_items = int(len(kwargs['items']) / 2)

        compartment_one = kwargs['items'][:num_items]
        compartment_two = kwargs['items'][num_items:]

        common_item = ''.join(list(set(compartment_one) & set(compartment_two)))
        self.add_priority(common_item=common_item)

    def result(self):
        return self.sum_priorities
