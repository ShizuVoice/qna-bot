# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime, time
from discord.ext import commands

start_time = time.time()

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        message = await ctx.send('POG!')
        await message.edit(content='I mean PONG!')
#        await ctx.send('I mean PONG!')
    
    @commands.command()
    async def version(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.red()
        )

        embed.set_author(name='QnA Bot')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/712312095214927892/cb43c18459a8eda7fd37fadd0d59222f.png?size=256')
        embed.set_footer(text='Bot by SilentVOEZ')

        embed.add_field(name='Version', value='0.8.1 Beta')
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        await ctx.author.send("This feature is not available.")

    @commands.command()
    async def say(self, ctx, *, arg: commands.clean_content):
        await ctx.send(arg)
        await ctx.message.delete()

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Bot by SilentVOEZ")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Guild name:', value=member.display_name)

        embed.add_field(name='Created at:', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name='Top role:', value=member.top_role.mention)

        embed.add_field(name='Bot?', value=member.bot)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def die(self, ctx):
        await ctx.send('https://tenor.com/view/dancing-coffin-coffin-dance-funeral-funny-farewell-gif-16737844')

# Error handling
    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to delete a message. Check other roles that may be overriding the bot's own role permission.")

        raise error

def setup(bot):
    bot.add_cog(General(bot))
