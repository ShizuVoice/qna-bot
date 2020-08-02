# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

import discord, datetime
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_disconnect(self):
        consoletime = datetime.datetime.now()
        print(f"{consoletime} [WARNING] {self.bot.user.name} got disconnected! Attempting to reconnect...")

    @commands.Cog.listener()
    async def on_connect(self):
        consoletime = datetime.datetime.now()
        print(f"{consoletime} [INFO] {self.bot.user.name} successfully connected.")

#    @commands.Cog.listener()
#    async def on_message(self, message):
#        print(f"{message.author} said {message.content}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        consoletime = datetime.datetime.now()
        if isinstance(error, commands.CheckFailure):
            print(f"{consoletime} [WARNING] Admin command triggered but user didn't have enough permission to use it!")
            await ctx.send("You do not have permission to do that!")
        if isinstance(error, commands.CommandInvokeError):
            print(f"{consoletime} [WARNING] Bot doesn't have permission to do certain action. Check other roles that may be overriding the bot's own role permission.")
            await ctx.send("Bot doesn't have permission to do certain action. Check other roles that may be overriding the bot's own role permission.")
        if isinstance(error, commands.CommandNotFound):
            print(f"{consoletime} [INFO] User invoked the bot with non-existing command.")
            await ctx.send("Command doesn't exist. *Maybe you have typed it wrong, no?*")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))