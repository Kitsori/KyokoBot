import os
from pymongo import MongoClient

import discord
from discord.ext import commands

import logging
from dotenv import load_dotenv

import random
import asyncio

import json

from cogs.animerpg import AnimeRPG
from cogs.jltg import jltg

from girlimages import randomGirlGen, testGirlGen, girlDictionary, showDictionary
from levels import XP_LEVELS, xp_to_level, level_up

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MONGO = os.getenv('MONGO_URI')





handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='~', intents=intents, help_command=None)



client = MongoClient(MONGO)

db = client["KyokoBot"]
rpgdb = client["KyokoRPG"]
xpdb = client["KyokoXP"]

gr5Stats = db["gr_5_stats"]
gr10Stats = db["gr_10_stats"]

grTotalPlays = db["grTotalPlays"]

FiveInitialRank = db["5InitialRank"]
TenInitialRank = db["10InitialRank"]

girlAvgRanks = db["GirlAverageRanks5"]
girlAvgRanksTen = db["GirlAverageRanks10"]


xpCol = db["XP"]

updateChannelsList = db["update_channels"]




# Database Methods

def roundFiveCount(user_id, command):
    gr5Stats.update_one({"user_id": user_id, "command": command},
                     {"$inc": {"count": 1}},
                             upsert=True
    )

def roundTenCount(user_id, command):
    gr10Stats.update_one({"user_id": user_id, "command": command},
                     {"$inc": {"count": 1}},
                             upsert=True
    )


def grTotalPlay(user_id, command):
    grTotalPlays.update_one({"user_id": user_id, "command": command},
                     {"$inc": {"count": 1}},
                             upsert=True
    )


async def roundFiveInitialRank(user_id, rank):
    await asyncio.to_thread(FiveInitialRank.update_one, {"user_id": user_id}, {"$push": {"first_ranks": rank}},
                            upsert=True
                            )

async def roundTenInitialRank(user_id, rank):
    await asyncio.to_thread(TenInitialRank.update_one, {"user_id": user_id}, {"$push": {"first_ranks": rank}},
                            upsert=True
                            )


async def avgGirlRank(girlName, user_id, rank):
    fieldName = f"player_ranks.{user_id}"

    await asyncio.to_thread(girlAvgRanks.update_one,{"girl_name": girlName},{"$push": {fieldName: rank}},
        upsert=True
    )

async def avgGirlRankTen(girlName, user_id, rank):
    fieldName = f"player_ranks.{user_id}"

    await asyncio.to_thread(girlAvgRanksTen.update_one,{"girl_name": girlName},{"$push": {fieldName: rank}},
        upsert=True
    )

async def userXP(user_id, userxp, level=None):

    update = {"$inc": {"xp": userxp}}


    exists = await asyncio.to_thread(xpCol.find_one, {"user_id": user_id})

    if not exists:
        update["$set"] = {"level": 1}

    if level is not None:
        update.setdefault("$set", {})["level"] = level


    await asyncio.to_thread(xpCol.update_one,{"user_id": user_id}, update, upsert=True)


def add_server(guild_id: int, channel_id: int):
    updateChannelsList.update_one(
        {"guild_id": str(guild_id)},
        {"$set": {"channel_id": str(channel_id)}},
        upsert=True
    )





class PageView(discord.ui.View):
    def __init__(self, embeds, timeout=180):
        super().__init__(timeout=timeout)
        self.embeds = embeds
        self.current_page = 0

    @discord.ui.button(label="< < <", style=discord.ButtonStyle.blurple)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    @discord.ui.button(label="> > >", style=discord.ButtonStyle.blurple)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.current_page < len(self.embeds) - 1:
            self.current_page += 1
            # Respond immediately
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True






@bot.listen("on_jltg_win")
async def on_jltg_win(user):
    await userXP(user.id, 20)












# Variables

selfrole = "Member"
#TEST_GUILD_ID = 734685955063152650



# BOT EVENTS
#@bot.check
#async def testServer(ctx):
#    return ctx.guild and ctx.guild.id == TEST_GUILD_ID




