from discord.ext import commands
import discord

class Extension():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commandName(self, ctx):
        await ctx.send

def setup(bot):
    bot.add_cog(Extension(bot))