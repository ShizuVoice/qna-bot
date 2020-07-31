# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Shutting down')
        await ctx.bot.logout()
        print("Bot Closed")

def setup(bot):
    bot.add_cog(Utility(bot))