@bot.event
async def on_ready():



    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game(name="Playing with Kitsori"))




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
async def updates(ctx, channel: discord.TextChannel):
    try:
        add_server(ctx.guild.id, channel.id)
        await ctx.send("Updates channel set to this channel.")
    except Exception as e:
        print(e)



@bot.command()
async def sendupdates(ctx):
    """Send an update message to all registered update channels in MongoDB."""
    if ctx.author.id != 333414505750986753:
        await ctx.send("Only Kyoko's favorite is allowed to run this command...!")
        return

    servers = updateChannelsList.find({})  # MongoDB query for all guild → channel entries

    for server in servers:
        guild_id = int(server["guild_id"])
        channel_id = int(server["channel_id"])

        try:
            channel = bot.get_channel(channel_id)
            if not channel:
                channel = await bot.fetch_channel(channel_id)

            await channel.send("# Update 1/15/2026\n"
                                    "- Added ~update, a command that allows users to set a specific channel to receive these updates!\n"
                                    "  - These updates will post across all channels anytime updates are made.\n"
                                    "- The Beta version of Train Tag is now live, play using ~tag\n"
                                    "  - A mini-game inspired by Tag from Jet Lag the Game!\n"
                                    "  - Take trains, collect coins, and try to reach the end before being tagged!\n"
                                    "- Added some new commands to the help menu for these corresponding updates.")

        except Exception as e:
            print(f"Failed to send update to guild {guild_id}: {e}")

    await ctx.send("Updates sent to all registered channels!")





@bot.command()
async def sut(ctx):
    if (ctx.author.id == 333414505750986753):
        try:
            channel = await bot.fetch_channel(1461414479911718986)
            await channel.send("# Update 1/15/2026\n"
                                    "- Added ~update, a command that allows users to set a specific channel to receive these updates!\n"
                                    "  - These updates will post across all channels anytime updates are made.\n"
                                    "- The Beta version of Train Tag is now live, play using ~tag\n"
                                    "  - A mini-game inspired by Tag from Jet Lag the Game!\n"
                                    "  - Take trains, collect coins, and try to reach the end before being tagged!\n"
                                    "- Added some new commands to the help menu for these corresponding updates.")
        except Exception as e:
            print(e)
    else:
        await ctx.send("Only Kyoko's favorite is allowed to run this command...!")





# HELP COMMANDS

@bot.command(name="help")
async def helpme(ctx):
    helpEmbed = discord.Embed(
        title="Kyoko's Help Menu",
        description="A list of all my fun fun commands! :3 \n\u200b",
        color=discord.Color.blue()
    )

    helpEmbed.add_field(name="~help", value="Wow.. it's this menu!", inline=False)
    helpEmbed.add_field(name="~ping", value="Pong...!! :3 \n\u200b", inline=False)
    helpEmbed.add_field(name="__Math__ (~mathhelp)", value="~add, ~sub, ~mult, ~div", inline=False)
    helpEmbed.add_field(name="__Random Girl__ (~rghelp)", value="~rg", inline=False)
    helpEmbed.add_field(name="__Girl Blind Ranking__ (~grhelp)", value="~gr, ~gl, ~gsl, ~grs, ~gs, ~ggs, ~gt, ~gtg, ~gtt, ~gttg", inline=False)
    helpEmbed.add_field(name="__Train Tag__ (~taghelp)", value="~tag, ~taginfo", inline=False)
    helpEmbed.add_field(name="__Admin Commands__ (~adminhelp)", value="~updates", inline=False)
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

    grHelpEmbed.add_field(name="~gr", value="Starts a Girl Blind Ranking game..! Good luck!\n\u200b", inline=False)
    grHelpEmbed.add_field(name="__Lookup Commands__", value="", inline=False)
    grHelpEmbed.add_field(name="~gl (name)", value="Lookup a girl's name in my list..!", inline=False)
    grHelpEmbed.add_field(name="~gsl (show)", value="Lookup all available girls from a specific series!!\n\u200b", inline=False)
    grHelpEmbed.add_field(name="__Stats Commands__", value="", inline=False)
    grHelpEmbed.add_field(name="~grs", value="View your general Girl Blind Ranking stats!!", inline=False)
    grHelpEmbed.add_field(name="~gs", value="View your stats for a specific girl..!!", inline=False)
    grHelpEmbed.add_field(name="~gs", value="View global stats for a specific girl!!", inline=False)
    grHelpEmbed.add_field(name="~gt", value="View your top ranked girls for rounds of 5..!", inline=False)
    grHelpEmbed.add_field(name="~gtg", value="View the top ranked girls globally for rounds of 5..!", inline=False)
    grHelpEmbed.add_field(name="~gtt", value="View your top ranked girls for rounds of 10..!", inline=False)
    grHelpEmbed.add_field(name="~gttg", value="View the top ranked girls globally for rounds of 10..!", inline=False)
    await ctx.send(embed=grHelpEmbed)


