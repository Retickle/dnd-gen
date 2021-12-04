from Weapon import Weapon
import WeaponGenerator
from Tools import Tools


lst = WeaponGenerator.generate_list(100)
for w in lst:
    print(str(w))
