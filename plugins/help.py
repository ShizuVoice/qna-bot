# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.send("Please enable direct messaging if you turned it off. I can't send you the help guide for this bot.")
        author = ctx.message.author

        embed = discord.Embed(
            colour = discord.Colour.dark_red()
        )

        embed.set_author(name='General Help')
        embed.add_field(name='ping', value='Respond with Pong!', inline=False)
        embed.add_field(name='say', value='Make the bot say with your input.', inline=False)
        embed.add_field(name='uptime', value='Shows how long the bot has been up for.', inline=False)
        embed.add_field(name='userinfo', value='Shows info of a mentioned user or yourself.')
        embed.add_field(name='version', value='Shows the bot version.', inline=False)

        await author.send(embed=embed)

        embed = discord.Embed(
            colour = discord.Colour.dark_red()
        )

        embed.set_author(name='Fun')
        embed.add_field(name='rps', value='Play rock, paper, scissor!', inline=False)
        embed.add_field(name='eightball', value='Ask the eightball for question.', inline=False)
        embed.add_field(name='haachama', value='Have some cooking tips from Akai Haato.', inline=False)

        await author.send(embed=embed)

        embed = discord.Embed(
            colour = discord.Colour.dark_red()
        )

        embed.set_author(name='Testpaper')
        embed.add_field(name='tphelp', value='Shows the testpaper help.')
        embed.add_field(name='testpaper', value='Sends the test question as a Direct Message.', inline=False)

        await author.send(embed=embed)

        embed = discord.Embed(
            colour = discord.Colour.dark_red()
        )

        embed.set_author(name='Moderation/Utility (Administrator/Owner only)')
        embed.add_field(name='kick', value='Kicks a member on the server.', inline=False)
        embed.add_field(name='ban', value='Bans a member on the server', inline=False)
        embed.add_field(name='purge', value='Clears messages with a certain amount.', inline=False)
        embed.add_field(name='status', value="Set the bot's online status.", inline=False)
        embed.add_field(name='shutdown', value='Shuts down the bot outside the terminal.', inline=False)

        await author.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))