# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class Testpaper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
   
# Bot's original function, maybe not the perfect code.
    @commands.command()
    async def tphelp(self, ctx):
        tphelp = open("./testpaper/tphelp.txt","r").read()
        await ctx.send(tphelp)

    @commands.command()
    async def testpaper(self, ctx, *, subject=None):
        if not subject:
            await ctx.send("You didn't specify what subject!")

        subject = subject.lower()
        paper = open(f"./testpaper/{subject}.txt","r").read()
        await ctx.send(f"Good luck taking the test!")
        await ctx.author.send(paper)

def setup(bot):
    bot.add_cog(Testpaper(bot))