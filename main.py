import os

from dotenv import load_dotenv
import discord
from discord.ext import commands

import random
import asyncio

from girlimages import randomGirlGen

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
    helpEmbed.add_field(name="~subtract (x) (y)", value="Subtracts one number from another.. like magic!", inline=False)
    helpEmbed.add_field(name="~multiply (x) (y)", value="Multiplies two numbers together.. woahhhh :O", inline=False)
    helpEmbed.add_field(name="~divide (x) (y)", value="Divides one number from another number.. everyone gets a share..!", inline=False)
    helpEmbed.add_field(name="~randomgirl", value="Generate a picture of a random anime girl!", inline=False)
    helpEmbed.add_field(name="~girlranking", value="Start a Anime Girl Blind Ranking!!! (WIP)", inline=False)

    await ctx.send(embed=helpEmbed)



# PING PONG PING PONG

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! :3")



# MATH COMMANDS

@bot.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f"Hai!! The sum of {num1} and {num2} is.... {result}! You're welcome!! :3")


@bot.command()
async def subtract(ctx, num1: int, num2: int):
    result = num1 - num2
    await ctx.send(f"Hai!! The difference of {num1} and {num2} is.... {result}! You're welcome!! :3")


@bot.command()
async def multiply(ctx, num1: int, num2: int):
    result = num1 * num2
    await ctx.send(f"Hai!! The product of {num1} and {num2} is.... {result}! You're welcome!! :3")


@bot.command()
async def divide(ctx, num1: int, num2: int):
    result = num1 / num2
    await ctx.send(f"Hai!! The quotient of {num1} and {num2} is.... {result}! You're welcome!! :3")



# RANDOM ANIME GIRL IMAGE GENERATOR

@bot.command()
async def randomgirl(ctx):

    name, path = randomGirlGen() # Make a tuple of the name of image and its filepath

    filename = os.path.basename(path)

    file = discord.File(path, filename=filename) # Prepare the actual image


    embed = discord.Embed(title=name, color=discord.Color.blue())
    embed.set_image(url=f"attachment://{filename}")


    await ctx.send(embed=embed, file=file)
    #await ctx.send(content=f"**{name}**", file=file) # Send the name and image file




# OLD RANDOM ANIME GIRL IMAGE GENERATOR

# @bot.command()
# async def randomGirl(ctx):
#    images = [f for f in os.listdir("Girls") if f.endswith((".jpg"))]
#
#    chosen_image = random.choice(images)
#
#    await ctx.send(file=discord.File(f"Girls/{chosen_image}"))




# ANIME GIRL BLIND RANKING GAME (WIP)

@bot.command()
async def girlranking(ctx):
    #girls = [f for f in os.listdir("Girls") if f.endswith((".jpg"))] # Get the list of girls

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

        loop = True

        name, path = randomGirlGen()  # Make a tuple of the name of image and its filepath

        filename = os.path.basename(path)

        file = discord.File(path, filename=filename)  # Prepare the actual image

        embed = discord.Embed(title=name, color=discord.Color.blue())
        embed.set_image(url=f"attachment://{filename}")

        await ctx.send(embed=embed, file=file) # Send the embed of name and girl image
        await asyncio.sleep(2)

        # Send a picture of a girl and wait 2 seconds
        #chosenGirl = random.choice(girls)
        #await ctx.send(file=discord.File(f"Girls/{chosenGirl}"))

        # Ask player where they'd rank the girl
        await ctx.send("Where would you rank her from 1-5..? :3")
        def check(message):
            return message.author == ctx.author # Only accept responses from the command user

        # Wait 30 seconds for player to give an answer and then wait 2 seconds after
        response = await bot.wait_for('message', check=check, timeout=30)
        rank = int(response.content)

        embedList.clear_fields()
        while loop == True:
            if 1 <= rank <= 5:
                await ctx.send(f"You decided to rank her {rank}! :3")
                ranks[rank - 1] = name
                await asyncio.sleep(2)
                loop == False
            else:
                await ctx.send(f"That's not a correct ranking silly..!")

        for i, rank in enumerate(ranks):
            embedList.add_field(name=f"Rank {i+1}", value=rank, inline=False)

        await ctx.send(embed=embedList)
        await asyncio.sleep(2)

        rankCount += 1




# BOT EVENTS

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # RESPOND TO NAME
    if "kyoko" in message.content.lower():
        await message.channel.send(f"Hai hai {message.author.mention}..! :3")

    await bot.process_commands(message)









bot.run(TOKEN)