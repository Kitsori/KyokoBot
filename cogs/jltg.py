import discord
from discord.ext import commands
import asyncio
import traceback
import random

import time
from datetime import datetime, timedelta
from cogs.challenges import raceChallenges




class jltg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tag(self, ctx):
        try:
            currentTime = datetime.strptime("8:00", "%I:%M")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel



            async def clock():
                self.currentTime = datetime.strptime("8:00", "%I:%M")
                time = await ctx.send(f"Current Time: {self.currentTime.strftime('%I:%M %p')}")
                await ctx.send("=======================")
                running = True

                await asyncio.sleep(1)
                await ctx.send("Can you make it to your target location before the taggers catch up with you? \n"
                               "You have 12 hours, from 8AM to 8PM...\n"
                               "Each minute on a train costs 1 coin..! :3 \n"
                               "Use ~taghelp for more info!\n"
                               "=======================")
                await asyncio.sleep(5)

                while running:
                    await time.edit(content=f"Current Time: {self.currentTime.strftime('%I:%M %p')}")
                    await asyncio.sleep(3)
                    self.currentTime += timedelta(minutes=1)

                    if self.currentTime.hour >= 20:
                        running = False



            start = True
            gameEnd = False
            coins = 100

            userDistance = 0
            targetDistance = random.randint(500, 1000)




            #async def taggers():
            #    nonlocal taggerDistance, userDistance
            #.    await asyncio.sleep(50)





            while gameEnd == False:


                if targetDistance <= 0:
                    gameEnd = True

                if start == True:
                    clockTask = asyncio.create_task(clock())
                    await asyncio.sleep(5)
                    start = False

                if gameEnd == True:
                    clockTask.cancel()
                    await ctx.send("You made it to your end location in time without being caught!!! CONGRATS!!! :3")




                numTrains = random.randint(2, 5)
                trains = []

                for i in range(numTrains):
                    time = random.randint(5, 120)
                    length = random.randint(10, 180)
                    distance = random.randint(10, 200)
                    arrival = time + length

                    trainTime = (self.currentTime + timedelta(minutes=time))
                    trainArrival = (self.currentTime + timedelta(minutes=arrival))
                    trainLength = length
                    trainDistance = distance

                    trainInfo = {
                        "Departure": trainTime,
                        "Arrival": trainArrival,
                        "Duration": trainLength,
                        "Distance": trainDistance,
                    }
                    trains.append(trainInfo)


                for index, t in enumerate(trains, start=1):
                    await ctx.send(f"## Train {index}:\n"
                            f"**Departure:** {t['Departure'].strftime('%I:%M %p')}\n"
                            f"**Arrival:** {t['Arrival'].strftime('%I:%M %p')}\n"
                            "~ ~ ~\n"
                            f"**Duration:** {t['Duration']} minutes\n"
                            f"**Distance:** {t['Distance']} miles\n"
                            "======================="
                            )

                trainNumber = len(trains)




                await ctx.send(f"**Balance**: {coins} coins \n"
                              f"**Distance Remaining**: {targetDistance} miles\n"
                              f"**Distance Traveled**: {userDistance} miles\n"
                              "===============\n")
                await ctx.send("What do you want to do..? :3 \n"
                               f"1-{trainNumber}: Take Train \n"
                               "6: Pull a Card \n"
                               "7: Check Time\n"
                               "8: Train List\n"
                               "9: Stats & Menu\n"
                               "0: Give Up"
                               )




                picking = True

                while picking:

                    trainResponse = await self.bot.wait_for('message', check=check)
                    content = trainResponse.content.strip()

                    if content.isdigit():
                        if trainResponse.content == "1":
                            train = trains[0]
                            lineTime = train["Duration"]
                            lineLength = train["Distance"]

                            if coins >= lineTime:
                                if self.currentTime <= train["Departure"]:

                                    await ctx.send(f"Train 1 leaves by {train['Departure'].strftime('%I:%M %p')}. "
                                                   f"It would arrive at the next station at {train['Arrival'].strftime('%I:%M %p')}")
                                    await ctx.send(f"It would take {lineTime} minutes to travel {lineLength} miles to the next station.")
                                    await asyncio.sleep(1)

                                    await ctx.send("-----")
                                    await asyncio.sleep(1)

                                    await ctx.send(f"Your new remaining distance would be {targetDistance - lineLength} miles")
                                    await ctx.send(f"Your remaining coin balance would be {coins - lineTime} coins.")
                                    await asyncio.sleep(1)

                                    await ctx.send("Do you want to take this train? (y/n)")
                                    takeTrain = await self.bot.wait_for('message', check=check)
                                    takeTrainBool = True

                                    while takeTrainBool:

                                        if takeTrain.content == "y":
                                            await ctx.send("Welcome aboard!! :3")
                                            await ctx.send(f"Your time will be fast forwarded to {train['Arrival'].strftime('%I:%M %p')}.")

                                            userDistance += lineLength
                                            targetDistance = targetDistance - lineLength
                                            coins = coins - lineTime
                                            self.currentTime = self.currentTime.replace(hour=train['Arrival'].hour, minute=train['Arrival'].minute, second=0)

                                            takeTrainBool = False
                                            picking = False

                                        elif takeTrain.content == "n":
                                            await ctx.send("No train for you..!")

                                            takeTrainBool = False
                                        else:
                                            await ctx.send("Not a valid answer.")

                                else:
                                    await ctx.send("You missed this train dummy..!")

                            else:
                                await ctx.send("You don't have enough coins to take this train! You gotta do more challenges silly! :3")




                        elif trainResponse.content == "2":
                            train = trains[1]
                            lineTime = train["Duration"]
                            lineLength = train["Distance"]

                            if coins >= lineTime:
                                if self.currentTime <= train["Departure"]:
                                    await ctx.send(f"Train 2 leaves by {train['Departure'].strftime('%I:%M %p')}. "
                                                   f"It would arrive at the next station at {train['Arrival'].strftime('%I:%M %p')}")
                                    await ctx.send(
                                        f"It would take {lineTime} minutes to travel {lineLength} miles to the next station.")
                                    await asyncio.sleep(1)

                                    await ctx.send("-----")
                                    await asyncio.sleep(1)

                                    await ctx.send(f"Your new remaining distance would be {targetDistance - lineLength} miles")
                                    await ctx.send(f"Your remaining coin balance would be {coins - lineTime} coins.")
                                    await asyncio.sleep(1)

                                    await ctx.send("Do you want to take this train? (y/n)")
                                    takeTrain = await self.bot.wait_for('message', check=check)
                                    takeTrainBool = True

                                    while takeTrainBool:

                                        if takeTrain.content == "y":
                                            await ctx.send("Welcome aboard!! :3")
                                            await ctx.send(f"Your time will be fast forwarded to {train['Arrival'].strftime('%I:%M %p')}.")
                                            await asyncio.sleep(2)

                                            userDistance += lineLength
                                            targetDistance = targetDistance - lineLength
                                            coins = coins - lineTime
                                            self.currentTime = self.currentTime.replace(hour=train['Arrival'].hour, minute=train['Arrival'].minute, second=0)

                                            takeTrainBool = False
                                            picking = False

                                        elif takeTrain.content == "n":
                                            await ctx.send("No train for you..!")
                                            takeTrainBool = False

                                        else:
                                            await ctx.send("Not a valid answer.")

                                else:
                                    await ctx.send("You missed this train dummy..!")

                            else:
                                await ctx.send("You don't have enough coins to take this train! You gotta do more challenges silly! :3")


                        elif trainResponse.content == "3" and len(trains) > 2:
                            train = trains[2]
                            lineTime = train["Duration"]
                            lineLength = train["Distance"]

                            if coins >= lineTime:
                                if self.currentTime <= train["Departure"]:
                                    await ctx.send(f"Train 3 leaves by {train['Departure'].strftime('%I:%M %p')}. "
                                                   f"It would arrive at the next station at {train['Arrival'].strftime('%I:%M %p')}")
                                    await ctx.send(
                                        f"It would take {lineTime} minutes to travel {lineLength} miles to the next station.")
                                    await asyncio.sleep(1)

                                    await ctx.send("-----")
                                    await asyncio.sleep(1)

                                    await ctx.send(f"Your new remaining distance would be {targetDistance - lineLength} miles")
                                    await ctx.send(f"Your remaining coin balance would be {coins - lineTime} coins.")
                                    await asyncio.sleep(1)

                                    await ctx.send("Do you want to take this train? (y/n)")
                                    takeTrain = await self.bot.wait_for('message', check=check)
                                    takeTrainBool = True

                                    while takeTrainBool:

                                        if takeTrain.content == "y":
                                            await ctx.send("Welcome aboard!! :3")
                                            await ctx.send(f"Your time will be fast forwarded to {train['Arrival'].strftime('%I:%M %p')}.")
                                            await asyncio.sleep(2)

                                            userDistance += lineLength
                                            targetDistance = targetDistance - lineLength
                                            coins = coins - lineTime
                                            self.currentTime = self.currentTime.replace(hour=train['Arrival'].hour, minute=train['Arrival'].minute, second=0)

                                            takeTrainBool = False
                                            picking = False

                                        elif takeTrain.content == "n":
                                            await ctx.send("No train for you..!")
                                            takeTrainBool = False

                                        else:
                                            await ctx.send("Not a valid answer.")

                                else:
                                    await ctx.send("You missed this train dummy..!")

                            else:
                                await ctx.send("You don't have enough coins to take this train! You gotta do more challenges silly! :3")




                        elif trainResponse.content == "4" and len(trains) > 3:
                            train = trains[3]
                            lineTime = train["Duration"]
                            lineLength = train["Distance"]

                            if coins >= lineTime:
                                await ctx.send(f"Train 4 leaves by {train['Departure'].strftime('%I:%M %p')}. "
                                               f"It would arrive at the next station at {train['Arrival'].strftime('%I:%M %p')}")
                                await ctx.send(
                                    f"It would take {lineTime} minutes to travel {lineLength} miles to the next station.")
                                await asyncio.sleep(1)

                                await ctx.send("-----")
                                await asyncio.sleep(1)

                                await ctx.send(f"Your new remaining distance would be {targetDistance - lineLength} miles")
                                await ctx.send(f"Your remaining coin balance would be {coins - lineTime} coins.")
                                await asyncio.sleep(1)

                                await ctx.send("Do you want to take this train? (y/n)")
                                takeTrain = await self.bot.wait_for('message', check=check)
                                takeTrainBool = True

                                while takeTrainBool:

                                    if takeTrain.content == "y":
                                        await ctx.send("Welcome aboard!! :3")
                                        await ctx.send(f"Your time will be fast forwarded to {train['Arrival'].strftime('%I:%M %p')}.")

                                        userDistance += lineLength
                                        targetDistance = targetDistance - lineLength
                                        coins = coins - lineTime
                                        self.currentTime = self.currentTime.replace(hour=train['Arrival'].hour, minute=train['Arrival'].minute, second=0)

                                        takeTrainBool = False
                                        picking = False

                                    elif takeTrain.content == "n":
                                        await ctx.send("No train for you..!")
                                        takeTrainBool = False

                                    else:
                                        await ctx.send("Not a valid answer.")




                        elif trainResponse.content == "5" and len(trains) > 4:
                            train = trains[4]
                            lineTime = train["Duration"]
                            lineLength = train["Distance"]

                            if coins >= lineTime:
                                await ctx.send(f"Train 5 leaves by {train['Departure'].strftime('%I:%M %p')}. "
                                               f"It would arrive at the next station at {train['Arrival'].strftime('%I:%M %p')}")
                                await ctx.send(
                                    f"It would take {lineTime} minutes to travel {lineLength} miles to the next station.")
                                await asyncio.sleep(1)

                                await ctx.send("-----")
                                await asyncio.sleep(1)

                                await ctx.send(f"Your new remaining distance would be {targetDistance - lineLength} miles")
                                await ctx.send(f"Your remaining coin balance would be {coins - lineTime} coins.")
                                await asyncio.sleep(1)

                                await ctx.send("Do you want to take this train? (y/n)")
                                takeTrain = await self.bot.wait_for('message', check=check)
                                takeTrainBool = True

                                while takeTrainBool:

                                    if takeTrain.content == "y":
                                        await ctx.send("Welcome aboard!! :3")
                                        await ctx.send(f"Your time will be fast forwarded to {train['Arrival'].strftime('%I:%M %p')}.")

                                        userDistance += lineLength
                                        targetDistance = targetDistance - lineLength
                                        coins = coins - lineTime
                                        self.currentTime = self.currentTime.replace(hour=train['Arrival'].hour, minute=train['Arrival'].minute, second=0)

                                        takeTrainBool = False
                                        picking = False

                                    elif takeTrain.content == "n":
                                        await ctx.send("No train for you..!")
                                        takeTrainBool = False

                                    else:
                                        await ctx.send("Not a valid answer.")




                        elif trainResponse.content == "6":

                            msg = await ctx.send("Drawing a card.")
                            await asyncio.sleep(1)
                            await msg.edit(content=f"Drawing a card..")
                            await asyncio.sleep(1)
                            await msg.edit(content=f"Drawing a card...")
                            await asyncio.sleep(1)

                            challenge = random.choice(raceChallenges)


                            reward = await challenge(ctx, self.bot)

                            if reward == "CURSE1":
                                coinsLost = coins // 2
                                curseEmbed = discord.Embed(description=f"### You lost {coinsLost} coins!!",
                                                            color=discord.Color.red())
                                await ctx.send(embed=curseEmbed)
                                coins = coins - coinsLost
                            else:
                                coins += reward

                            await asyncio.sleep(1)
                            await ctx.send(f"You now have **{coins}** coins!")




                        elif trainResponse.content == "7":
                            await ctx.send(f"Current Time: {self.currentTime.strftime('%I:%M %p')}")




                        elif trainResponse.content == "8":
                            for index, t in enumerate(trains, start=1):
                                await ctx.send(f"## Train {index}:\n"
                                               f"**Departure:** {t['Departure'].strftime('%I:%M %p')}\n"
                                               f"**Arrival:** {t['Arrival'].strftime('%I:%M %p')}\n"
                                               "~ ~ ~\n"
                                               f"**Duration:** {t['Duration']} minutes\n"
                                               f"**Distance:** {t['Distance']} miles\n"
                                               "======================="
                                               )




                        elif trainResponse.content == "9":
                            await ctx.send(f"**Balance**: {coins} coins \n"
                                           f"**Distance Remaining**: {targetDistance} miles\n"
                                           f"**Distance Traveled**: {userDistance} miles\n"
                                           "===============\n")
                            await ctx.send("What do you want to do..? :3 \n"
                                           f"1-{trainNumber}: Take Train \n"
                                           "6: Pull a Card \n"
                                           "7: Check Time\n"
                                           "8: Train List\n"
                                           "9: Stats & Menu\n"
                                           "0: Give Up"
                                           )



                        elif trainResponse.content == "0":
                            await ctx.send("Couldn't handle the pressure huh?? Oh well...")
                            return






                        else:
                            await ctx.send("Not a valid option.")














        except Exception:
            await ctx.send(f"```{traceback.format_exc()}```")