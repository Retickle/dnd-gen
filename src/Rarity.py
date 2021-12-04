from enum import Enum
import random as rnd

Legendary_Percent = 2.5
Very_Rare_Percent = 7.5
Rare_Percent = 15
Uncommon_Percent = 25
Common_Percent = 50

Percent_Multiplier = 10


class RarityType(Enum):
    Common = 1
    Uncommon = 2
    Rare = 3
    Very_Rare = 4
    Legendary = 5


def random():
    """Returns a random RarityType based on percentages."""
    num = rnd.randint(1, 100 * Percent_Multiplier)

    lower = 0
    upper = Legendary_Percent * Percent_Multiplier

    if num <= upper:
        return RarityType.Legendary

    lower = upper
    upper = (Very_Rare_Percent * Percent_Multiplier) + lower

    if num > lower and num <= upper:
        return RarityType.Very_Rare

    lower = upper
    upper = (Rare_Percent * Percent_Multiplier) + lower

    if num > lower and num <= upper:
        return RarityType.Rare

    lower = upper
    upper = (Uncommon_Percent * Percent_Multiplier) + lower

    if num > lower and num <= upper:
        return RarityType.Uncommon

    lower = upper
    upper = (Common_Percent * Percent_Multiplier) + lower

    if num > lower and num <= upper:
        return RarityType.Common
