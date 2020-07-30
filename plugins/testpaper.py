# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class Testpaper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
   
# Bot's original function, everything is still in progress.
    @commands.command()
    async def tphelp(self, ctx):
        tphelp = open("./testpaper/tphelp.txt","r").read()
        await ctx.send(tphelp)

    @commands.command()
    async def oldtestpaper(self, ctx):
        testpaper = open("./testpaper/testpaper.txt","r").read()
        await ctx.send(f'Good luck taking the test!')
        await ctx.author.send(testpaper)

    @commands.command()
    async def testpaper(self, ctx, *, subject=None):
        if not subject:
            await ctx.send("You didn't specify what subject!")

        subject = subject.lower()
        paper = open(f"./testpaper/{subject}.txt","r").read()
        await ctx.send(f"Good luck taking the test!")
        await ctx.author.send(paper)
        

#    @commands.command()
#    async def testpaper(self, ctx, *, subject=None):
#        if not subject:
#            await ctx.send("Error: Please input subject!")
#            return
#
#        subject = subject.lower() # Lower-case only
#        with open("./testpaper/testpaper.json") as f:
#            content = json.load(f)
#
#        try:
#            paper = content[subject]
#        except KeyError:
#            await ctx.send("No paper named" + subject)
#            return
#        await ctx.send(f"Good luck taking the test!")
#        await ctx.author.send(paper)

def setup(bot):
    bot.add_cog(Testpaper(bot))