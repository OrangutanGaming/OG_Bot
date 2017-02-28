from discord.ext import commands
import discord

class Giveaway():
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Giveaway(bot))