# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):
        responses = ["It's a rock!",
                    "It's a paper!",
                    "It's a scissor!",]
        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def eightball(self, ctx, *, question):
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
        print(f'Eightball triggered. Question: `{question}`')

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

def setup(bot):
    bot.add_cog(Fun(bot))