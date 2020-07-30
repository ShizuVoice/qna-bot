# QnA Bot by SilentVOEZ#2523
# plugins (QnA Bot Py Extension)

# NOTICE: Events doesn't work for some reason.

import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        user = message.author
        msg = message.content
        print(f"{user} said {msg}")

def setup(bot):
    bot.add_cog(Events(bot))