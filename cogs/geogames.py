import discord
from discord.ext import commands
import asyncio
import random

from cogs.geodata import countries

class geogames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # wins = 0
    # total = 0

    @commands.command()
    async def geocap(self, ctx, flag=None):

        geoguessr = False

        if flag == "gg":
            geoguessr = True

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel


        if geoguessr == True:
            key = random.choice(list(k for k, v in countries.items() if v.get("geoguessr") == "y"))
            geototal = sum(1 for v in countries.values() if v.get("geoguessr") == "y")
            await ctx.send(f"Selecting from the {geototal} possible countries in geoguessr...")
            await asyncio.sleep(1)

        else:
            key = random.choice(list(countries.keys()))
            total = sum(1 for v in countries.values())
            await ctx.send(f"Selecting from the {total} possible countries in the world...")
            await asyncio.sleep(1)

        country = countries[key]

        await ctx.send(f"Your random country: {country['name']}")

        await ctx.send("What is the capital of this country?")
        response = await self.bot.wait_for('message', check=check)
        playerAnswer = response.content.title()
        answer = country["capital"].title()

        if (playerAnswer == answer):
            await ctx.send("That's correct..! :3")
            # self.wins += 1
            # self.total += 1
        else:
            await ctx.send("Too bad that's not correct..! :(")
            # self.total += 1

        await ctx.send(f"Your answer was: {playerAnswer}")
        await ctx.send(f"The correct answer was: {answer}")

        await asyncio.sleep(1)

        # losses = self.total - self.wins

        # await ctx.send(f"Your win/loss ratio is: {self.wins} - {losses}")


async def setup(bot):
    await bot.add_cog(geogames(bot))
