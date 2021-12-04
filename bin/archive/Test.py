import WeaponGenerator
import Rarity

# for i in range(100):
# print(Rarity.random_rarity().name)

list = WeaponGenerator.generate_list(300)

for w in list:
    print(str(w))

print(len(list))
input()
