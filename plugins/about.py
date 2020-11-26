# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class About(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        avatar = self.bot.user.avatar_url
        embed = discord.Embed(
            colour = discord.Colour.orange()
        )

        embed.set_author(name='About QnA Bot')
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text='Made with <3')

        embed.add_field(name='\u200b', value="QnA Bot was made by SilentVOEZ for the use of school with Discord as their platform and moderation in server. This bot is open-source which you can find in https://www.github.com/silentvoez/qna-bot and you can use it freely, modify it, redistribute it without restriction as long as you include the original license of this bot.", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))
