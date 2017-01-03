import re

lines = open('input10.txt').read().split('\n')
numbers = re.compile(r'(\d+)')


class Output(object):

    def __init__(self, num):
        self.num = num
        self.nums = []

    def add_num(self, num2):
        if num2 not in self.nums:
            self.nums.append(num2)
            self.nums.sort()


class Bot(Output):

    def __init__(self, num):
        self.num = num
        self.nums = []
        self.high = None
        self.low = None


class AllBots(object):

    def __init__(self):
        self.bots = set()

    def add_bot(self, bot):
        self.bots.add(bot)

    def find_bot(self, bot_num):
        for bot in self.bots:
            if bot.num == bot_num:
                return bot

    def __repr__(self):
        repr_string = ""
        for bot in self.bots:
            repr_string += str(bot.num) + ", "
        return repr_string

all_bots = AllBots()
all_outputs = AllBots()

for line in lines:
    bots = map(int, numbers.findall(line))
    if line[0] == "v":
        bot = all_bots.find_bot(bots[1])
        if not bot:
            bot = Bot(bots[1])
            all_bots.add_bot(bot)
        bot.add_num(bots[0])
    else:
        bot = all_bots.find_bot(bots[0])
        if not bot:
            bot = Bot(bots[0])
            all_bots.add_bot(bot)
        line = line.split()
        if line[5] == "bot":
            bot.low = all_bots.find_bot(bots[1])
            if not all_bots.find_bot(bots[1]):
                new_low = Bot(bots[1])
                all_bots.add_bot(new_low)
                bot.low = new_low
        else:
            bot.low = all_outputs.find_bot(bots[1])
            if not all_outputs.find_bot(bots[1]):
                new_low = Output(bots[1])
                all_outputs.add_bot(new_low)
                bot.low = new_low
        if line[10] == "bot":
            bot.high = all_bots.find_bot(bots[2])
            if not all_bots.find_bot(bots[2]):
                new_high = Bot(bots[2])
                all_bots.add_bot(new_high)
                bot.high = new_high
        else:
            bot.high = all_outputs.find_bot(bots[2])
            if not all_outputs.find_bot(bots[2]):
                new_high = Output(bots[2])
                all_outputs.add_bot(new_high)
                bot.high = new_high

print "All bots added: ", all_bots
print "All outputs added: ", all_outputs

skip = set()
while len(skip) < len(all_bots.bots):
    for bot in all_bots.bots:
        if bot in skip:
            continue
        if len(bot.nums) > 1:
            if bot.nums == [17, 61]:
                print "Part 1: ", bot.num
            bot.low.add_num(bot.nums[0])
            bot.high.add_num(bot.nums[-1])
            skip.add(bot)
            print "Completed: bot", bot.num

part_two = reduce((lambda x, y: x*y), [output.nums[0] for output in all_outputs.bots if output.num in [0, 1, 2]])
print "Part 2: ", part_two

# Part 1: 141
# Part 2: 1209
