# QnA Bot Version 1.0.1 Stable by SilentVOEZ#2523

import discord, datetime, time
import os
import sys
import psutil

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
    activity = discord.Game(name=f"{prefix}help | Stable version", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

# Extension commands/code I borrowed from DaijobuDes
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

@bot.command()
@commands.is_owner()
async def loadall(ctx):
    for filename in os.listdir('./plugins'):
        consoletime = datetime.datetime.now()
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'plugins.{filename[:-3]}')
                await ctx.send(f"**{filename}** extensions loaded.")
                print(f'{consoletime} [INFO] {filename} loaded')
            except Exception as e:
                await ctx.send(f"Failed to reload **{filename}**. Please check the extension's code or you were trying reloading an unloaded extension or non-exisiting extension.")
                print(f"{consoletime} [WARNING] Failed to load {filename}. Please check the extension's code or extension does not exist.")
                raise e

@bot.command()
@commands.is_owner()
async def unloadall(ctx):
    for filename in os.listdir('./plugins'):
        consoletime = datetime.datetime.now()
        if filename.endswith('.py'):
            bot.unload_extension(f'plugins.{filename[:-3]}')
            await ctx.send(f"**{filename}** unloaded")
            print(f'{consoletime} [INFO] {filename} extension unloaded.')

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    consoletime = datetime.datetime.now()
    await ctx.send('Shutting down')
    await ctx.bot.logout()
    print(f"Bot closed at {consoletime}")

for filename in os.listdir('./plugins'):
    consoletime = datetime.datetime.now()
    if filename.endswith('.py'):
        bot.load_extension(f'plugins.{filename[:-3]}')
        print(f'{consoletime} [INFO] {filename} loaded')

bot.run(TOKEN)