@bot.command()
async def taghelp(ctx):
    taghelpEmbed = discord.Embed(
        title="Kyoko's Train Tag Commands",
        description="They'll never catch me on this train..! :3 \n\u200b",
        color=discord.Color.blue()
    )

    taghelpEmbed.add_field(name="~tag", value="Starts a round of Train Tag!", inline=False)
    taghelpEmbed.add_field(name="~taginfo", value="An in-depth breakdown of how Train Tag works.", inline=False)
    await ctx.send(embed=taghelpEmbed)


@bot.command()
async def taginfo(ctx):
    taginfoEmbed = discord.Embed(
        title="Train Tag Guide",
        description="Train Tag is a silly little minigame inspired by Tag from Jet Lag The Game! \n\u200b",
        color=discord.Color.blue()
    )

    taginfoEmbed.add_field(name="Overview", value="This game involves taking various trains to try to reach "
                                                 "an end location before the end of the day OR before the taggers "
                                                 "catch up with you.\n"
                                                 "\n"
                                                 "You travel on trains with coins, a game-specific currency, for a "
                                                 "cost of 1 coin = 1 minute on trains. In order to earn more coins, you "
                                                 "must pull cards, which could consist of challenges, curses, or blessings.\n"
                                                 "\n"
                                                 "Each 'station' has a list of trains, varying in distance and travel time, try "
                                                 "to take the trains that are most optimal! The game will update you on your "
                                                 "total distance traveled and remaining distance so you can see how far you "
                                                 "have yet to go.\n"
                                                 "\n"
                                                 "In addition, there are taggers chasing you! (You do not know their dsitance, "
                                                 "so if you stall in an area for too long trying to farm coins, you might get "
                                                 "tagged and lose before you even get the chance to get to your end location!", inline=False)
    taginfoEmbed.add_field(name="Good Luck!", value="This game is still a WIP, so expect bugs or some 'unfinished' content!", inline=False)
    await ctx.send(embed=taginfoEmbed)



@bot.command()
async def adminhelp(ctx):
    adminEmbed = discord.Embed(
        title="Kyoko's Admin Commands",
        description="Don't be too much of a Discord mod.... :3 \n\u200b",
        color=discord.Color.blue()
    )

    adminEmbed.add_field(name="~updates (channel ID)", value="Sets the designated channel as a Kyoko Live Updates Feed", inline=False)
    await ctx.send(embed=adminEmbed)





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




# ────────────────────────────────────────────────────────────────────────────────────────────────
# KYOKO XP / LEVELING
# ────────────────────────────────────────────────────────────────────────────────────────────────

