# tool methods
import random as rnd


# returns random element from list
def random(list):
    index = rnd.randint(0, len(list)-1)
    return list[index]


# returns true or false
def chance(percent):
    # invalid percent
    if percent < 0:
        return False

    # invalid > 100 percent
    if(percent > 100):
        return True

    num = rnd.randint(1, 100)

    if(num <= percent):
        return True
    else:
        return False
