from utils import *
from random import randint
from time import sleep


# Messages
class msg:
    # Exit
    def exit():
        print(api.getMsg('msg.reveal').format(game['bomb']))
        print(api.getMsg('msg.exit'))
        sleep(1)

    # Skip
    def skip():
        print(api.getMsg('msg.reveal').format(game['bomb']))
        print(api.getMsg('msg.skip'))
        sleep(0.5)

    # Chaet
    def rev():
        print(api.getMsg('msg.reveal').format(game['bomb']))
        sleep(0.5)

    # Player wins
    def win():
        print("BOOM!")
        print(api.getMsg('msg.win'))
        sleep(1.5)

    # Player loses
    def lose():
        print("BOOM!")
        print(api.getMsg('msg.lose').format(game['bot-name']))
        sleep(1.5)

    # Welcome
    def welcome():
        print(api.getMsg('msg.welcome.1'))
        sleep(0.1)
        print(api.getMsg('msg.version').format(
            prof['version'], prof['author']))
        sleep(0.2)
        print(api.getMsg('msg.welcome.2'))
        sleep(0.1)
        print(api.getMsg('msg.welcome.3'))
        sleep(0.1)
        print(api.getMsg('msg.welcome.4'))
        sleep(0.1)


prof = api.getConfig('config\\profile')
data = api.getConfig('config\\settings')
names = api.getConfig('config\\names')
game = {
    'min': 0,
    'max': 0,
    'bot-name': 'null',
    'bomb': 0
}


def ranSet(a, b):
    return randint(a, b)


def Loop(game):
    game['min'] = data['start']
    game['max'] = data['end']
    game['bomb'] = ranSet(game['min']+1, game['max']-1)
    game['bot-name'] = names['name'][ranSet(0, len(names['name']) - 1)]
    sleep(0.5)

    print(api.getMsg('msg.match').format(game['bot-name']))
    print(api.getMsg('msg.ready'))

    MainGame()

    return Loop(game)


def MainGame():
    plInput = input(api.getMsg('msg.input').format(game['min'], game['max']))
    # Exit Game
    if plInput == "exit":
        msg.exit()
        exit(0)

    # Skip this round
    if plInput == "skip":
        msg.skip()
        return 0

    # Cheat
    if plInput == "rev":
        msg.rev()
        return MainGame()

    try:
        plNum = int(plInput)
    except ValueError:
        print(api.getMsg('msg.warn.int'))
        return MainGame()

    # Continue
    if plNum >= game['max']:
        print(api.getMsg('msg.warn.big').format(game['max']))
        return MainGame()
    if plNum <= game['min']:
        print(api.getMsg('msg.warn.little').format(game['min']))
        return MainGame()

    if plNum > game['bomb']:
        print(api.getMsg('msg.big'))
        game['max'] = plNum
    elif plNum < game['bomb']:
        print(api.getMsg('msg.little'))
        game['min'] = plNum
    else:
        msg.lose()
        return 0
    sleep(0.1)

    print(api.getMsg('msg.wait').format(game['bot-name']))
    sleep(0.5)
    botNum = randint(game['min'] + 1, game['max'] - 1)
    sleep(randint(1, 3))
    print(api.getMsg('msg.bot_input').format(game['bot-name'], botNum))
    if botNum > game['bomb']:
        print(api.getMsg('msg.big'))
        game['max'] = botNum
    elif botNum < game['bomb']:
        print(api.getMsg('msg.little'))
        game['min'] = botNum
    else:
        msg.win()
        return 0

    return MainGame()


# Game Route
msg.welcome()
Loop(game)
