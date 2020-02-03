import random


def printKeyValue(key, start, end):
    value = random.randint(start, end)
    print(key, ":", value)


userInput = input("Please enter value:")
printKeyValue(userInput, 0, 20)
