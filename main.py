import os
from urllib import response

import discord
from discord.ext import commands

import logging
from dotenv import load_dotenv

import random
import asyncio

from girlimages import randomGirlGen

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='~', intents=intents)


# Variables

selfrole = "Member"





# BOT EVENTS

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game(name="with Kitsori"))



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return # Don't reply to own message

    # RESPOND TO NAME
    if "kyoko" in message.content.lower():
        await message.channel.send(f"Hai hai {message.author.mention}..! :3") # Send a message to current channel and mention author of message
        # await message.delete() - Can be used for filtering words

    await bot.process_commands(message) # Allows us to continue handling all other messages in the server by anyone

@bot.event
async def on_member_join(member):
    # await member.send(f"Hai hai {member.name}..! :3")   # Sends a dm to the member

    role = discord.utils.get(member.guild.roles, name=selfrole)

    if role:
        await member.add_roles(role)
    else:
        pass








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
async def ping(ctx): # Get context of message
    await ctx.send("Pong! :3") # Send back in the current channel wherever it was mentioned



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


#@bot.command()
#async def assign(ctx):
#    role = discord.utils.get(ctx.guild.roles, name=selfrole)

#    if role:
#        await ctx.author.add_roles(role)
#        await ctx.send(f"{ctx.author.mention} is now assigned to {selfrole}")
#    else:
#        await ctx.send("Role not found.")


#@bot.command()
#async def remove(ctx):
#    role = discord.utils.get(ctx.guild.roles, name=selfrole)
#
#    if role:
#        await ctx.author.remove_roles(role)
#        await ctx.send(f"{ctx.author.mention} is no longer assigned to {selfrole}")
#    else:
#        await ctx.send("Role not found.")

#@bot.command()
#@commands.has_role(selfrole) # Has to have the role to be able to use command
#async def secret(ctx):
#    await ctx.send("dlwafa")

#@secret.error
#sync def secret_error(ctx, error): # Define context and the type of error
#    if isinstance(error, commands.MissingRole):  # If error is a missing role error
#        await ctx.send("You have no permission to do that.")


#@bot.command()
#async def dm(ctx, *, msg): # If you want to get what is sent after the command you do this
#    await ctx.author.send(f"You said {msg}")

#@bot.command()
#async def reply(ctx):
#    await ctx.reply("Reply reply reply")

#@bot.command()
#async def poll(ctx, *, poll):
#    embed = discord.Embed(title="New Poll", description=poll)
#    poll_message = await ctx.send(embed=embed)
#    await poll_message.add_reaction("👍")
#    await poll_message.add_reaction("👎")







# RANDOM ANIME GIRL IMAGE GENERATOR

@bot.command()
async def randomgirl(ctx):
    await ctx.send("Hiya!! Here's your random girl...! :3")
    await asyncio.sleep(1)

    chosenGirls = randomGirlGen(1)

    name, url = chosenGirls[0] # Make a tuple of the name of image and its filepath

    embed = discord.Embed(title=name, color=discord.Color.blue())  # Set embed left side color
    embed.set_image(url=url)  # Set the image?

    await ctx.send(embed=embed)  # Send the embed of name and girl image
    #await ctx.send(content=f"**{name}**", file=file) # Send the name and image file








# ANIME GIRL BLIND RANKING GAME (WIP)

