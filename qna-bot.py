# QnA Bot Version 0.1 alpha by SilentVOEZ#2523

import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = open("token.txt","r").read()
bot = commands.Bot(command_prefix='q!')

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'----------------')

# Bot Commands

@bot.command()
async def ping(ctx):
    """Pong"""
    await ctx.send('POG')

@bot.command()
async def version(ctx):
    """Shows the Bot version"""
    await ctx.send("> QnA Bot version 0.1 alpha by SilentVOEZ")

@bot.command()
async def OwO(ctx):
    await ctx.send("What's this?")

@bot.command()
async def owo(ctx):
    await ctx.send("What's this?")

@bot.command()
async def loli(ctx):
    """Try it, maybe it show you something cool."""
    await ctx.send("Moshi moshi FBI desu~")

# Bot's function to open a question paper

@bot.command()
async def startquiz(ctx):
    """Initializes the test question"""
    # So how the fuck am I gonna do here?
    await ctx.send("***Soon*** (*tm*)")

bot.run(TOKEN)