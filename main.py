import os
from urllib import response

import discord
from discord.ext import commands

import logging
from dotenv import load_dotenv

import random
import asyncio

from girlimages import randomGirlGen, girlDictionary

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






# HELP COMMANDS

@bot.command()
async def helpme(ctx):
    helpEmbed = discord.Embed(
        title="Kyoko's Help Menu",
        description="A list of all my fun fun commands! :3 \n\u200b",
        color=discord.Color.blue()
    )

    helpEmbed.add_field(name="~helpme", value="Wow.. it's this menu!", inline=False)
    helpEmbed.add_field(name="~ping", value="Pong...!! :3 \n\u200b", inline=False)
    helpEmbed.add_field(name="__Math__ (~mathhelp)", value="~add, ~sub, ~mult, ~div", inline=False)
    helpEmbed.add_field(name="__Random Girl__ (~rghelp)", value="~rg", inline=False)
    helpEmbed.add_field(name="__Girl Blind Ranking__ (~grhelp)", value="~gr", inline=False)
    await ctx.send(embed=helpEmbed)


@bot.command()
async def mathhelp(ctx):
    mathHelpEmbed = discord.Embed(
        title="Kyoko's Math Commands",
        description="Numbers are so fun..! :3 \n\u200b",
        color=discord.Color.blue()
    )

    mathHelpEmbed.add_field(name="~add (x) (y)", value="Adds two different numbers together.. like magic!", inline=False)
    mathHelpEmbed.add_field(name="~sub (x) (y)", value="Subtracts one number, y from x..!", inline=False)
    mathHelpEmbed.add_field(name="~mult (x) (y)", value="Multiples two numbers together.. it's growing so fast..!", inline=False)
    mathHelpEmbed.add_field(name="~div (x) (y)", value="Divides x into y equal parts... where is my share..? :(", inline=False)
    await ctx.send(embed=mathHelpEmbed)


@bot.command()
async def rghelp(ctx):
    rgHelpEmbed = discord.Embed(
        title="Kyoko's Random Girl Commands",
        description="What's better than random anime girls...! :3 \n\u200b",
        color=discord.Color.blue()
    )

    rgHelpEmbed.add_field(name="~rg", value="Generates a random girl.. what else could you need..!", inline=False)
    await ctx.send(embed=rgHelpEmbed)


@bot.command()
async def grhelp(ctx):
    grHelpEmbed = discord.Embed(
        title="Kyoko's Girl Blind Ranking Commands",
        description="What's better than random girls... objectively ranking them of course..! :3 \n\u200b",
        color=discord.Color.blue()
    )

    grHelpEmbed.add_field(name="~gr", value="Starts a girl blind ranking game..! Good luck!", inline=False)
    grHelpEmbed.add_field(name="~grl", value="Lookup a girl's name in my database..! :3", inline=False)
    await ctx.send(embed=grHelpEmbed)



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
async def sub(ctx, num1: int, num2: int):
    result = num1 - num2
    await ctx.send(f"Hai!! The difference of {num1} and {num2} is.... {result}! You're welcome!! :3")


@bot.command()
async def mult(ctx, num1: int, num2: int):
    result = num1 * num2
    await ctx.send(f"Hai!! The product of {num1} and {num2} is.... {result}! You're welcome!! :3")


@bot.command()
async def div(ctx, num1: int, num2: int):
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
async def rg(ctx):
    await ctx.send("Hiya!! Here's your random girl...! :3")
    await asyncio.sleep(1)

    chosenGirls = randomGirlGen(1)

    name, show, url = chosenGirls[0] # Make a tuple of the name of image and its filepath

    embed = discord.Embed(title=name, description=show, color=discord.Color.blue())  # Set embed left side color
    embed.set_image(url=url)  # Set the image?

    await ctx.send(embed=embed)  # Send the embed of name and girl image
    #await ctx.send(content=f"**{name}**", file=file) # Send the name and image file








# ANIME GIRL BLIND RANKING GAME (WIP)

