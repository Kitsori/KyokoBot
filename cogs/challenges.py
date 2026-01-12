import random
import asyncio
import discord



async def challenge1(ctx, bot):

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel


    challenge1 = discord.Embed(title="GUESS THE MYSTERY NUMBER",
                               description="I'm thinking of a number between 1 and 100. Guess my number correctly "
                                            "and win 25 coins!\n"
                                            "If guessed incorrectly, for every number off of my number, you earn 1 less coin."
                                            "Any numbers over 25 off from my number earn nothing.",
                               color=discord.Color.blue())

    await ctx.send(embed=challenge1)
    await asyncio.sleep(2)
    await ctx.send("Place your guess!! :3")

    number = random.randint(1, 100)

    running = True


    while running:

        msg = await bot.wait_for('message', check=check)
        content = msg.content.strip()

        if content.isdigit():
            guess = int(content)
            if (0 < guess < 101):

                await ctx.send(f"My number was {number}!")
                await asyncio.sleep(1)

                if (guess == number):
                    await ctx.send("You guessed it spot on!? Whaaat you sure you're not cheating..!?")
                    rewardEmbed = discord.Embed(description="### You gained 50 coins!!", color=discord.Color.green())
                    await ctx.send(embed=rewardEmbed)
                    return 25

                if (guess > number):
                    space = guess - number
                    if space <= 25:
                        reward = 25 - space
                        await ctx.send(f"You guessed over my number!! You were {space} off!")
                        rewardEmbed = discord.Embed(description=f"### You gained {reward} coins!!", color=discord.Color.green())
                        await ctx.send(embed=rewardEmbed)
                    else:
                        reward = 0
                        await ctx.send(f"You guessed {space} off! I'm sorry.. it's too far off for coins..! :(")
                    return reward

                if (number > guess):
                    space = number - guess
                    if space <= 25:
                        reward = 25 - space
                        await ctx.send(f"You guessed under my number!! You were {space} off!")
                        rewardEmbed = discord.Embed(description=f"### You gained {reward} coins!!", color=discord.Color.green())
                        await ctx.send(embed=rewardEmbed)
                    else:
                        reward = 0
                        await ctx.send(f"You guessed {space} off! I'm sorry.. it's too far off for coins..! :(")
                    return reward

            else:
                await ctx.send("That number is not in the valid range silly..!")






async def challenge2(ctx, bot):

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    challenge2 = discord.Embed(title="HIGHER OR LOWER",
                               description="Starting from 50, I will think of a random number between 1 to 100.\n"
                                           "For each number, guess if it is higher or lower than the previous number. "
                                           "For each correct guess you earn 3 coins! "
                                           "One incorrect guess and you're out!",
                               color=discord.Color.blue())

    await ctx.send(embed=challenge2)
    await asyncio.sleep(2)

    number = 50
    reward = 0
    running = True

    while running:
        await ctx.send(f"I'm thinking of a number... do you think it's higher or lower than {number}..? (h/l)?")
        newNumber = random.randint(1, 100)

        msg = await bot.wait_for('message', check=check)
        content = msg.content.strip().lower()


        if content in ('h', 'l'):
            await ctx.send(f"I was thinking of {newNumber}...")
            await asyncio.sleep(1)

            if content == 'h' and newNumber > number:
                await ctx.send("You guessed correctly!")
                number = newNumber
                reward += 3
                await asyncio.sleep(1)
            elif content == 'l' and newNumber < number:
                await ctx.send("You guessed correctly!")
                number = newNumber
                reward += 3
                await asyncio.sleep(1)
            else:
                await ctx.send("Awww I'm sorry that was not the correct side...")
                running = False
        else:
            await ctx.send("Send a valid answer dummy!")

    if reward > 0:
        rewardEmbed = discord.Embed(description=f"### You gained {reward} coins!!", color=discord.Color.green())
        await ctx.send(embed=rewardEmbed)
    return reward






async def blessing1(ctx, bot):

    blessing1 = discord.Embed(title="BLESSING OF THE COIN GOD",
                               description="Wow!! It's your lucky day! You found 15 coins on the ground that you instantly earn!",
                               color=discord.Color.yellow())

    await ctx.send(embed=blessing1)
    await asyncio.sleep(2)

    rewardEmbed = discord.Embed(description="### You gained 15 coins!!", color=discord.Color.green())
    await ctx.send(embed=rewardEmbed)
    return 15



async def curse1(ctx, bot):

    curse1 = discord.Embed(title="CURSE OF THE ANCIENT WALLET",
                               description="Lose 50% of your current coins.\n"
                                           "Maybe it's time to get a safer wallet than carrying around that one full of holes...",
                               color=discord.Color.purple())

    await ctx.send(embed=curse1)
    await asyncio.sleep(2)
    return "CURSE1"










raceChallenges = [challenge1, challenge2, blessing1, curse1]