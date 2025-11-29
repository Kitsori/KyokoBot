import discord
from discord.ext import commands
import asyncio
import traceback
import random


from .rpggirls import rpgDictionary, randomGirl, rpgGirls

class AnimeRPG(commands.Cog):
    def __init__(self, bot, db):
        self.bot = bot
        self.db = db
        self.players = db["Players"]


    def rarityColor(self, rarity):
        if rarity == "Common":
            return 0x34cceb
        elif rarity == "Uncommon":
            return 0x34eb3a
        elif rarity == "Epic":
            return 0xf538ff


    def getPlayer(self, user_id: int):
        player = self.players.find_one({"_id": user_id})
        if not player:
            player = {"_id": user_id, "characters": [], "coins": 0}
            self.players.insert_one(player)
        return player

    def add_character(self, user_id: int, char_name: str):
        self.players.update_one({"_id": user_id}, {"$addToSet": {"characters": char_name.lower()}}, upsert=True)

    def add_coins(self, user_id: int, amount: int):
        self.players.update_one({"_id": user_id}, {"$inc": {"coins": amount}}, upsert=True)




    def summonChar(self):
        roll = random.randint(1, 100)

        if roll <= 60:
            rarity = "Common"
        elif roll <= 90:
            rarity = "Uncommon"
        else:
            rarity = "Epic"

        chars = [c for c in rpgGirls if c.rarity == rarity]
        return random.choice(chars)




    @commands.command()
    async def girl(self, ctx, *, input):
        name = input.lower()
        chars = rpgDictionary()
        if name not in chars:
            await ctx.send("Character not found.")
            return

        char = chars[name]
        color = self.rarityColor(char.rarity)

        embed = discord.Embed(title=char.name.title(), description=f"{char.rarity} - Level {char.level}", color=color)
        embed.add_field(name="HP", value=char.hp)
        embed.add_field(name="ATK", value=char.atk)
        embed.set_image(url=char.url)
        embed.set_footer(text=char.show)
        await ctx.send(embed=embed)


    @commands.command()
    async def summon(self, ctx):
        try:
            char = self.summonChar()
            self.add_character(ctx.author.id, char.name)
            await ctx.send(f"```diff\n+ You summoned {char.name}!\n```")
        except Exception:
            await ctx.send(f"```{traceback.format_exc()}```")


    @commands.command()
    async def rpgcol(self, ctx):
        try:
            player = self.getPlayer(ctx.author.id)

            if not player["characters"]:
                await ctx.send("You don't have any collection.")
                return

            chars = rpgDictionary()
            owned = [chars[g].name.title() for g in player["characters"] if g in chars]

            await ctx.send(f"**Your Girls:** {', '.join(owned)}")
        except Exception:
            await ctx.send(f"```{traceback.format_exc()}```")


    @commands.command()
    async def fight(self, ctx, *, input):
        try:
            player_name = input.lower()
            chars = rpgDictionary()
            if player_name not in chars:
                await ctx.send("Character not found.")
                return

            player = chars[player_name]
            enemy = randomGirl()

            color = self.rarityColor(player.rarity)
            colorEnemy = self.rarityColor(enemy.rarity)

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            turn = 0
            while player.hp > 0 and enemy.hp > 0:
                if turn % 2 == 0:
                    # Player's turn
                    move_text = "\n".join([f"{i} - {m.desc}" for i, m in player.moves.items()])
                    await ctx.send(f"What will you do {player.name.title()}?\n{move_text}\nB - Back")
                    move_response = await self.bot.wait_for("message", check=check)
                    move_input = move_response.content.strip()

                    if move_input.isdigit():
                        move_no = int(move_input)
                        if move_no in player.moves:
                            move = player.moves[move_no]
                            amount = move.apply(user=player, target=enemy if move.target=="enemy" else player)
                            action = "healed" if move.target=="self" else "dealt"
                            await ctx.send(f"{player.name} used {move.name}! {amount} HP {action}.")
                        else:
                            await ctx.send("Invalid move number.")
                            continue
                    else:
                        await ctx.send("Invalid input.")
                        continue

                else:
                    # Enemy's turn
                    move = random.choice(list(enemy.moves.values()))
                    amount = move.apply(user=enemy, target=player if move.target=="enemy" else enemy)
                    action = "healed" if move.target=="self" else "dealt"
                    await ctx.send(f"{enemy.name} used {move.name}! {amount} HP {action}.")

                # Status embed
                embed = discord.Embed(title="Battle", color=color if turn %2 == 0 else colorEnemy)
                embed.add_field(name=player.name, value=f"HP: {player.hp}\nATK: {player.atk}", inline=True)
                embed.add_field(name=enemy.name, value=f"HP: {enemy.hp}\nATK: {enemy.atk}", inline=True)
                embed.set_image(url=player.url if turn % 2 == 0 else enemy.url)
                embed.set_footer(text=f"{player.name if turn %2 ==0 else enemy.name}'s turn!")
                await ctx.send(embed=embed)

                turn += 1
                await asyncio.sleep(1)

            # End of fight
            winner = player.name if player.hp > 0 else enemy.name
            await ctx.send(f"{winner} wins!")

        except Exception:
            await ctx.send(f"```{traceback.format_exc()}```")

async def setup(bot):
    await bot.add_cog(AnimeRPG(bot))
