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
    async def run(self, ctx):

        # Setup Check
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Find the user running the command's RPG File
        user = self.findPlayer(ctx.author.id)

        # Create the list of the player's characters
        charList = ""
        await ctx.send("Choose your character: ")

        for char in user["characters"]:
            charList += f"- {char}\n"

        await ctx.send(charList)

        # Choose character
        msg = await self.bot.wait_for('message', check=check)
        playerChoice = msg.content


        world = user["world"]


        # Get that character's info
        try:
            for c in user["characters"]:
                char = c.lower()
                if playerChoice.lower() == char:
                    player = copy.deepcopy(rpgGirls[char])


            # Enemy counter
            room = 1
            alive = True


            while alive == True:

                # Generate enemies, dependant on world
                if world == 1 and room % 5 != 0:
                    enemy = copy.deepcopy(random.choice(list(world1Enemies.values())))
                elif world == 1 and room % 5 == 0:
                    enemy = copy.deepcopy(random.choice(list(world1Bosses.values())))

                # Setup turn counter
                turn = 0

                barValue = player['MAXHP'] / 10
                barValueE = enemy['HP'] / 10


                while player["HP"] > 0 and enemy["HP"] > 0:
                    if turn % 2 == 0:

                        barCountDouble = player["HP"] / barValue
                        barCountDoubleE = enemy["HP"] / barValueE
                        barCount = round(barCountDouble)
                        barCountE = round(barCountDoubleE)

                        bars = ""
                        barsE = ""
                        remBars = 10 - barCount
                        remBarsE = 10 - barCountE

                        for i in range(barCount):
                            bars += "█"

                        for i in range(remBars):
                            bars += "░"

                        for i in range(barCountE):
                            barsE += "█"

                        for i in range(remBarsE):
                            barsE += "░"

                        statusEmbed = discord.Embed(title=f"{player['name']}'s Turn!",
                                                    color=self.rarityColor(player["rarity"]))

                        statusEmbed.add_field(name=player['name'], value=f"{player['HP']} HP\n ║{bars}║")
                        statusEmbed.add_field(name=enemy['name'], value=f"{enemy['HP']} HP\n ║{barsE}║")
                        statusEmbed.set_image(url=player["image"])

                        await ctx.send(embed=statusEmbed)


                        move_text = "\n".join([f"({k}) **{v['name']}** - {v['desc']}" for k, v in player["moves"].items()])
                        await ctx.send(f"Choose a move:\n{move_text}")


                        msg = await self.bot.wait_for('message', check=check)
                        choice = msg.content.strip()

                        if choice in player['moves']:
                            move = player['moves'][choice]
                            await move['action'](ctx, player, enemy)
                        else:
                            await ctx.send("Invalid choice!")
                            continue

                        if enemy["HP"] <= 0:
                            break

                        await asyncio.sleep(1)
                        turn += 1

                        # ENEMY TURN
                    elif turn % 2 == 1:
                        if player['BLOCKS'] >= 1:
                            await ctx.send(f"{player['name']} blocks the attack!")
                            player['BLOCKS'] -= 1
                        else:
                            enemyEmbed = discord.Embed(title=f"{enemy['name']}'s Turn!",
                                                       description=f"dealt {enemy['ATK']} damage to {player['name']}!",
                                                       color=discord.Color.red())

                            await ctx.send(embed=enemyEmbed)
                            player["HP"] -= enemy["ATK"]

                        await asyncio.sleep(1)
                        turn += 1



                # RESULTS
                if player["HP"] <= 0:
                    await ctx.send(f"You were defeated by {enemy['name']}!")
                    alive = False

                elif enemy["HP"] <= 0:
                    await ctx.send(f"You defeated {enemy['name']}!")
                    await asyncio.sleep(2)

                    coinsEmbed = discord.Embed(title="You gained 1 coin!", color=discord.Color.pink())
                    await ctx.send(embed=coinsEmbed)

                    self.changeCoins(ctx.author.id, 1)
                    room += 1
                    await asyncio.sleep(1)



        except Exception as e:
            print(e)


async def setup(bot):
    from main import rpgdb  # import your database object if needed
    await bot.add_cog(AnimeRPG(bot, rpgdb))