@bot.command()
async def xp(ctx, user_id: str = None):

    if ctx.message.mentions:
        user = ctx.message.mentions[0]
        userID = int(user.id)
    elif user_id:
        try:
            userID = int(user_id)
            user = await bot.fetch_user(userID)
        except:
            user = None
    else:
        user = ctx.author
        userID = ctx.author.id



    try:
        xpFile = xpCol.find_one({"user_id": userID})

        startingXP = xpFile['xp']
        await ctx.send(f"Current Level: {xpFile['level']}")



        levelxp = xp_to_level(xpFile["level"])

        leveledup, xpFileNew = level_up(xpFile)


        if leveledup == True:

            await ctx.send("You leveled up!")

            await userXP(ctx.author.id, -levelxp, xpFileNew['level'])
        else:
            await userXP(ctx.author.id, 0, xpFileNew['level'])

        newlevelxp = xp_to_level(xpFileNew['level'])

        await ctx.send(f"Current XP: {xpFileNew['xp']}/{newlevelxp}")






        await ctx.send("You have no xp")
    except Exception as e:
        print(e)







# ────────────────────────────────────────────────────────────────────────────────────────────────
# RANDOM ANIME GIRL IMAGE GENERATOR
# ────────────────────────────────────────────────────────────────────────────────────────────────

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







# ────────────────────────────────────────────────────────────────────────────────────────────────
# ANIME GIRL BLIND RANKING GAME
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gr(ctx):

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel  # Only accept responses from the command user.

    # Game Intro Message
    await ctx.send("You wanna rank some anime girls huh...? :3")
    await asyncio.sleep(1)

    await ctx.send("How many do you wanna rank..? (1-10)")

    numGirls = None
    user_id = ctx.author.id




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

            if numGirls == 5:
                asyncio.create_task(avgGirlRank(name, user_id, finalSlotIndex + 1))

            if numGirls == 10:
                asyncio.create_task(avgGirlRankTen(name, user_id, finalSlotIndex + 1))

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

                        if numGirls == 5 and rankCount == 0:
                            asyncio.create_task(roundFiveInitialRank(ctx.author.id, rank))

                        if numGirls == 10 and rankCount == 0:
                            asyncio.create_task(roundTenInitialRank(ctx.author.id, rank))

                        if ranks[rank - 1] == "-": # If the rank is empty on the embed
                            ranks[rank - 1] = name # Then set the current rank to that rank
                            countTask.cancel() # Cancel the countdown
                            loop = False # End the loop
                            await ctx.send(f"You decided to rank her #{rank}!")
                            await asyncio.sleep(2)
                            await ctx.send("Here's your updated Best Girl Ranking! :3")

                            if numGirls == 5:
                                asyncio.create_task(avgGirlRank(name, user_id, rank))

                            if numGirls == 10:
                                asyncio.create_task(avgGirlRankTen(name, user_id, rank))

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

            if rankCount == 4:
                roundFiveCount(ctx.author.id, "gr")
            elif rankCount == 9:
                roundTenCount(ctx.author.id, "gr")

            if rankCount >= 4:
                grTotalPlay(ctx.author.id, "gr")
                await userXP(ctx.author.id, 1)


        # Send the embed after each iteration
        await ctx.send(embed=embedList)

        if rankCount == numGirls - 1:
            xpembed = discord.Embed(description="You gained +1 XP!!", color=discord.Color.green())
            await ctx.send(embed=xpembed)

        await asyncio.sleep(3)

        rankCount += 1
        # As long as rankCount is less than the number of girls repeat the process of the loop.






# ────────────────────────────────────────────────────────────────────────────────────────────────
# Girl Lookup Command
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gl(ctx, *, input):

    nameInput = input.lower()
    list = []
    found = False

    if nameInput in girlDictionary:
        list.append(girlDictionary[nameInput])
        girlInfo = girlDictionary[nameInput]
        name = girlInfo["name"]
        show = girlInfo["show"]
        url = girlInfo["url"]

        embed = discord.Embed(title=name, description=show, color=discord.Color.blue())
        embed.set_image(url=url)

        await ctx.send("I found this girl based off your search!!!")
        await ctx.send(embed=embed)
        found = True

    else:
        foundOne = False
        for key in girlDictionary:
            names = key.split()
            if nameInput in names:
                girlInfo = girlDictionary[key]

                name = girlInfo["name"]
                show = girlInfo["show"]

                await ctx.send(f"{name} - {show}")
                found = True
                foundOne = True

        if foundOne == True:
            await ctx.send("I found these girls based off your search!!!")



    if found == False:
        await ctx.send("I couldn't find any girl with that name... :(")