@bot.command()
async def girlranking(ctx):

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel  # Only accept responses from the command user.

    # Game Intro Message
    await ctx.send("You wanna rank some anime girls huh...? :3")
    await asyncio.sleep(1)

    await ctx.send("How many do you wanna rank..? (1-10)")

    numGirls = None
    girlNumBool = True

    async def numCountdown():
        nonlocal numGirls
        await asyncio.sleep(15)
        await ctx.send("Hai..? You there..? Whatever.. defaulting to 5 girls..")
        numGirls = 5
        numResponseTask.cancel()


    async def numResponse():
        nonlocal numGirls
        try:
            while True:
                numResponse = await bot.wait_for('message', check=check)
                response = numResponse.content.strip()
                if response.isdigit():
                    num = int(response)
                    if 1 <= num <= 10:
                        numGirls = num
                        await asyncio.sleep(0.5)
                        await ctx.send(f"Sure thing!! {numGirls} girls coming right up for ya..!")
                        await asyncio.sleep(2)
                        numTask.cancel()
                        break
                    else:
                        await ctx.send("That's not a valid number! :3")
        except asyncio.CancelledError:
            pass

    numTask = asyncio.create_task(numCountdown())
    numResponseTask = asyncio.create_task(numResponse())

    done, pending = await asyncio.wait([numTask, numResponseTask], return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()



    # Set up the number of ranks done so far and the embed
    rankCount = 0
    embedList = discord.Embed(title="Best Girl Ranking")

    # Create a band emped rank list
    ranks = ["-"] * numGirls

    await ctx.send("Well here ya go...! Here's your first girl!")



    chosenGirls = randomGirlGen(numGirls)  # Make a tuple of the name of image and its filepath



    # Main game loop while you have ranked less than 5 girls
    while rankCount < numGirls:

        # Set while loop for waiting for a reply to true
        loop = True

        name, show, url = chosenGirls[rankCount]

        embed = discord.Embed(title=name, description=show, color=discord.Color.blue()) # Set embed left side color
        embed.set_image(url=url) # Set the image?

        await ctx.send(embed=embed) # Send the embed of name and girl image
        await asyncio.sleep(2)



        # Loop for waiting for rank answer

        # Ask player where they'd rank the girl
        await ctx.send(f"Where would you rank her from 1-{numGirls}..? :3")

        await asyncio.sleep(0.5)

         # Initial countdown message
        countdown = await ctx.send("You have 30 seconds to decide..!")

          # Countdown in increments of 5 seconds
        async def rankCountdown():
            nonlocal loop
            for i in [30, 25, 20, 15, 10, 5, 0]:
                if i == 0:
                    await countdown.edit(content=f"Time Expired... :(")
                    loop = False
                else:
                    await countdown.edit(content=f"You have {i} seconds to decide..!")
                    await asyncio.sleep(6)

          # Make the countdown above a task so it can run at the same time as the code below
        countTask = asyncio.create_task(rankCountdown())

        # Loop for waiting for rank answer
        while loop == True:

            # Wait for 30 total seconds and then timeout if not given an answer.
            try:
                response = await bot.wait_for('message', check=check)
                content = response.content.strip()

                if loop == False:
                    await ctx.send(content=f"You didn't respond in time silly..! No more ranking for you..")
                    return
                elif content.isdigit():
                    rank = int(content)
                    if 1 <= rank <= numGirls:
                        if ranks[rank - 1] == "-":
                            ranks[rank - 1] = name
                            countTask.cancel()
                            loop = False
                            await ctx.send(f"You decided to rank her #{rank}!")
                            await asyncio.sleep(2)
                            if rankCount == numGirls - 1:
                                await ctx.send("Here's your FINAL Best Girl Ranking! Hope you didn't mess up too bad..! Heehee..!")
                                await asyncio.sleep(3)
                            else:
                                await asyncio.sleep(1)
                                await ctx.send("Here's your updated Best Girl Ranking! :3")
                        else:
                            await ctx.send(f"That rank is already full you dummy..!")
                    else:
                        await ctx.send(f"That's not a correct ranking silly..!")
                else:
                    pass

            except asyncio.TimeoutError:
                countTask.cancel()
                ##await countdown.edit(content=f"You didn't respond in time silly..! No more ranking for you..")

            # Reset embed list so it doesnt keep adding on
            embedList.clear_fields()


            # If a valid rank tell user and add to the rank list and exit the loop, otherwise repeat and say its not
            #if 1 <= rank <= 5:
            #    await ctx.send(f"You decided to rank her {rank}! :3")
            #    ranks[rank - 1] = name
            #    await asyncio.sleep(2)
            #    countTask.cancel()
            #    loop = False
            #else:
            #    await ctx.send(f"That's not a correct ranking silly..!")


        for i, rank in enumerate(ranks):
            embedList.add_field(name=f"#{i+1}", value=rank, inline=False)

        if rankCount == numGirls - 1:
            embedList.title = "FINAL Best Girl Ranking"

        await ctx.send(embed=embedList)
        await asyncio.sleep(3)

        rankCount += 1







bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)













