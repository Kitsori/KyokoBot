import os

from dotenv import load_dotenv
import discord
from discord.ext import  commands

import random
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='~', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game(name="with Kitsori"))




@bot.command()
async def helpme(ctx):
    helpEmbed = discord.Embed(
        title="Kyoko's Help Menu",
        description="A list of all my fun fun commands! :3 \n\u200b",
        color=discord.Color.blue()
    )

    helpEmbed.add_field(name="~helpme", value="Wow.. it's this menu!", inline=False)
    helpEmbed.add_field(name="~ping", value="Pong...!! :3", inline=False)
    helpEmbed.add_field(name="~add (x) (y)", value="Adds 2 numbers together... I'm so smart! :D", inline=False)
    helpEmbed.add_field(name="~subtract", value="Subtracts one number from another.. like magic!", inline=False)
    helpEmbed.add_field(name="~randomGirl", value="Generate a picture of a random anime girl!", inline=False)
    helpEmbed.add_field(name="~GirlRanking", value="Start a Anime Girl Blind Ranking!!! (WIP)", inline=False)

    await ctx.send(embed=helpEmbed)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f"Hai!! The sum of {num1} and {num2} is.... {result}! You're welcome!! :3")

@bot.command()
async def subtract(ctx, num1: int, num2: int):
    result = num1 - num2
    await ctx.send(f"Hai!! The difference of {num1} and {num2} is.... {result}! You're welcome!! :3")

@bot.command()
async def randomGirl(ctx):
    images = [f for f in os.listdir("Girls") if f.endswith((".jpg"))]

    chosen_image = random.choice(images)

    await ctx.send(file=discord.File(f"Girls/{chosen_image}"))

@bot.command()
async def GirlRanking(ctx):
    girls = [f for f in os.listdir("Girls") if f.endswith((".jpg"))] # Get the list of girls

    # Game Intro Message
    await ctx.send("You wanna rank some anime girls huh...? :3")
    await asyncio.sleep(3)
    await ctx.send("Well here ya go...! Here's your first girl!")

    # Main Game Loop
    rankCount = 0
    embedList = discord.Embed(title="Girl Ranking")

    ranks = [" Empty", " Empty", " Empty", " Empty", " Empty",]

    rankList = await ctx.send(embed=embedList)

    while rankCount < 5:

        # Send a picture of a girl and wait 2 seconds
        chosenGirl = random.choice(girls)
        await ctx.send(file=discord.File(f"Girls/{chosenGirl}"))
        await asyncio.sleep(2)

        # Ask player where they'd rank the girl
        await ctx.send("Where would you rank her from 1-5..? :3")
        def check(message):
            return message.author == ctx.author # Only accept responses from the command user

        # Wait 30 seconds for player to give an answer and then wait 2 seconds after
        response = await bot.wait_for('message', check=check, timeout=30)
        rank = int(response.content)
        if 1 <= rank <= 5:
            await ctx.send(f"You decided to rank her {rank}! :3")
            ranks[rank - 1] = "Girl"
            await asyncio.sleep(2)
        else:
            await ctx.send(f"That's not a correct ranking silly..!")

        for i, rank in enumerate(ranks):
            embedList.add_field(name=f"Rank {i+1}", value=rank, inline=False)

        await rankList.edit(embed=embedList)




        rankCount += 1








bot.run(TOKEN)