# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        consoletime = datetime.datetime.now()
        await ctx.send('Shutting down')
        await ctx.bot.logout()
        print(f"Bot closed at {consoletime}")


def setup(bot):
    bot.add_cog(Utility(bot))