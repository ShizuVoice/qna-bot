# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime
from discord.ext import commands

class Testpaper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
   
# Bot's original function, maybe not the perfect code.
    @commands.command()
    async def tphelp(self, ctx):
        with open(f"./testpaper/tphelp.txt","r") as tphelp:
            tph = tphelp.read()
        await ctx.send(tph)
        tphelp.close()

    @commands.command()
    async def testpaper(self, ctx, *, subject=None):
        consoletime = datetime.datetime.now()
#        if not subject:
#            await ctx.send("You didn't specify what subject!")

        subject = subject.lower()
        with open(f"./testpaper/{subject}.txt", "r") as paper:
            testpaper = paper.read()

#        paper = open(f"./testpaper/{subject}.txt","r").read()
        print(f"{consoletime} [INFO] Testpaper triggered by '{ctx.author}' with a subject '{subject}'.")
        await ctx.send(f"Good luck taking the test!")
        await ctx.author.send(testpaper)
        paper.close()

    @testpaper.error
    async def testpaper_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        with open(f"./prefix.txt", "r") as botprefix:
            prefix = botprefix.read()

        if isinstance(error, commands.CommandInvokeError):
            print(f"{consoletime} [INFO] Testpaper triggered, but no subject specified or subject does not exist.")
            await ctx.send(f"You didin't specify the subject or subject doesn't exist! Please refer to `{prefix}tphelp`")
            botprefix.close()

def setup(bot):
    bot.add_cog(Testpaper(bot))