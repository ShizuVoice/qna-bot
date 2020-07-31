# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f"{self.bot.user.name} got disconnected! Attempting to reconnect...")

    @commands.Cog.listener()
    async def on_connect(self):
        print(f"{self.bot.user.name} successfully connected.")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"{message.author} said {message.content}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to do that!")
        if isinstance(error,commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to do certain action. Check other roles that may be overriding the bot's own role permission.")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))