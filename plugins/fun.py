# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loli(self, ctx):
        responses = ['Moshi moshi FBI desu!',
                    'All the lolis were out now so no loli for you.',
                    'Guards are watching now.',
                    'The NSA is watching you.',
                    "They're sleeping, you can't wake them up.",
                    '*sirens incoming*',
                    'Pervert.',
                    'Lolicon.',
                    "I'll send you to jail.",
                    'This is the police and it seems you are suspicious from your activity',
                    'https://memegenerator.net/img/instances/73517979/tadaima-motherfucker.jpg',
                    'https://media.tenor.com/images/1ec1659fd1cdaaf72a9a5fa566f842d6/tenor.gif',
                    'https://media.tenor.com/images/523e65404d07340e5397c7b5e0d0929b/tenor.gif']
        await ctx.send(f'{random.choice(responses)}')

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
                    'https://www.youtube.com/watch?v=FAQQUMcRj_Q']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def dorime(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=zQ4LiyFF8RU')
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Fun(bot))