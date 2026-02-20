import random


# ATTACKS

# AQUA
async def aquaAttack1(ctx, player, enemy):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Aqua splashes water on {enemy['name']} for {player['ATK']} damage!")

async def aquaAttack2(ctx, player, enemy):
    player['HP'] += 2
    await ctx.send("Aqua heals herself for 2 HP!")


async def darknessAttack1(ctx, player, enemy):
    enemy['HP'] -= player['ATK']
    await ctx.send(f"Darkness slashes at {enemy['name']} and deals {player['ATK']} damage!")

async def darknessAttack2(ctx, player, enemy):
    player['BLOCKS'] += 1
    await ctx.send("Darkness prepares to block the next attack!")


async def meguminAttack1(ctx, player, enemy):
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
                          "action": aquaAttack1},
                    "2": {"name": "Heal",
                          "desc": "Heals herself for 2 HP.",
                          "action": aquaAttack2}
                }
            },
        "darkness":
            {
                "name": "Darkness",
                "rarity": "Rare",
                "image": "https://cdn.myanimelist.net/images/characters/7/301407.jpg",
                "HP": 8,
                "MAXHP": 8,
                "ATK": 1,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Sword Slash",
                          "desc": "Slash at the enemy to deal 1 ATK.",
                          "action": darknessAttack1},
                    "2": {"name": "Guard",
                          "desc": "Blocks the next attack.",
                          "action": darknessAttack2}
                }
            },
        "megumin":
            {
                "name": "Megumin",
                "rarity": "Epic",
                "image": "https://cdn.myanimelist.net/images/characters/2/309075.jpg",
                "HP": 5,
                "MAXHP": 5,
                "ATK": 3,
                "BLOCKS": 0,
                "moves": {
                    "1": {"name": "Explosion",
                          "desc": "Deal 3 damage",
                          "action": ""},
                }
            },
    }





world1Enemies = {
            "sprite":
                {
                    "name": "Sprite",
                    "HP": 2,
                    "ATK": 1
                },
            "slime":
                {
                    "name": "Slime",
                    "HP": 3,
                    "ATK": 1
                },
            "goblin":
                {
                    "name": "Goblin",
                    "HP": 4,
                    "ATK": 1
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