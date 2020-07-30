# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime, time
from discord.ext import commands

start_time = time.time()

class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Shutting down')
        await ctx.bot.logout()
        print("Bot Closed")

    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You do not own this bot!")

def setup(bot):
    bot.add_cog(Utility(bot))