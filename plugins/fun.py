# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx, *, draw):
        consoletime = datetime.datetime.now()
        responses = ["rock!",
                    "paper!",
                    "scissor!",]
        await ctx.send("It's a " + f'{random.choice(responses)}')
        print(f"{consoletime} [INFO] RPS triggered. '{ctx.author}' drawed {draw}.")

    @commands.command()
    async def eightball(self, ctx, *, question):
        consoletime = datetime.datetime.now()
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'{random.choice(responses)}')
        print(f"{consoletime} [INFO] Eightball triggered. Question: `{question}`")

    @commands.command()
    async def eightballfil(self, ctx, *, question):
        consoletime = datetime.datetime.now()
        responses = ["Panigurado.",
                    "Napagpasyahan ito.",
                    "Walang duda.",
                    "Oo - sigurado.",
                    "Maaari kang umasa dito.",
                    "Sa nakikita ko, oo.",
                    "Maaaring totoo.",
                    "Oo.",
                    "Nakikita ko na oo.",
                    "Medyo malabo yung sagot, subukan mo ulit.",
                    "Magtanong ka mamaya.",
                    "Mas mabuti na hindi sabihin sa iyo ngayon.",
                    "Hindi mahuhulaan ngayon.",
                    "Pagtuon at magtanong muli.",
                    "Ang sagot ko hindi.",
                    "Hindi.",
                    "Medyo hindi maganda.",
                    "Napaka duda."]
        await ctx.send(f'{random.choice(responses)}')
        print(f"{consoletime} [INFO] Eightballfil triggered. Question: `{question}`")

    @commands.command()
    async def haachama(self, ctx):
        responses = ['https://www.youtube.com/watch?v=h2CfS9akvVo',
                    'https://www.youtube.com/watch?v=xBqWAQodhFg',
                    'https://www.youtube.com/watch?v=iGUzLFFKf7w',
                    'https://www.youtube.com/watch?v=HQvX9ClXsWE',
                    'https://www.youtube.com/watch?v=0y6vH-AZKMk',
                    'https://www.youtube.com/watch?v=S9OLBMG0-nY',
                    'https://www.youtube.com/watch?v=NRKsqut_FUw',
                    'https://www.youtube.com/watch?v=9zJMVHULJ0c',
                    'https://www.youtube.com/watch?v=rAEjfEd8uSk',
                    'https://www.youtube.com/watch?v=XTlDdGA5cO8',
                    'https://www.youtube.com/watch?v=cGxKncDHY_U',
                    'https://www.youtube.com/watch?v=kPBZOjh-tP4',
                    'https://www.youtube.com/watch?v=R9dLe4vOfz8',
                    'https://www.youtube.com/watch?v=D1t0NsYy4mI',
                    'https://www.youtube.com/watch?v=FAQQUMcRj_Q',
                    'https://www.youtube.com/watch?v=B5KoNaDvfmc']
        await ctx.send(f'{random.choice(responses)}')

def setup(bot):
    bot.add_cog(Fun(bot))