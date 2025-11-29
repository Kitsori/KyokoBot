import discord
from discord.ext import commands
import asyncio
import traceback
import random

import time
from datetime import datetime, timedelta




class jltg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def race(self, ctx):
        try:
            currentTime = datetime.strptime("8:00", "%I:%M")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            start = True
            win = False

            distance = 0
            taggerDistance = 0
            targetDistance = random.randint(1000,2000)

            coins = 100

            numTrains = random.randint(2, 5)
            trains = []

            for i in range(numTrains):
                time = random.randint(1, 120)
                length = random.randint(10, 180)
                arrival = time + length

                trainTime = (currentTime + timedelta(minutes=time))
                trainArrival = (currentTime + timedelta(minutes=arrival))
                trainLength = length

                trainInfo = {
                    "Departure": trainTime,
                    "Arrival": trainArrival,
                    "Duration": trainLength,
                }
                trains.append(trainInfo)

            for index, t in enumerate(trains, start=1):
                await ctx.send(f"Train {index}:\n"
                        f"Departure: {t['Departure'].strftime('%I:%M %p')}\n"
                        f"Arrival: {t['Arrival'].strftime('%I:%M %p')}\n"
                        f"Duration: {t['Duration']} minutes\n"
                        "==============="
                        )


            async def clock():
                currentTime = datetime.strptime("8:00", "%I:%M")
                time = await ctx.send(f"Current Time: {currentTime.strftime('%I:%M %p')}")
                running = True

                await ctx.send("Can you make it to your target before the taggers catch up with you? \n"
                               "Each minute on a train costs 1 coin..! :3 \n "
                               "==================================================")
                await asyncio.sleep(5)
                while running:
                    await time.edit(content=f"Current Time: {currentTime.strftime('%I:%M %p')}")
                    await asyncio.sleep(2)
                    currentTime += timedelta(minutes=1)

                    if currentTime.hour >= 19:
                        running = False

            if start == True:
                clockTask = asyncio.create_task(clock())
                await asyncio.sleep(1)

            if win == True:
                clockTask.cancel()

            await ctx.send(f"Balance: {coins} coins \n"
                          f"--------------------")
            await ctx.send("What do you want to do..? :3 \n 1-5: Take Train \n 6: Pull Challenge")
            trainResponse = await self.bot.wait_for('message', check=check)

            if trainResponse.content == "1":
                train = trains[1].content
                time = train["Duration"]
                await ctx.send(train)









        except Exception:
            await ctx.send(f"```{traceback.format_exc()}```")