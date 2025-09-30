import os
from dotenv import load_dotenv
import discord
from discord.ext import  commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='~', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")



@bot.command()
async def helpme(ctx):
    help = """"
    Hai hai!!! You need some help?? You got it..!! :3
    
    ~ping - Pong!!! :3
    ~add x y - adds 2 numbers together.. I'm so smart!
    """
    await ctx.send(help)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f"Hai!! The sum of {num1} and {num2} is.... {result}! You're welcome!! :3")







bot.run(TOKEN)