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


class AnimeRPG(commands.Cog):

    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.players = db["Players"]


    # Find a player's file, if not existing create one with defaults
    def findPlayer(self, user_id: int):
        player = self.players.find_one({"_id": user_id})
        if not player:
            player = {"_id": user_id, "world": 1, "characters": ["Aqua"], "coins": 0}
            self.players.insert_one(player)
        return player

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

    # Colors for rarities for embeds
    def rarityColor(self, rarity):

        if rarity == "Common":
            return 0x34cceb
        elif rarity == "Rare":
            return 0x34eb3a
        elif rarity == "Epic":
            return 0xf538ff


    @commands.command()
    async def coins(self, ctx):
        player = self.findPlayer(ctx.author.id)
        self.changeCoins(ctx.author.id, 10)
        await ctx.send("+10 Coins!")


    @commands.command()
    async def summon(self, ctx):
        player = self.findPlayer(ctx.author.id)

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


        chars = [c for c in rpgGirls.values() if c["rarity"] == rarity]
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

        self.addCharacter(ctx.author.id, character["name"])





    @commands.command()
    async def rrr(self, ctx):

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        user = self.findPlayer(ctx.author.id)

        charList = ""
        await ctx.send("Choose your characters: ")

        for char in user["characters"]:
            charList += f"- {char}\n"

        await ctx.send(charList)

        msg = await self.bot.wait_for('message', check=check)
        playerChoice = msg.content

        for c in user["characters"]:
            char = c.lower()
            if playerChoice.lower() == char:
                player = copy.deepcopy(rpgGirls[char])


        await ctx.send(player['moves']['1']['name'])



    @commands.command()
    async def run(self, ctx):

        # Setup Check
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Find the user running the command's RPG File
        user = self.findPlayer(ctx.author.id)

        # Create the list of the player's characters
        charList = ""
        await ctx.send("Choose your characters: ")

        for char in user["characters"]:
            charList += f"- {char}\n"

        await ctx.send(charList)

        # Choose character
        msg = await self.bot.wait_for('message', check=check)
        playerChoice = msg.content

        msg2 = await self.bot.wait_for('message', check=check)
        playerChoice2 = msg2.content


        world = user["world"]


        # Get that character's info
        try:
            for c in user["characters"]:
                char = c.lower()
                if playerChoice.lower() == char:
                    player = copy.deepcopy(rpgGirls[char])
                if playerChoice2.lower() == char:
                    player2 = copy.deepcopy(rpgGirls[char])


            # Room counter
            room = 1

            alive = True
            player1Alive = True
            player2Alive = True




            while alive == True:

                # Generate enemies, dependant on world
                if world == 1 and room % 5 != 0:
                    enemy = copy.deepcopy(random.choice(list(world1Enemies.values())))
                    enemy2 = copy.deepcopy(random.choice(list(world1Enemies.values())))
                elif world == 1 and room % 5 == 0:
                    enemy = copy.deepcopy(random.choice(list(world1Bosses.values())))

                # Setup turn counter
                turn = 0
                enemy1Alive = True
                enemy2Alive = True

                barValue = player['MAXHP'] / 10
                barValue2 = player2['MAXHP'] / 10

                barValueE = enemy['HP'] / 10
                barValueE2 = enemy2['HP'] / 10

                while (player['HP'] > 0 or player2['HP'] > 0) and (enemy['HP'] > 0 or enemy2['HP'] > 0):

                    barCountDouble = player["HP"] / barValue
                    barCountDouble2 = player2["HP"] / barValue2

                    barCountDoubleE = enemy["HP"] / barValueE
                    barCountDoubleE2 = enemy2["HP"] / barValueE2

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



                    statusEmbed = discord.Embed(title=f"{active}'s Turn!",
                                                color=self.rarityColor(rarity))

                    statusEmbed.add_field(name=player['name'], value=f"{player['HP']} HP\n ║{bars}║", inline=True)
                    statusEmbed.add_field(name=player2['name'], value=f"{player2['HP']} HP\n ║{bars2}║", inline=True)

                    statusEmbed.add_field(name="\u200b", value="─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ VS ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─ · ─", inline=False)

                    statusEmbed.add_field(name=enemy['name'], value=f"{enemy['HP']} HP\n ║{barsE}║", inline=True)
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

                            if choice in player['moves']:
                                move = player['moves'][choice]
                            else:
                                await ctx.send("Pick a proper attack dummy!")


                            if (player['moves'][choice]['target'] == "Enemy"):
                                await ctx.send(f"Choose a target (1 or 2)")

                                msg2 = await self.bot.wait_for('message', check=check)
                                enemyChoice = msg2.content.strip()

                                if enemyChoice == "1":
                                    if enemy['HP'] > 0:
                                        target = enemy
                                    else:
                                        await ctx.send("This enemy is already defeated silly!")

                                elif enemyChoice == "2":
                                    if enemy2['HP'] > 0:
                                        target = enemy2
                                    else:
                                        await ctx.send("This enemy is already defeated silly!")

                                await move['action'](ctx, player, target)


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

                                elif playerChoice.lower() == player2['name'].lower():
                                    await move['action'](ctx, player2)


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


                            if choice in player2['moves']:
                                move = player2['moves'][choice]
                            else:
                                await ctx.send("Pick a proper attack dummy!")


                            if (player2['moves'][choice]['target'] == "Enemy"):
                                await ctx.send(f"Choose a target (1 or 2)")

                                msg2 = await self.bot.wait_for('message', check=check)
                                enemyChoice = msg2.content.strip()

                                if enemyChoice == "1":
                                    if enemy['HP'] > 0:
                                        target = enemy
                                    else:
                                        await ctx.send("This enemy is already defeated silly!")

                                elif enemyChoice == "2":
                                    if enemy2['HP'] > 0:
                                        target = enemy2
                                    else:
                                        await ctx.send("This enemy is already defeated silly!")

                                await move['action'](ctx, player, target)


                            elif (player2['moves'][choice]['target'] == "Self"):
                                await move['action'](ctx, player, target)


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


                    # ENEMY TURN
                    elif turn % 4 == 2:

                        if enemy1Alive == False:
                            turn += 1

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
                                                           color=discord.Color.red())

                                await ctx.send(embed=enemyEmbed)
                                target["HP"] -= activeEnemy["ATK"]

                            await asyncio.sleep(2)
                            turn += 1

                    elif turn % 4 == 3:

                        if enemy2Alive == False:
                            turn += 1

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
                                                           color=discord.Color.red())

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

                if enemy["HP"] <= 0:
                    await ctx.send(f"You defeated {enemy['name']}!")
                    await asyncio.sleep(2)

                    enemy1Alive = False

                    coinsEmbed = discord.Embed(title="You gained 1 coin!", color=discord.Color.pink())
                    await ctx.send(embed=coinsEmbed)

                    self.changeCoins(ctx.author.id, 1)
                    await asyncio.sleep(1)

                if enemy2['HP'] <= 0:
                    await ctx.send(f"You defeated {enemy2['name']}!")
                    await asyncio.sleep(2)

                    enemy2Alive = False

                    coinsEmbed = discord.Embed(title="You gained 1 coin!", color=discord.Color.pink())
                    await ctx.send(embed=coinsEmbed)

                    self.changeCoins(ctx.author.id, 1)
                    await asyncio.sleep(1)

                if enemy1Alive == False and enemy2Alive == False:
                    curRoom = room + 1
                    await ctx.send(f"Room {curRoom} cleared!")
                    room += 1
                    break



        except Exception as e:
            print(e)


async def setup(bot):
    from main import rpgdb  # import your database object if needed
    await bot.add_cog(AnimeRPG(bot, rpgdb))