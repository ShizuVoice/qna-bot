# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"{message.author} said {message.content}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You do not have permission to do that!")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))