# ────────────────────────────────────────────────────────────────────────────────────────────────
# Girl Show Lookup Command
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gsl(ctx, *, input):

    showInput = input.lower()
    showFound = False


    if showInput in showDictionary:
        entry = showDictionary[showInput]
        showName = entry[0]["show"]
        count = 0

        nameList = []
        for girl in showDictionary[showInput]:
            name = girl["name"]
            nameList.append(f" - {name}")
            count += 1


            showFound = True

        await ctx.send(f"I found {count} girls from {showName}!! :3")

        nameList.sort()

        names = "\n".join(nameList)

        await ctx.send(names)

    if showFound == False:
        await ctx.send("I couldn't find any shows with that title... :(")


    #if showInput in showDictionary:
    #    showList.append(girlDictionary[showInput])
    #    showInfo = girlDictionary[showInput]


    #    await ctx.send("Debug: Found show")

    #    await ctx.send(f"Found {showInput}.")





# ────────────────────────────────────────────────────────────────────────────────────────────────
# General Girl Ranking Stats
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def grs(ctx, user_id: str = None):

    if ctx.message.mentions:
        user = ctx.message.mentions[0]
        userid = user.id
    elif user_id:
        try:
            userid = int(user_id)
            user = await bot.fetch_user(userid)
        except:
            user = None
            userid = int(user_id)
    else:
        user = ctx.author
        userid = ctx.author.id

    command = "gr"

    # Run MongoDB lookups in a separate thread to avoid blocking the event loop
    def fetch_data():
        gr5file = gr5Stats.find_one({"user_id": userid, "command": command})
        gr10file = gr10Stats.find_one({"user_id": userid, "command": command})
        grTotalFile = grTotalPlays.find_one({"user_id": userid, "command": command})
        FiveRankFile = FiveInitialRank.find_one({"user_id": userid})
        TenRankFile = TenInitialRank.find_one({"user_id": userid})
        return gr5file, gr10file, grTotalFile, FiveRankFile, TenRankFile

    gr5file, gr10file, grTotalFile, FiveRankFile, TenRankFile = await asyncio.to_thread(fetch_data)

    fiveRankAvg = "-"
    tenRankAvg = "-"

    if FiveRankFile and "first_ranks" in FiveRankFile and FiveRankFile["first_ranks"]:
        fiveRankAvg = round(sum(FiveRankFile["first_ranks"]) / len(FiveRankFile["first_ranks"]), 2) if FiveRankFile else "-"

    if TenRankFile and "first_ranks" in TenRankFile and TenRankFile["first_ranks"]:
        tenRankAvg = round(sum(TenRankFile["first_ranks"]) / len(TenRankFile["first_ranks"]), 2) if TenRankFile else "-"

    fiveCount = gr5file.get("count", 0) if gr5file else 0
    tenCount = gr10file.get("count", 0) if gr10file else 0
    totalCount = grTotalFile.get("count", 0) if grTotalFile else 0


    if fiveCount + tenCount > 0:
        if user and user.id == ctx.author.id:
            title = f"{ctx.author.display_name}'s Girl Ranking Stats"
        elif user:
            title = f"{user.display_name}'s Girl Ranking Stats"
        else:
            return

        grsembed = discord.Embed(
            title=title,
            description=" \n\u200b",
            color=discord.Color.blue()
        )

        grsembed.add_field(name="__Total Times Played (5+ Girls)__", value=f"{totalCount}\n\u200b", inline=False)
        grsembed.add_field(name="__Times Played (5 Girls)__", value=f"{fiveCount}", inline=False)
        grsembed.add_field(name="__Average First Rank (5 Girls)__", value=f"{fiveRankAvg}\n\u200b", inline=False)
        grsembed.add_field(name="__Times Played (10 Girls)__", value=f"{tenCount}", inline=False)
        grsembed.add_field(name="__Average First Rank (10 Girls)__", value=f"{tenRankAvg}", inline=False)

        await ctx.send(embed=grsembed)
    else:
        await ctx.send("Play a full round of 5 girls and 10 girls to view stats!! :3")





