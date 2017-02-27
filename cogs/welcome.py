from discord.ext import commands
import discord

class Welcome():
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        await self.bot.send_message(member.server.default_channel, "{0.name} joined in {0.joined_at}".format(member))

def setup(bot):
    bot.add_cog(Welcome(bot))