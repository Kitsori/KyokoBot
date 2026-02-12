import random

# class Move:
#     def __init__(self, name, stat, value, target, desc):
#         self.name = name
#         self.stat = stat      # "HP" or "ATK"
#         self.value = value    # number or "ATK"
#         self.target = target  # "self" or "enemy"
#         self.desc = desc
#
#     def apply(self, user, target):
#         # Determine actual amount
#         amount = user.atk if self.value == "ATK" else self.value
#
#         if self.stat == "HP":
#             if self.target == "self":
#                 user.hp += amount
#             else:
#                 target.hp -= amount
#         elif self.stat == "ATK":
#             if self.target == "self":
#                 user.atk += amount
#             else:
#                 target.atk -= amount
#         return amount
#
# class Character:
#     def __init__(self, name, show, rarity, url, stats_by_level, moves_by_level):
#         self.name = name
#         self.show = show
#         self.rarity = rarity
#         self.url = url
#         self.stats_by_level = stats_by_level
#         self.moves_by_level = moves_by_level
#
#         self.level = 1
#         self.hp = stats_by_level[self.level]["HP"]
#         self.atk = stats_by_level[self.level]["ATK"]
#
#     @property
#     def moves(self):
#         return self.moves_by_level[self.level]
#
#
#
#
#
# # Define characters
# rpgGirls = []
#
# # Aqua
# aqua_moves = {
#     1: Move("Attack", "HP", "ATK", "enemy", "Deals damage equal to ATK."),
#     2: Move("Heal", "HP", 2, "self", "Heals 2 HP.")
# }
# aqua_stats = {
#     1: {"HP": 5, "ATK": 1},
#     2: {"HP": 6, "ATK": 1},
#     3: {"HP": 7, "ATK": 2}
# }
# rpgGirls.append(Character("Aqua", "Konosuba", "Common", "https://cdn.myanimelist.net/images/characters/13/327741.jpg", aqua_stats, {1: aqua_moves}))
#
#
#
#
#
# # Darkness
# darkness_moves = {
#     1: Move("Attack", "HP", 2, "enemy", "Deals 2 damage."),
#     2: Move("Heal", "HP", 2, "self", "Heals 2 HP.")
# }
# darkness_stats = {
#     1: {"HP": 8, "ATK": 1},
#     2: {"HP": 9, "ATK": 1},
#     3: {"HP": 10, "ATK": 1}
# }
# rpgGirls.append(Character("Darkness", "Konosuba", "Uncommon", "https://cdn.myanimelist.net/images/characters/7/301407.jpg", darkness_stats, {1: darkness_moves}))
#
#
#
#
#
# # Megumin
# megumin_moves = {
#     1: Move("Attack", "HP", 2, "enemy", "Deals 2 damage."),
#     2: Move("Heal", "HP", 1, "self", "Heals 1 HP.")
# }
# megumin_stats = {
#     1: {"HP": 5, "ATK": 2},
#     2: {"HP": 6, "ATK": 2},
#     3: {"HP": 7, "ATK": 3}
# }
# rpgGirls.append(Character("Megumin", "Konosuba", "Epic", "https://cdn.myanimelist.net/images/characters/2/309075.jpg", megumin_stats, {1: megumin_moves}))
#
#
#
#
#
# def rpgDictionary():
#     return {char.name.lower(): char for char in rpgGirls}
#
# def randomGirl():
#     return random.choice(rpgGirls)