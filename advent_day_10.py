import re
# from collections import defaultdict

lines = open('input10.txt').read().split('\n')
numbers = re.compile(r'(\d+)')
# all_bots = defaultdict(list)


class Bot(object):

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

for line in lines:
    bots = map(int, numbers.findall(line))
    if line[0] == "v":
        bot = all_bots.find_bot(bots[1])
        if not bot:
            bot = Bot(bots[1])
            all_bots.add_bot(bot)
        if bots[0] not in bot.nums:
            bot.nums.append(bots[0])
            bot.nums.sort()
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
        if line[10] == "bot":
            bot.high = all_bots.find_bot(bots[2])
            if not all_bots.find_bot(bots[2]):
                new_high = Bot(bots[2])
                all_bots.add_bot(new_high)
                bot.high = new_low 
print all_bots
