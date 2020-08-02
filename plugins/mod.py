# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        consoletime = datetime.datetime.now()
        await member.send(f"You were kicked from the server by {ctx.author.mention}.\n Reason: {reason}")
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention}.\n Reason: {reason}")
        print(f"{consoletime} [INFO] User '{member.mention}' got kicked by '{ctx.author.mention}' with the reason of '{reason}'.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        consoletime = datetime.datetime.now()
        await member.send(f"You were banned from the server by {ctx.author.mention}.\n [{reason}]")
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention}.\n Reason: {reason}")
        print(f"{consoletime} [INFO] User '{member.mention}' got banned by '{ctx.author.mention}' with the reason of '{reason}'.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

# Dedicated error handling for this commands

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage is: `q!kick <User/ID> <Reason>`")
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found!")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to kick a member. Check other roles that may be overriding the bot's own role permission.")
        
        raise error

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage is: `q!ban <User/ID> <Reason>`")
        if isinstance(error, commands.BadArgument):
            await ctx.send("User not found!")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to ban a member. Check other roles that may be overriding the bot's own role permission.")

        raise error

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage is: `q!purge <amount>`")
        if isinstance(error, commands.BadArgument):
            await ctx.send("Not a number!")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!")
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("Bot doesn't have permission to delete a message. Check other roles that may be overriding the bot's own role permission.")

def setup(bot):
    bot.add_cog(Mod(bot))