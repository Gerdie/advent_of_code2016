
with open('input10.txt') as bot_file:
    bots = {}
    for line in bot_file:
        line = line.rstrip().split()
        if line[0] == "value":
            value = line[1]
            destination = line[-2]
            destination_num = line[-1]
        else:
            giver_bot = line[1]
            low_recipient = line[5:7]
            high_recipient = line[10:]