@bot.command()
async def gr(ctx):

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel  # Only accept responses from the command user.

    # Game Intro Message
    await ctx.send("You wanna rank some anime girls huh...? :3")
    await asyncio.sleep(1)

    await ctx.send("How many do you wanna rank..? (1-10)")

    numGirls = None




    # Simultaneously start a countdown to answer while also waiting to accept an answer
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

    # Create task for each so they can be run simulatenously
    numTask = asyncio.create_task(numCountdown())
    numResponseTask = asyncio.create_task(numResponse())

    # Whichever task finishes first you call that one and then cancel the other one
    done, pending = await asyncio.wait([numTask, numResponseTask], return_when=asyncio.FIRST_COMPLETED)

    for task in pending:
        task.cancel()




    # Set up the number of ranks done so far variable and the embed for the ranking
    rankCount = 0
    embedList = discord.Embed(title="Best Girl Ranking")

    # Create an empty embed rank list which numGirls slots in it.
    ranks = ["-"] * numGirls




    await ctx.send("Well here ya go...! Here's your first girl!")




    chosenGirls = randomGirlGen(numGirls)  # Make a tuple list of numGirls number of girls from the girlimages list
                                           # Contains their name, show, image, etc each

    # Main game loop while you have ranked less than 5 girls
    while rankCount < numGirls:






        # Set while loop for waiting for a reply to true
        loop = True

        # Pull the different values for each girl into their name, show, etc.
        name, show, url = chosenGirls[rankCount]

        # Set the girl name as title, show as description, and side color as blue
        embed = discord.Embed(title=name, description=show, color=discord.Color.blue())
        embed.set_image(url=url) # Set the image to the url given

        await ctx.send(embed=embed) # Send the final embed
        await asyncio.sleep(2)


        # If only one girl left, the bot ranks her herself.
        if rankCount == numGirls - 1:
            loop = False

            await ctx.send("Oh..? It seems you only have one slot left..!")
            await asyncio.sleep(1)

            # Find where the blank slot is
            blank = "-"
            for index, value in enumerate(ranks):
                if blank == value:
                    finalSlotIndex = index # Set the finalSlotIndex to the blank slot index

            await ctx.send(f"Let me rank her for you then..! I hope you like her at #{finalSlotIndex + 1}!")
            await asyncio.sleep(2)
            embedList.clear_fields() # Clear embed

            await ctx.send("Here's your FINAL Best Girl Ranking! Hope you didn't mess up too bad..! Heehee..!")
            await asyncio.sleep(3)

            ranks[finalSlotIndex] = name # set the final slot to the name of the last girl

        else:
            # Ask player where they'd rank the girl
            await ctx.send(f"Where would you rank her from 1-{numGirls}..? :3")

            await asyncio.sleep(0.5)

             # Initial countdown message
            countdown = await ctx.send("You have 30 seconds to decide..!")

            # Countdown in increments of 5 seconds
            async def rankCountdown():
                nonlocal loop
                for i in [30, 25, 20, 15, 10, 5, 0]:
                    if i == 0:  # Once i is 0 it says time expired and ends the loop below
                        await countdown.edit(content=f"Time Expired... :(")
                        loop = False
                    else:   # Else keep counting down
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

                if loop == False: # Will set to false if time runs out above, if so end the loop/command
                    await ctx.send(content=f"You didn't respond in time silly..! No more ranking for you..")
                    return

                elif content.isdigit(): # If the response is a digit
                    rank = int(content) # Set the rank value to that digit

                    if 1 <= rank <= numGirls: # If the rank is in the valid range

                        if ranks[rank - 1] == "-": # If the rank is empty on the embed
                            ranks[rank - 1] = name # Then set the current rank to that rank
                            countTask.cancel() # Cancel the countdown
                            loop = False # End the loop
                            await ctx.send(f"You decided to rank her #{rank}!")
                            await asyncio.sleep(2)
                            await ctx.send("Here's your updated Best Girl Ranking! :3")

                        else: # Rank is already full
                            await ctx.send(f"That rank is already full you dummy..!")

                    else: # Rank is not in the valid range
                        await ctx.send(f"That's not a correct ranking silly..!")

                else: # If not a digit just ignore the message
                    pass

            except asyncio.TimeoutError:
                countTask.cancel()

            # Reset embed list so it doesnt keep adding on
            embedList.clear_fields()



        # Sets up the rank embed list?? I think??
        for i, rank in enumerate(ranks):
            embedList.add_field(name=f"#{i+1}", value=rank, inline=False)

        # If the rank count and number of girls are the same change the title to FINAL
        if rankCount == numGirls - 1:
            embedList.title = "FINAL Best Girl Ranking"

        # Send the embed after each iteration
        await ctx.send(embed=embedList)
        await asyncio.sleep(3)

        rankCount += 1
        # As long as rankCount is less than the number of girls repeat the process of the loop.




@bot.command()
async def grl(ctx, *, input):

    name = input.lower()
    if name in girlDictionary:
        girlInfo = girlDictionary[name]
        show = girlInfo["show"]
        url = girlInfo["url"]

        embed = discord.Embed(title=name, description=show, color=discord.Color.blue())
        embed.set_image(url=url)

        await ctx.send("I found this girl based off your search!!!")
        await ctx.send(embed=embed)
    else:
        await ctx.send("I couldn't find any girl with that name... :(")




    #girlList = testGirlGen(5)
    #await ctx.send("Made girl list")

    #notFound = True
    #number = 0

    #for i in girlList:
        #await ctx.send("Debug: Entered loop")
        #name, show, url = girlList[number]

        #nameLower = name.lower()
        #inputLower = input.lower()
        #await ctx.send(f"Debug: {number}")
        #await ctx.send(f"Debug Name: {nameLower}")
        #await ctx.send(f"Debug Input: {inputLower}")
        #if nameLower == inputLower:
            #await ctx.send("Debug: Entered if equal loop")
            #embed = discord.Embed(title=name, description=show, color=discord.Color.blue())
            #embed.set_image(url=url)


            #await ctx.send("I found this girl based off your search!!!")
            #await ctx.send(embed=embed)
            #break
        #else:
            #number += 1
            #ctx.send("Debug: Passing/Add Num")
            #pass

    #await ctx.send(f"Debug notFound: {notFound}")
    #if notFound == True:
        #await ctx.send("I found no girls matching your search.. :(")





bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)