# ────────────────────────────────────────────────────────────────────────────────────────────────
# Self Stats for a Specific Girl
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gs(ctx, *, input):

    parts = input.split()

    lastPart = parts[-1]

    if ctx.message.mentions:
        user = ctx.message.mentions[0]
        userID = str(user.id)
        girlName = " ".join(parts[:-1])
    elif lastPart.isdigit():
        userID = lastPart
        girlName = " ".join(parts[:-1])
        try:
            user = await bot.fetch_user(int(userID))
        except:
            user = None
    else:
        user = ctx.author
        userID = str(ctx.author.id)
        girlName = input



    girl = await asyncio.to_thread(girlAvgRanks.find_one, {"girl_name": girlName.title()})
    girlTen = await asyncio.to_thread(girlAvgRanksTen.find_one, {"girl_name": girlName.title()})

    if (not girl or "player_ranks" not in girl) and (not girlTen or "player_ranks" not in girlTen):
        await ctx.send(f"No rankings found for {girlName.title()}!")
        return None

    userRanks = girl["player_ranks"].get(userID) if girl else []
    userRanksTen = girlTen["player_ranks"].get(userID) if girlTen else []

    if not userRanks and not userRanksTen:
        if user and user.id == ctx.author.id:
            await ctx.send(f"You haven't ranked {girlName.title()}!! Get to ranking more you silly..! :3")
        elif user:
            await ctx.send(f"{user.display_name} hasn't ranked this girl yet..!")
        else:
            await ctx.send("No rankings found.")
        return

    avg = round(sum(userRanks) / len(userRanks), 2) if userRanks else "-"
    avgTen = round(sum(userRanksTen) / len(userRanksTen), 2) if userRanksTen else "-"



    nameInput = girlName.lower()

    if nameInput in girlDictionary:
        girlInfo = girlDictionary[nameInput]
        name = girlInfo["name"]
        url = girlInfo["url"]

        embed = discord.Embed(title=f"{girlName.title()} Stats", description=f"for {user.display_name}\n\u200b",
                              color=discord.Color.blue())

        embed.set_image(url=url)

        embed.add_field(name="__Total Times Rolled (5+ Girls)__", value=f"{len(userRanks + userRanksTen)}\n\u200b", inline=False)
        embed.add_field(name="__Times Rolled (5 Girls)__", value=len(userRanks), inline=False)
        embed.add_field(name="__Average Rank (5 Girls)__", value=f"{avg}\n\u200b", inline=False)
        embed.add_field(name="__Times Rolled (10 Girls)__", value=len(userRanksTen), inline=False)
        embed.add_field(name="__Average Rank (10 Girls)__", value=avgTen, inline=False)

        await ctx.send(embed=embed)


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Global Stats for a Specific Girl
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def ggs(ctx, *, input):
    girlName = input


    girl = await asyncio.to_thread(girlAvgRanks.find_one, {"girl_name": girlName.title()})
    girlTen = await asyncio.to_thread(girlAvgRanksTen.find_one, {"girl_name": girlName.title()})


    if (not girl or "player_ranks" not in girl) and (not girlTen or "player_ranks" not in girlTen):
        await ctx.send(f"No one has ranked {girlName.title()} yet..!! :(")
        return None

    userAverages = []
    userAveragesTen = []
    totalCount = 0
    totalCountTen = 0

    if girl:
        playerList = girl.get("player_ranks", [])

        for rankList in playerList.values():
            if rankList:
                userAverages.append(sum(rankList) / len(rankList))
                totalCount += len(rankList)

        avgFive = round(sum(userAverages) / len(userAverages), 2)
    else:
        totalCount = 0
        avgFive = 0

    if girlTen:
        playerListTen = girlTen.get("player_ranks", [])

        for rankList in playerListTen.values():
            if rankList:
                userAveragesTen.append(sum(rankList) / len(rankList))
                totalCountTen += len(rankList)

        avgTen = round(sum(userAveragesTen) / len(userAveragesTen), 2)
    else:
        totalCountTen = 0
        avgTen = 0



    nameInput = girlName.lower()


    if nameInput in girlDictionary:
        girlInfo = girlDictionary[nameInput]
        name = girlInfo["name"]
        url = girlInfo["url"]


        embed = discord.Embed(title=f"{girlName.title()}'s Stats", description=f"Globally\n\u200b",
                              color=discord.Color.blue())

        embed.set_image(url=url)

        embed.add_field(name="__Times Rolled (5 Girls)__", value=(totalCount), inline=False)
        embed.add_field(name="__Average Rank (5 Girls)__", value=f"{avgFive}\n\u200b", inline=False)
        embed.add_field(name="__Times Rolled (10 Girls)__", value=(totalCountTen), inline=False)
        embed.add_field(name="__Average Rank (10 Girls)__", value=avgTen, inline=False)

        await ctx.send(embed=embed)



