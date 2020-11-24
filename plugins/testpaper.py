# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
import datetime
import json
import asyncio
import os
import psutil
from discord.ext import commands

class Testpaper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
   
# Bot's original function, maybe not the perfect code.
    @commands.command()
    async def tphelp(self, ctx):
        with open(f"./prefix.txt", "r") as botprefix:
            prefix = botprefix.read()

        directory = os.listdir("./testpaper")

        text = "\n**Subjects**\n"

        for i in range(0, len(directory)):
            text += f"> **{prefix}testpaper {directory[i][:-5].lower()}** - starts the {directory[i][:-5].lower()} test\n"
            if i == len(directory) - 1:
                if psutil.WINDOWS:
                    text += "\n   **NOTICE: Some subjects may not work if it's running on Windows**"
                    
        await ctx.send(text)
        botprefix.close()

    @commands.command()
    async def testpaper(self, ctx, *, subject=None):
        consoletime = datetime.datetime.now()
        
        subject.lower()
        with open(f"./testpaper/{subject}.json", "r") as paper:
            data = json.load(paper)

        print(f"{consoletime} [INFO] Testpaper triggered by '{ctx.author}' with a subject '{subject}'.")
        await ctx.send(f"I'm sending the paper through direct message. Good luck taking the test!")

        embed = discord.Embed(colour=0x00ff00)

        embed.add_field(name=f'{data["school"]}', value=f'Subject: {data["subject"].title()} with {int(len(data["questions"]))} questions. Good luck!')
        await ctx.author.send(embed=embed)
        embed.remove_field(0)

        await asyncio.sleep(5)

        embed.add_field(name=f'Directions', value=f'{data["directions"]}')
        await ctx.author.send(embed=embed)
        embed.remove_field(0)

        await asyncio.sleep(2)

        for i in range(0, int(len(data["questions"]))):
            choiceA = data["questions"][f"{i+1}"]["choices"]["A"]
            choiceB = data["questions"][f"{i+1}"]["choices"]["B"]
            choiceC = data["questions"][f"{i+1}"]["choices"]["C"]
            choiceD = data["questions"][f"{i+1}"]["choices"]["D"]
            embed.add_field(name=f'Question {i+1}: {data["questions"][f"{i+1}"]["ask"]}', value=f'**A.** {choiceA} **B.** {choiceB} **C.** {choiceC} **D.** {choiceD}')
            await ctx.author.send(embed=embed)
            embed.remove_field(0)
            await asyncio.sleep(3)
        
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