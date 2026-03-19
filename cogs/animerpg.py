import discord
from discord.ext import commands
import asyncio
import traceback
import random
import copy

from cogs.rpggirls import rpgGirls, world1Enemies, world1Bosses


rarityWeights = \
    {
        "Common": 60,
        "Rare": 30,
        "Epic": 10
    }


charOrder = ["Aqua", "Darkness", "Wiz", "Yunyun", "Megumin"]


class AnimeRPG(commands.Cog):

    rpgColor = 0x4B9DAD


    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.players = db["Players"]
        self.fragments = db["Fragments"]




    # Find a player's file, if not existing create one with defaults
    def findPlayer(self, user_id: int):
        player = self.players.find_one({"_id": user_id})
        if not player:
            player = {
                "_id": user_id,
                "world": 1,
                "characters": ["Aqua", "Darkness"],
                "coins": 0,
                "levels": {"Aqua": 1, "Darkness": 1},
                "fragments": {"Aqua": 0, "Darkness": 0}
            }
            self.players.insert_one(player)
            new = True
        else:
            new = False
        return player, new

    # Find a player's character list and add one
    def addCharacter(self, user_id: int, char_name: str):
        self.players.update_one(
            {"_id": user_id},
            {"$addToSet": {"characters": char_name}},
            upsert=True
        )

    # Find a player's coin list and add to it
    def changeCoins(self, user_id: int, amount: int):
        self.players.update_one(
            {"_id": user_id},
            {"$inc": {"coins": amount}},
            upsert=True
        )

    # Find the player's world number and update
    def changeWorld(self, user_id: int, amount: int):
        self.players.update_one(
            {"_id": user_id},
            {"$inc": {"world": amount}},
            upsert=True
        )

    def changeFragments(self, user_id: int, character: str, amount: int):
        self.players.update_one(
            {"_id": user_id},
            {"$inc": {f"fragments.{character}": amount}},
            upsert=True
        )

    def changeLevel(self, user_id: int, character: str, amount: int):
        self.players.update_one(
            {"_id": user_id},
            {"$inc": {f"levels.{character}": amount}},
            upsert=True
        )

    # Colors for rarities for embeds
    def rarityColor(self, rarity):

        if rarity == "Common":
            return 0x34cceb
        elif rarity == "Rare":
            return 0x34eb3a
        elif rarity == "Epic":
            return 0xf538ff


    @commands.command()
    async def ccccc(self, ctx):
        player = self.findPlayer(ctx.author.id)
        self.changeCoins(ctx.author.id, 10)
        await ctx.send("+10 Coins!")


    @commands.command()
    async def summon(self, ctx):
        player, new = self.findPlayer(ctx.author.id)

        if new == True:
            await ctx.send("Oh, its your first time playing! Take Aqua and Darkness for free to start! :3")


        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send("A character summon costs 10 coins. Do you want to summon? ('y' to confirm) \n"
                       "View rarity chances with ~summonrates")

        msg = await self.bot.wait_for('message', check=check)
        choice = msg.content.strip()

        if choice.lower() == "y":

            if player["coins"] < 10:
                await ctx.send("You don't have enough coins.")
                return

            self.changeCoins(ctx.author.id, -10)

            num = random.randint(1, 100)

            if 60 >= num >= 1:
                rarity = "Common"
            elif 90 >= num >= 61:
                rarity = "Rare"
            elif 100 >= num >= 91:
                rarity = "Epic"


            chars = [c for c in rpgGirls.values() if c["rarity"] == rarity and int(c["world"]) <= player["world"]]
            character = random.choice(chars)

            msg = await ctx.send("Summoning.")
            await asyncio.sleep(1)
            await msg.edit(content="Summoning..")
            await asyncio.sleep(1)
            if rarity == "Rare":
                await msg.edit(content="Summoning...")
                await asyncio.sleep(1)
            if rarity == "Epic":
                await msg.edit(content="Summoning...")
                await asyncio.sleep(1)
                await msg.edit(content="Summoning....")
                await asyncio.sleep(1)
            if rarity == "Legendary":
                await msg.edit(content="Summoning...")
                await asyncio.sleep(1)
                await msg.edit(content="Summoning....")
                await asyncio.sleep(1)
                await msg.edit(content="Summoning.....")
                await asyncio.sleep(1)

            summonEmbed = discord.Embed(title=f"You summoned {character['name']}!", color=self.rarityColor(character["rarity"]))
            summonEmbed.set_image(url=character["image"])

            await ctx.send(embed=summonEmbed)

            if character["name"] in player["characters"]:
                await ctx.send("You already own this character!")

                fragmentEmbed = discord.Embed(
                    title=f"+1 {character['name']} fragment!",
                    color=self.rarityColor(character["rarity"])
                )
                await ctx.send(embed=fragmentEmbed)

                self.changeFragments(ctx.author.id, character["name"], 1)

            else:
                # NEW CHARACTER
                await ctx.send(f"New character unlocked: {character['name']}!")

                self.addCharacter(ctx.author.id, character["name"])

                # initialize level
                self.players.update_one(
                    {"_id": ctx.author.id},
                    {"$set": {f"levels.{character['name']}": 1}},
                    upsert=True
                )

        else:
            await ctx.send("Okay... I'll be waiting for your next summon!")



    @commands.command()
    async def summonrates(self, ctx):
        ratesEmbed = discord.Embed(title="KyokoRPG Summon Rates",
                                   description="─ · ─ · ─ · ─ · ─ · ─ ✴︎ ─ · ─ · ─ · ─ · ─ · ─",
                                   color=self.rpgColor)

        ratesEmbed.add_field(name="Common: 60%", value='', inline=False)
        ratesEmbed.add_field(name="Rare: 30%", value='', inline=False)
        ratesEmbed.add_field(name="Epic: 10%", value='', inline=False)

        await ctx.send(embed=ratesEmbed)



    @commands.command()
    async def coins(self, ctx):
        player, new = self.findPlayer(ctx.author.id)

        if new == True:
            await ctx.send("Oh, its your first time playing! Take Aqua and Darkness for free to start! :3")


        coinEmbed = discord.Embed(title=f"You have {player['coins']} coins!",
                                  color=self.rpgColor)
        coinEmbed.set_footer(text="KyokoRPG")

        await ctx.send(embed=coinEmbed)



    @commands.command()
    async def characterlist(self, ctx):

        player, new = self.findPlayer(ctx.author.id)

        if new == True:
            await ctx.send("Oh, its your first time playing! Take Aqua and Darkness for free to start! :3")


        commonEmbed = discord.Embed(title="COMMON (3)", color=0x34cceb)
        rareEmbed = discord.Embed(title="RARE (3)", color=0x34eb3a)
        epicEmbed = discord.Embed(title="EPIC (1)", color=0xf538ff)


        for char in rpgGirls.values():
            if char["rarity"] == "Common":
                found = False
                name = char["name"]
                for c in player['characters']:
                    if c == name:
                        level = player['levels'].get(c)
                        commonEmbed.add_field(name=f"- {char['name']} (Lvl {level})", value='', inline=False)
                        found = True
                if found == False:
                    commonEmbed.add_field(name=f"- ??? (W{char['world']})", value='', inline=False)


            elif char["rarity"] == "Rare":
                found = False
                name = char["name"]
                for c in player['characters']:
                    if c == name:
                        level = player['levels'].get(c)
                        rareEmbed.add_field(name=f"- {char['name']} (Lvl {level})", value='', inline=False)
                        found = True
                if found == False:
                    rareEmbed.add_field(name=f"- ??? (W{char['world']})", value='', inline=False)

            elif char["rarity"] == "Epic":
                found = False
                name = char["name"]
                for c in player['characters']:
                    if c == name:
                        level = player['levels'].get(c)
                        epicEmbed.add_field(name=f"- {char['name']} (Lvl {level})", value='', inline=False)
                        found = True
                if found == False:
                    epicEmbed.add_field(name=f"- ??? (W{char['world']})", value='', inline=False)

        await ctx.send(embeds=[commonEmbed, rareEmbed, epicEmbed])



    @commands.command()
    async def levelup(self, ctx, character=None):
        user, new = self.findPlayer(ctx.author.id)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        if character is None:
            await ctx.send("Who do you want to level up?")

            msg = await self.bot.wait_for("message", check=check, timeout=30)
            character = msg.content.strip()


        charName = character.capitalize()

        if charName not in user['characters']:
            await ctx.send("You don't own that character!")
            return

        level = user['levels'].get(charName)
        fragments = user['fragments'].get(charName)

        if level == 1:
            required = 2
        elif level == 2:
            required = 3
        elif level == 3:
            required = 5
        elif level == 4:
            required = 8
        elif level == 5:
            required = 12

        if fragments >= required:
            await ctx.send(f"You have {fragments} {charName} fragments. \n"
                           f"You need {required} fragments to level up.")
            await ctx.send(f"Do you want to level up {charName}? (y/n)")

            msg = await self.bot.wait_for("message", check=check, timeout=30)
            content = msg.content.strip()

            if content.lower() == "y":
                self.changeLevel(ctx.author.id, charName, 1)
                self.changeFragments(ctx.author.id, charName, -required)
                await ctx.send(f"{charName} leveled up to level {level + 1}!")
            else:
                await ctx.send("Come back when you're ready!")
        else:
            await ctx.send(f"You need {required} fragments to level up to Level {level + 1}. \n"
                           f"You don't have enough fragments/coins to level up currently.")




    @commands.command()
    async def fragments(self, ctx):
        player, new = self.findPlayer(ctx.author.id)

        fragEmbed = discord.Embed(title=f"{ctx.author.display_name}'s Fragments", color=0xE6A0E8)

        for char in charOrder:
            frags = player["fragments"].get(char, 0)

            if frags == 0:
                continue

            fragEmbed.add_field(name=f"**{char}**: {frags}", value='', inline=False)

        await ctx.send(embed=fragEmbed)




    @commands.command()
    async def worldup(self, ctx):
        player, new = self.findPlayer(ctx.author.id)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        coins = player["coins"]
        world = player["world"]

        if world == 1:
            required = 50
        if world == 2:
            required = 150

        if coins >= required:
            await ctx.send(f"You need {required} coins to get to the next world. \n"
                           f"You have {coins} coins. Do you want to advance to the next world? (y/n)")

            msg = await self.bot.wait_for("message", check=check, timeout=30)
            content = msg.content.strip()

            if content.lower() == "y":
                self.changeWorld(ctx.author.id, 1)
                self.changeCoins(ctx.author.id, -required)
                await ctx.send(f"{ctx.author.display_name} advanced to world {world + 1}!")
            else:
                await ctx.send("Come back when you're ready!")
        else:
            await ctx.send(f"You need {required} coins to get to the next world. \n"
                           f"You only have {coins} coins currently.")






    @commands.command()
    async def run(self, ctx):

        # Setup Check
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Find the user running the command's RPG File
        user, new = self.findPlayer(ctx.author.id)

        await ctx.send("Starting a new run!")
        await asyncio.sleep(1)
        await ctx.send("Type 'quit' at any time to end the run early!")

        if new == True:
            await ctx.send("Oh, its your first time playing! Take Aqua and Darkness for free to start! :3")


        # Create the list of the player's characters
        charList = ""
        await ctx.send("Choose your first character: ")

        for char in user["characters"]:
            charList += f"- {char}\n"

        await ctx.send(charList)


        # First character
        try:
            picking = True
            while picking:
                msg = await self.bot.wait_for('message', check=check)
                playerChoice = msg.content

                valid = False

                if playerChoice.lower() == "quit":
                    await ctx.send("Stopping run!")
                    return

                for c in user["characters"]:
                    char = c.lower()
                    if playerChoice.lower() == char:
                        player = copy.deepcopy(rpgGirls[char])


                        picking = False
                        valid = True
                        await ctx.send(f"You selected {char.capitalize()} as your first team member!")
                        await asyncio.sleep(1)
                        break

                if not valid:
                    await ctx.send("You don't have that character silly!")

            level = user["levels"][player['name']]  # or whatever level system you use
            stats = player["levels"][level]

            player["HP"] = stats["HP"]
            player["MAXHP"] = stats["MAXHP"]
            player["ATK"] = stats["ATK"]




            await ctx.send("Choose your second character: ")

            # Second character
            picking2 = True
            while picking2:
                msg2 = await self.bot.wait_for('message', check=check)
                playerChoice2 = msg2.content

                valid = False

                if playerChoice.lower() == "quit":
                    await ctx.send("Stopping run!")
                    return

                if playerChoice2.lower() == playerChoice.lower():
                    await ctx.send("You already picked that character silly!")
                    continue

                for c in user["characters"]:
                    char = c.lower()
                    if playerChoice2.lower() == char:
                        player2 = copy.deepcopy(rpgGirls[char])

                        picking2 = False
                        valid = True
                        await ctx.send(f"You selected {char.capitalize()} as your second team member!")
                        await asyncio.sleep(1)
                        break

                if not valid:
                    await ctx.send("You don't have that character silly!")

            level = user["levels"][player2['name']]  # or whatever level system you use
            stats2 = player2["levels"][level]

            player2["HP"] = stats2["HP"]
            player2["MAXHP"] = stats2["MAXHP"]
            player2["ATK"] = stats2["ATK"]


        except Exception as e:
            print(e)



        world = user["world"]


        # Get that character's info
        try:


            # Room counter
            room = 1
            roomCleared = False

            alive = True
            player1Alive = True
            player2Alive = True




            while alive == True:

                roomCleared = False

                # Generate enemies, dependant on world
                if world == 2 and room % 5 != 0:
                    enemy = copy.deepcopy(random.choice(list(world1Enemies.values())))
                    enemy2 = copy.deepcopy(random.choice(list(world1Enemies.values())))
                elif world == 2 and room % 5 == 0:
                    enemy = copy.deepcopy(random.choice(list(world1Bosses.values())))
                    enemy2 = {"name": "None", "HP": 0, "ATK": 0}
                    color = 0xFF0000
                    bossEmbed = discord.Embed(title="BOSS INCOMING...",
                                              color=color)
                    await ctx.send(embed=bossEmbed)
                    await asyncio.sleep(2)

                # Setup turn counter
                turn = 0
                enemy1Alive = True
                enemy2Alive = True
                enemy2Exists = True

                barValue = player['MAXHP'] / 10
                barValue2 = player2['MAXHP'] / 10

                barValueE = enemy['HP'] / 10

                if enemy2['HP'] > 0:
                    barValueE2 = enemy2['HP'] / 10
                else:
                    barValueE2 = 0
                    enemy2Exists = False

                while (player['HP'] > 0 or player2['HP'] > 0) and (enemy['HP'] > 0 or enemy2['HP'] > 0):

                    barCountDouble = player["HP"] / barValue
                    barCountDouble2 = player2["HP"] / barValue2

                    barCountDoubleE = enemy["HP"] / barValueE

                    if enemy2Exists == True:
                        barCountDoubleE2 = enemy2["HP"] / barValueE2
                    else:
                        barCountDoubleE2 = 0

                    barCount = round(barCountDouble)
                    barCount2 = round(barCountDouble2)

                    barCountE = round(barCountDoubleE)
                    barCountE2 = round(barCountDoubleE2)

                    bars = ""
                    bars2 = ""

                    barsE = ""
                    barsE2 = ""

                    remBars = 10 - barCount
                    remBars2 = 10 - barCount2

                    remBarsE = 10 - barCountE
                    remBarsE2 = 10 - barCountE2

                    for i in range(barCount):
                        bars += "█"

                    for i in range(remBars):
                        bars += "░"

                    for i in range(barCount2):
                        bars2 += "█"

                    for i in range(remBars2):
                        bars2 += "░"



                    for i in range(barCountE):
                        barsE += "█"

                    for i in range(remBarsE):
                        barsE += "░"

                    for i in range(barCountE2):
                        barsE2 += "█"

                    for i in range(remBarsE2):
                        barsE2 += "░"


                    if turn % 4 == 0:
                        active = player['name']
                        image = player['image']
                        rarity = player['rarity']
                    elif turn % 4 == 1:
                        active = player2['name']
                        image = player2['image']
                        rarity = player2['rarity']
                    elif turn % 4 == 2:
                        active = enemy['name']
                    elif turn % 4 == 3:
                        active = enemy2['name']


                    if turn % 4 == 0 or turn % 4 == 1:
                        color = self.rarityColor(rarity)
                    elif turn % 4 == 2 or turn % 4 == 3:
                        color = 0x874545

                    statusEmbed = discord.Embed(title=f"{active}'s Turn!",
                                                color=color)

                    statusEmbed.add_field(name=f"{player['name']} (Lvl {user['levels'][player['name']]})", value=f"{player['HP']} HP\n ║{bars}║", inline=True)
                    statusEmbed.add_field(name=f"{player2['name']} (Lvl {user['levels'][player2['name']]})", value=f"{player2['HP']} HP\n ║{bars2}║", inline=True)

                    statusEmbed.add_field(name="\u200b", value="─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ VS ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─", inline=False)

                    statusEmbed.add_field(name=enemy['name'], value=f"{enemy['HP']} HP\n ║{barsE}║", inline=True)

                    if enemy2Exists == True:
                        statusEmbed.add_field(name=enemy2['name'], value=f"{enemy2['HP']} HP\n ║{barsE2}║", inline=True)

                    if turn % 4 == 0 or turn % 4 == 1:
                        statusEmbed.set_image(url=image)

                    await ctx.send(embed=statusEmbed)


                    if turn % 4 == 0:

                        if player1Alive == False:
                            turn += 1

                        else:
                            move_text = "\n".join([f"({k}) **{v['name']}** - {v['desc']}" for k, v in player["moves"].items()])
                            await ctx.send(f"Choose a move:\n{move_text}")

                            msg = await self.bot.wait_for('message', check=check)
                            choice = msg.content.strip()

                            if choice.lower() == "quit":
                                await ctx.send("Stopping run!")
                                return

                            if choice in player['moves']:
                                move = player['moves'][choice]
                            else:
                                await ctx.send("Pick a proper attack dummy!")



                            if (player['moves'][choice]['target'] == "Enemy"):
                                await ctx.send(f"Choose a target (1 or 2)")


                                enemyChoiceLoop = True
                                while enemyChoiceLoop == True:

                                    msg2 = await self.bot.wait_for('message', check=check)
                                    enemyChoice = msg2.content.strip()

                                    if enemyChoice == "1":
                                        if enemy['HP'] > 0:
                                            target = enemy
                                            target2 = enemy2
                                            break
                                        else:
                                            await ctx.send("This enemy is already defeated silly!")

                                    elif enemyChoice == "2":
                                        if enemy2['HP'] > 0:
                                            target = enemy2
                                            target2 = enemy
                                            break
                                        else:
                                            await ctx.send("This enemy is already defeated silly!")

                                await move['action'](ctx, player, target, target2)


                            elif (player['moves'][choice]['target'] == "Self"):
                                await move['action'](ctx, player, target)


                            elif (player['moves'][choice]['target'] == "Team"):
                                await ctx.send("Which character do you want to perform this to?")
                                await ctx.send(f"- {player['name']}")
                                await ctx.send(f"- {player2['name']}")

                                msg3 = await self.bot.wait_for('message', check=check)
                                playerChoice = msg3.content.strip()


                                if playerChoice.lower() == player['name'].lower():
                                    await move['action'](ctx, player)
                                    break

                                elif playerChoice.lower() == player2['name'].lower():
                                    await move['action'](ctx, player2)
                                    break

                                else:
                                    await ctx.send("That isn't a valid team member silly!")

                            elif (player['moves'][choice]['target'] == "TeamFull"):
                                await move['action'](ctx, player, player2)


                            await asyncio.sleep(1)
                            turn += 1

                    elif turn % 4 == 1:

                        if player2Alive == False:
                            turn += 1

                        else:
                            move_text = "\n".join(
                                [f"({k}) **{v['name']}** - {v['desc']}" for k, v in player2["moves"].items()])
                            await ctx.send(f"Choose a move:\n{move_text}")

                            msg = await self.bot.wait_for('message', check=check)
                            choice = msg.content.strip()

                            if choice.lower() == "quit":
                                await ctx.send("Stopping run!")
                                return

                            if choice in player2['moves']:
                                move = player2['moves'][choice]
                            else:
                                await ctx.send("Pick a proper attack dummy!")


                            if (player2['moves'][choice]['target'] == "Enemy"):
                                await ctx.send(f"Choose a target (1 or 2)")


                                enemyChoiceLoop = True
                                while enemyChoiceLoop == True:

                                    msg2 = await self.bot.wait_for('message', check=check)
                                    enemyChoice = msg2.content.strip()

                                    if enemyChoice == "1":
                                        if enemy['HP'] > 0:
                                            target = enemy
                                            target2 = enemy2
                                            break
                                        else:
                                            await ctx.send("This enemy is already defeated silly!")

                                    elif enemyChoice == "2":
                                        if enemy2['HP'] > 0:
                                            target = enemy2
                                            target2 = enemy
                                            break
                                        else:
                                            await ctx.send("This enemy is already defeated silly!")

                                await move['action'](ctx, player2, target, target2)


                            elif (player2['moves'][choice]['target'] == "Self"):
                                await move['action'](ctx, player2)


                            elif (player2['moves'][choice]['target'] == "Team"):
                                await ctx.send("Which character do you want to perform this to?")
                                await ctx.send(f"- {player['name']}")
                                await ctx.send(f"- {player2['name']}")

                                msg3 = await self.bot.wait_for('message', check=check)
                                playerChoice = msg3.content.strip()

                                if playerChoice.lower() == player['name'].lower():
                                    await move['action'](ctx, player)

                                elif playerChoice.lower() == player2['name'].lower():
                                    await move['action'](ctx, player2)


                            await asyncio.sleep(1)
                            turn += 1






                    if enemy["HP"] <= 0 and enemy1Alive == True:
                        await ctx.send(f"You defeated {enemy['name']}!")
                        await asyncio.sleep(2)

                        enemy1Alive = False

                        if world == 1:
                            if room % 5 != 0:

                                coinsEmbed = discord.Embed(title="You gained 1 coin!", color=discord.Color.pink())
                                await ctx.send(embed=coinsEmbed)

                                self.changeCoins(ctx.author.id, 1)
                                await asyncio.sleep(1)

                            elif room % 5 == 0:

                                coinsEmbed = discord.Embed(title="You gained 5 coins!", color=discord.Color.pink())
                                await ctx.send(embed=coinsEmbed)

                                self.changeCoins(ctx.author.id, 5)
                                await asyncio.sleep(1)


                    if enemy2Exists and enemy2['HP'] <= 0 and enemy2Alive == True:
                        await ctx.send(f"You defeated {enemy2['name']}!")
                        await asyncio.sleep(2)

                        enemy2Alive = False

                        if world == 1:
                            if room % 5 != 0:

                                coinsEmbed = discord.Embed(title="You gained 1 coin!", color=discord.Color.pink())
                                await ctx.send(embed=coinsEmbed)

                                self.changeCoins(ctx.author.id, 1)
                                await asyncio.sleep(1)

                            elif room % 5 == 0:

                                coinsEmbed = discord.Embed(title="You gained 5 coins!", color=discord.Color.pink())
                                await ctx.send(embed=coinsEmbed)

                                self.changeCoins(ctx.author.id, 5)
                                await asyncio.sleep(1)

                    if enemy1Alive == False and enemy2Alive == False:
                        await ctx.send(f"Room {room} cleared!")
                        roomCleared = True
                        break






                    # ENEMY TURN
                    elif turn % 4 == 2:

                        if enemy1Alive == False:
                            turn += 1
                            continue

                        if enemy['FROZEN'] >= 1:
                            await ctx.send(f"{enemy['name']} can't attack!")
                            enemy['FROZEN'] -= 1
                            await asyncio.sleep(1)
                            turn += 1
                            continue

                        else:

                            activeEnemy = enemy
                            choice = random.randint(1, 2)

                            if choice == 1:
                                target = player
                            elif choice == 2:
                                target = player2

                            await asyncio.sleep(2)

                            if target['BLOCKS'] >= 1:
                                await ctx.send(f"{player['name']} blocks the attack!")
                                target['BLOCKS'] -= 1

                            else:
                                enemyEmbed = discord.Embed(title=f"{activeEnemy['name']}'s Turn!",
                                                           description=f"dealt {activeEnemy['ATK']} damage to {target['name']}!",
                                                           color=0x874545)

                                await ctx.send(embed=enemyEmbed)
                                target["HP"] -= activeEnemy["ATK"]

                            await asyncio.sleep(2)
                            turn += 1

                    elif turn % 4 == 3:

                        if not enemy2Exists or enemy2Alive == False:
                            turn += 1
                            continue

                        if enemy2['FROZEN'] >= 1:
                            await ctx.send(f"{enemy2['name']} can't attack!")
                            enemy2['FROZEN'] -= 1
                            await asyncio.sleep(1)
                            turn += 1
                            continue

                        else:

                            activeEnemy = enemy2
                            choice = random.randint(1, 2)

                            await asyncio.sleep(2)

                            if choice == 1:
                                target = player
                            elif choice == 2:
                                target = player2

                            if target['BLOCKS'] >= 1:
                                await ctx.send(f"{player['name']} blocks the attack!")
                                target['BLOCKS'] -= 1

                            else:
                                enemyEmbed = discord.Embed(title=f"{activeEnemy['name']}'s Turn!",
                                                           description=f"dealt {activeEnemy['ATK']} damage to {target['name']}!",
                                                           color=0x874545)

                                await ctx.send(embed=enemyEmbed)
                                target["HP"] -= activeEnemy["ATK"]

                            await asyncio.sleep(2)
                            turn += 1



                # RESULTS
                if player['HP'] <= 0 and player2['HP'] <= 0:
                    await ctx.send(f"Both {player['name']} and {player2['name']} have been defeated!")
                    alive = False
                    break

                if player["HP"] <= 0:
                    await ctx.send(f"{player['name']} was defeated!")

                if player2["HP"] <= 0:
                    await ctx.send(f"{player2['name']} was defeated!")


                if roomCleared == True:
                    room += 1
                    continue



        except Exception as e:
            print(e)


async def setup(bot):
    from main import rpgdb  # import your database object if needed
    await bot.add_cog(AnimeRPG(bot, rpgdb))