# ────────────────────────────────────────────────────────────────────────────────────────────────
# Self Top Girls for Rounds of 5
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gt(ctx, user_id: str = None):

    if ctx.message.mentions:
        user = ctx.message.mentions[0]
        userID = int(user.id)
    elif user_id:
        try:
            userID = int(user_id)
            user = await bot.fetch_user(userID)
        except:
            user = None
    else:
        user = ctx.author
        userID = ctx.author.id

    girls = await asyncio.to_thread(list, girlAvgRanks.find())

    userAverages = []

    for girl in girls:
        ranks = girl.get("player_ranks", {}).get(str(userID))

        if not ranks or len(ranks) < 3:
            continue


        avg = sum(ranks) / len(ranks)
        userAverages.append((girl["girl_name"], round(avg, 2)))

    if not userAverages:
        if user and user.id == ctx.author.id:
            await ctx.send("You haven't ranked any girls 3 times yet silly!!")
        elif user:
            await ctx.send(f"{user.display_name} hasn't ranked any girls 3 times yet..!")
        else:
            await ctx.send("No rankings found.")
        return

    userAverages.sort(key=lambda x: x[1], reverse=False)

    per_page = 15
    pages_list = []

    for i in range(0, len(userAverages), per_page):
        start_rank = i + 1
        end_rank = min(i + per_page, len(userAverages))

        if user and user.id == ctx.author.id:
            title = f"{ctx.author.display_name}'s Highest Ranked Girls"
        else:
            userName = user.display_name if user else f"User {user_id}"
            title = f"{userName}'s Highest Ranked Girls"


        embed = discord.Embed(
            title=title,
            description=f"**Rounds of 5** - Top {start_rank}-{end_rank}\n\u200b",
            color=discord.Color.blue())


        for count, (name, avg) in enumerate(userAverages[i:i + per_page], start=start_rank):
            embed.add_field(name=f"#{count}: {name} - {avg}", value="", inline=False)


        embed.set_footer(text="Minimum of at least 3 rankings..!")
        pages_list.append(embed)

    view = PageView(pages_list)
    await ctx.send(embed=pages_list[0], view=view)


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Self Top Girls for Rounds of 10
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gtt(ctx, user_id: str = None):

    if ctx.message.mentions:
        user = ctx.message.mentions[0]
        userID = int(user.id)
    elif user_id:
        try:
            userID = int(user_id)
            user = await bot.fetch_user(userID)
        except:
            user = None
    else:
        user = ctx.author
        userID = ctx.author.id

    girls = await asyncio.to_thread(list, girlAvgRanksTen.find())

    userAverages = []

    for girl in girls:
        ranks = girl.get("player_ranks", {}).get(userID)

        if not ranks or len(ranks) < 3:
            continue


        avg = sum(ranks) / len(ranks)
        userAverages.append((girl["girl_name"], round(avg, 2)))

    if not userAverages:
        if user and user.id == ctx.author.id:
            await ctx.send("You haven't ranked any girls 3 times yet silly!!")
        elif user:
            await ctx.send(f"{user.display_name} hasn't ranked any girls 3 times yet..!")
        else:
            await ctx.send("No rankings found.")
        return

    userAverages.sort(key=lambda x: x[1], reverse=False)
    topRanks = userAverages[:15]

    if user and user.id == ctx.author.id:
        title = f"{ctx.author.display_name}'s Highest Ranked Girls"
    else:
        userName = user.display_name if user else f"User {user_id}"
        title = f"{userName}'s Highest Ranked Girls"

    embed = discord.Embed(title=title, description="**Rounds of 10**   -   Top 15 \n\u200b", color=discord.Color.blue())

    count = 1
    for name, avg in topRanks:
        embed.add_field(name=f"#{count}: {name} - {avg}", value="", inline=False)
        count += 1

    embed.set_footer(text="Minimum of at least 3 rankings..!")

    await ctx.send(embed=embed)





