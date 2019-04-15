import random

info = ['info1', 'io1', 'ac1', 'sh1', 'tm1', 'llc1', 'pet1', 'bet', 'pro', 'mobi', 'black', 'blue', 'kim', 'lgbt', 'pink', 'poker', 'red', 'shiksha', 'green', 'vote', 'voto', 'xn-6frz82g']


def randomTld(contractName):
    return '.'+random.choice(contractName)