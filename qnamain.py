# QnA Bot Version 0.9.4 Pre-release Final Debug by SilentVOEZ#2523

import discord, datetime, time
import os
import sys

import asyncio
from discord.ext import commands

start_time = time.time()

TOKEN = open("./token.txt","r").read()
PREFIX = open("./prefix.txt","r").read()

ID = open ("./author.txt", "r").read()
ID_list = ID.split()
map_object = map(int, ID_list)
list_IDs = list(map_object)

bot = commands.Bot(command_prefix=PREFIX, owner_ids=list_IDs)
bot.remove_command('help')

@bot.event
async def on_ready():
    prefix = open('./prefix.txt','r').read()
    print(f'----------------')
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print(f'----------------')
    print(f'Ensure that the bot has adequate permission to prevent errors while in use.')
    print(f'----------------')
    activity = discord.Game(name=f"{prefix}help, PR Final Debugging", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

# Uptime command
@bot.command(pass_context=True)
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=ctx.message.author.top_role.colour)
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text="Bot by SilentVOEZ")
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("Current uptime: " + text)


# Status Cycle (TY DaijobuDes)
@bot.command()
@commands.is_owner()
async def status(ctx, status: str):
    status.lower()
    prefix = open('./prefix.txt','r').read()
    activity = discord.Game(name=f"{prefix}help, PR Final Debugging", type=3)
    if status == 'online':
        await bot.change_presence(status=discord.Status.online, activity=activity)
    elif status == 'idle':
        await bot.change_presence(status=discord.Status.idle, activity=activity)
    elif status == 'dnd' or status == 'donotdisturb':
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
    else:
        await ctx.send(f'"{status}" is not a valid argument.')

# A bit of code borrowed from DaijobuDes
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    consoletime = datetime.datetime.now()
    try:
        bot.load_extension(f'plugins.{extension}')
        print(f'{consoletime} [INFO] {extension} loaded')
        await ctx.send(f'**{extension}** loaded')
    except Exception as e:
        print(f"{consoletime} [WARNING] Failed to load {extension}. Please check the extension's code or extension does not exist.")
        await ctx.send(f"Failed to load **{extension}**. Please check the extension's code or extension does not exist.")
        raise e

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    consoletime = datetime.datetime.now()
    try:
        bot.unload_extension(f'plugins.{extension}')
        print(f'{consoletime} [INFO] {extension} unloaded')
        await ctx.send(f'**{extension}** unloaded')
    except Exception as e:
        print(f"{consoletime} [WARNING] Failed to unload {extension}. Extension does not exist or it's been already unloaded.")
        await ctx.send(f"Failed to unload **{extension}**. Extension does not exist or it's been already unloaded.")
        raise e
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    consoletime = datetime.datetime.now()
    try:
        bot.unload_extension(f'plugins.{extension}')
        bot.load_extension(f'plugins.{extension}')
        print(f'{consoletime} [INFO] {extension} reloaded')
        await ctx.send(f'**{extension}** reloaded')
    except Exception as e:
        print(f"{consoletime} [WARNING] Failed to reload {extension}. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
        await ctx.send(f"Failed to reload **{extension}**. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
        raise e

for filename in os.listdir('./plugins'):
    consoletime = datetime.datetime.now()
    if filename.endswith('.py'):
        bot.load_extension(f'plugins.{filename[:-3]}')
        print(f'{consoletime} [INFO] {filename} loaded')

bot.run(TOKEN)