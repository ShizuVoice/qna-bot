# QnA Bot Version 0.8.2 Beta by SilentVOEZ#2523

#import logging
import discord
import os

import asyncio
from discord.ext import commands

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger('discord')
#logger.setLevel(logging.INFO)
#handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

TOKEN = open("./token.txt","r").read()
PREFIX = open("./prefix.txt","r").read()
bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')

async def is_owner(ctx):
    owner = open("author.txt","r").read()
    return ctx.author.id == owner

@bot.event
async def on_ready():
    print(f'----------------')
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'----------------')
    print(f'Ensure that the bot has adequate permission to prevent errors while in use.')
    print(f'----------------')
    activity = discord.Game(name="q!help, Beta release", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

# Status Cycle
@bot.command()
async def statusonline(ctx):
    activity = discord.Game(name="q!help, Beta release", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command()
async def statusidle(ctx):
    activity = discord.Game(name="q!help, Beta release", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.command()
async def statusdnd(ctx):
    activity = discord.Game(name="q!help, Beta release", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)

#Code borrowed from DaijobuDes
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(f'plugins.{extension}')
        print(f'{extension} loaded')
        await ctx.send(f'**{extension}** loaded')
    except Exception as e:
        print(f"Failed to load {extension}. Please check the extension's code or extension does not exist.")
        await ctx.send(f"Failed to load **{extension}**. Please check the extension's code or extension does not exist.")
        raise e

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'plugins.{extension}')
        print(f'{extension} unloaded')
        await ctx.send(f'**{extension}** unloaded')
    except Exception as e:
        print(f"Failed to unload {extension}. Extension does not exist or it's been already unloaded.")
        await ctx.send(f"Failed to unload **{extension}**. Extension does not exist or it's been already unloaded.")
        raise e
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(f'plugins.{extension}')
        bot.load_extension(f'plugins.{extension}')
        print(f'{extension} reloaded')
        await ctx.send(f'**{extension}** reloaded')
    except Exception as e:
        print(f"Failed to reload {extension}. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
        await ctx.send(f"Failed to reload **{extension}**. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
        raise e

for filename in os.listdir('./plugins'):
    if filename.endswith('.py'):
        bot.load_extension(f'plugins.{filename[:-3]}')
        print(f'{filename} loaded')

bot.run(TOKEN)