# ────────────────────────────────────────────────────────────────────────────────────────────────
# Global Top Girl for Rounds of 5
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gtg(ctx):
    girls = await asyncio.to_thread(list, girlAvgRanks.find())


    globalAverages = []

    for girl in girls:
        playerList = girl.get("player_ranks", [])

        userAverages = []

        for rankList in playerList.values():
            if rankList:
                userAverages.append(sum(rankList) / len(rankList))

        if len(userAverages) < 3:
            continue

        avg = round(sum(userAverages) / len(userAverages), 2)
        globalAverages.append((girl["girl_name"], avg))

    if not globalAverages:
        await ctx.send("There hasn't been enough ranking done yet..! :(")
        return

    globalAverages.sort(key=lambda x: x[1], reverse=False)

    per_page = 15
    pages_list = []

    for i in range(0, len(globalAverages), per_page):
        start_rank = i + 1  # First rank on this page
        end_rank = min(i + per_page, len(globalAverages))  # Last rank on this page

        embed = discord.Embed(
            title=f"Globally Highest Ranked Girls",
            description=f"**Rounds of 5** - Top {start_rank}-{end_rank}\n\u200b",
            color=discord.Color.blue()
        )

        for count, (name, avg) in enumerate(globalAverages[i:i + per_page], start=start_rank):
            embed.add_field(name=f"#{count}: {name} - {avg}", value="", inline=False)

        embed.set_footer(text="Minimum of at least 3 unique user rankings..!")
        pages_list.append(embed)

    view = PageView(pages_list)
    await ctx.send(embed=pages_list[0], view=view)




# ────────────────────────────────────────────────────────────────────────────────────────────────
# Global Top Girls for Rounds of 10
# ────────────────────────────────────────────────────────────────────────────────────────────────
@bot.command()
async def gttg(ctx):
    girls = await asyncio.to_thread(list, girlAvgRanksTen.find())


    globalAverages = []

    for girl in girls:
        playerList = girl.get("player_ranks", [])

        userAverages = []

        for rankList in playerList.values():
            if rankList:
                userAverages.append(sum(rankList) / len(rankList))

        if len(userAverages) < 3:
            continue

        avg = round(sum(userAverages) / len(userAverages), 2)
        globalAverages.append((girl["girl_name"], avg))

    if not globalAverages:
        await ctx.send("There hasn't been enough ranking done yet..! :(")
        return

    globalAverages.sort(key=lambda x: x[1], reverse=False)
    topGlobalRanks = globalAverages[:15]

    embed = discord.Embed(title="Globally Highest Ranked Girls", description="**Rounds of 10** - Top 15 \n\u200b", color=discord.Color.blue())

    count = 1
    for name, avg in topGlobalRanks:
        embed.add_field(name=f"#{count}: {name} - {avg}", value="", inline=False)
        count += 1

    embed.set_footer(text="Minimum of at least 3 unique user rankings..!")

    await ctx.send(embed=embed)






# ─── Main Runner ───────────────────────────────────────
async def main():
    async with bot:
        # Load your cogs here
        await bot.add_cog(AnimeRPG(bot, rpgdb))  # example
        await bot.add_cog(jltg(bot))
        await bot.start(TOKEN)




# ─── Start ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped manually.")


#bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)