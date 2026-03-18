import random


# ATTACKS

# AQUA
async def aquaAttack1(ctx, player, enemy, enemy2):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Aqua splashes water on {enemy['name']} for {player['ATK']} damage!")

async def aquaAttack2(ctx, player):
    player['HP'] += 2

    if player['HP'] > player['MAXHP']:
        player['HP'] = player['MAXHP']

    await ctx.send("Aqua heals herself for 2 HP!")




async def darknessAttack1(ctx, player, enemy, enemy2):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Darkness slashes at {enemy['name']} and deals {player['ATK']} damage!")

async def darknessAttack2(ctx, player):
    player['BLOCKS'] += 1
    await ctx.send(f"Darkness shields {player['name']} from the next attack on them!")




async def wizAttack1(ctx, player, enemy, enemy2):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Wiz drains {player['ATK']} of {enemy['name']}'s HP!")

async def wizAttack2(ctx, player, enemy, enemy2):
    chance = random.randint(1, 100)
    if chance > 50:
        enemy['FROZEN'] += 1
        await ctx.send(f"Wiz petrified {enemy['name']}!")
    else:
        await ctx.send("Wiz's petrification failed!")



async def yunyunAttack1(ctx, player, enemy, enemy2):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Yunyun fires a fireball at {enemy['name']} for {player['ATK']} damage!")


async def yunyunAttack2(ctx, player, enemy, enemy2):
    atk = player['ATK'] - 1
    chance = random.randint(1, 100)
    enemy['HP'] -= atk
    await ctx.send(f"Yunyun fires a bolt of lighting at {enemy['name']} for {atk} damage!")
    if chance > 1:
        enemy2['HP'] -= atk
        await ctx.send(f"The bolt bounced to {enemy2['name']} for {atk} damage!")




async def meguminAttack(ctx, player, enemy, enemy2):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Megumin sets off an explosion on {enemy['name']} for {player['ATK']} damage!")





rpgGirls = {
        "aqua":
            {
                "name": "Aqua",
                "rarity": "Common",
                "image": "https://cdn.myanimelist.net/images/characters/13/327741.jpg",
                "HP": 5,
                "MAXHP": 5,
                "ATK": 1,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Create Water!",
                          "desc": "Shoot a beam of water at the enemy to deal 1 ATK.",
                          "target": "Enemy",
                          "action": aquaAttack1},
                    "2": {"name": "Heal",
                          "desc": "Heals herself for 2 HP.",
                          "target": "Self",
                          "action": aquaAttack2}
                }
            },
        "darkness":
            {
                "name": "Darkness",
                "rarity": "Common",
                "image": "https://cdn.myanimelist.net/images/characters/7/301407.jpg",
                "HP": 7,
                "MAXHP": 7,
                "ATK": 1,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Sword Slash",
                          "desc": "Slash at a target to deal 1 ATK.",
                          "target": "Enemy",
                          "action": darknessAttack1},
                    "2": {"name": "Guard",
                          "desc": "Blocks the next attack. Give to any team member.",
                          "target": "Team",
                          "action": darknessAttack2}
                }
            },
        "wiz":
            {
                "name": "Wiz",
                "rarity": "Rare",
                "image": "https://cdn.myanimelist.net/images/characters/14/312300.jpg",
                "HP": 5,
                "MAXHP": 5,
                "ATK": 2,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Drain Touch",
                          "desc": "Drains 2 HP from the target.",
                          "target": "Enemy",
                          "action": wizAttack1},
                    "2": {"name": "Petrification",
                          "desc": "Petrifies the target. 50% chance of success.",
                          "target": "Enemy",
                          "action": wizAttack2}
                }
            },
        "yunyun":
            {
                "name": "Yunyun",
                "rarity": "Rare",
                "image": "https://cdn.myanimelist.net/images/characters/13/583284.jpg",
                "HP": 5,
                "MAXHP": 5,
                "ATK": 2,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Fireball",
                          "desc": "Blasts a fireball at the target for 2 ATK.",
                          "target": "Enemy",
                          "action": yunyunAttack1},
                    "2": {"name": "Lighting",
                          "desc": "Fires a lighting bolt at the target for 1 ATK, with a 50% chance to hit the other target as well.",
                          "target": "Enemy",
                          "action": yunyunAttack2}
                }
            },
        "megumin":
            {
                "name": "Megumin",
                "rarity": "Epic",
                "image": "https://cdn.myanimelist.net/images/characters/2/309075.jpg",
                "HP": 4,
                "MAXHP": 4,
                "ATK": 4,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Explosion",
                          "desc": "Create an explosion on an enemy for 4 ATK.",
                          "target": "Enemy",
                          "action": meguminAttack},
                }
            },
    }





world1Enemies = {
            "sprite":
                {
                    "name": "Sprite",
                    "HP": 2,
                    "ATK": 1,
                    "FROZEN": 0,
                },
            "slime":
                {
                    "name": "Slime",
                    "HP": 3,
                    "ATK": 1,
                    "FROZEN": 0,
                },
            "goblin":
                {
                    "name": "Goblin",
                    "HP": 4,
                    "ATK": 1,
                    "FROZEN": 0,
                },
        }


world1Bosses = {
            "demon":
                {
                    "name": "Demon",
                    "HP": 5,
                    "ATK": 2
                },
            "dragon":
                {
                    "name": "Dragon",
                    "HP": 7,
                    "ATK": 2
                },

}