import re

lines = open('input10.txt').read().split('\n')
numbers = re.compile(r'(\d+)')

for line in lines:
    bots = map(int, numbers.findall(line))


    # bots = {}
    # for line in bot_file:
    #     line = line.rstrip().split()
    #     if line[0] == "value":
    #         value = int(line[1])
    #         destination = line[-2]
    #         destination_num = line[-1]
    #         if destination == "bot":
    #             bots[destination_num] = bots.get(destination_num, {"low_to": None, "high_to": None, "nums": set()})
    #             bots[destination_num]["nums"].add(value)
    #             if len(bots[destination_num]["nums"]) == 2:
    #                 print giver_bot, "should be 104"
    #                 low, high = sorted(list(bots[destination_num]["nums"]))
    #                 if bots[destination_num]["low_to"]:
    #                     low_recipient = bots[destination_num]["low_to"]
    #                     bots[low_recipient = bots.get(low_recipient, {"low_to": None, "high_to": None, "nums": set()})
    #                     bots[low_recipient["nums"].add(low)
    #                 if bots[destination_num]["high_to"]:
    #                     bots[high_recipient[1]] = bots.get(high_recipient[1], {"low_to": None, "high_to": None, "nums": set()})
    #                     bots[high_recipient[1]]["nums"].add(high)
    #     else:
    #         giver_bot = line[1]
    #         low_recipient = line[5:7]
    #         high_recipient = line[10:]
    #         bots[giver_bot] = bots.get(giver_bot, {"low_to": None, "high_to": None, "nums": set()})
    #         bots[giver_bot]["low_to"] = low_recipient[1]
    #         bots[giver_bot]["high_to"] = high_recipient[1]
    #         if len(bots[giver_bot]["nums"]) == 2:
    #             # print giver_bot, "should be 104"
    #             low, high = sorted(list(bots[giver_bot]["nums"]))
    #             if low_recipient[0] == "bot":
    #                 bots[low_recipient[1]] = bots.get(low_recipient[1], {"low_to": None, "high_to": None, "nums": set()})
    #                 bots[low_recipient[1]]["nums"].add(low)
    #             if high_recipient[0] == "bot":
    #                 bots[high_recipient[1]] = bots.get(high_recipient[1], {"low_to": None, "high_to": None, "nums": set()})
    #                 bots[high_recipient[1]]["nums"].add(high)

# for k in bots:
#     print k, bots[k]

# print len(bots), complete_sets
