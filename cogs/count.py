from discord.ext import commands
import discord

class Count():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=["mcount"])
    async def msgcount(self, ctx, user: discord.Member = None, channel: discord.Channel = None):
        counter = 0
        tmp = await self.bot.say("Counting messages...")
        if not user:
            user = ctx.message.author
        if not channel:
            channel = ctx.message.channel
        async for log in self.bot.logs_from(channel, limit=100, before=ctx.message):
            if log.author == user:
                counter += 1
        self.bot.delete_message(ctx.message)
        if counter == 100:
            await self.bot.edit_message(tmp, "{} has at least {} messages in {}".format(user.mention, counter, channel.mention))
        elif counter <= 99:
            await self.bot.edit_message(tmp, "{} has {} messages in {}".format(user.mention, counter, channel.mention))
        else:
            await self.bot.edit_message(tmp, "Counter Bug")
    
    @commands.command(pass_context=True, aliases=["amcount"])
    async def amsgcount(self, ctx, channel: discord.Channel = None):
        counter = 0
        tmp = await self.bot.say("Counting messages...")
        if not channel:
            channel = ctx.message.channel
        async for log in self.bot.logs_from(channel, before=ctx.message):
            counter += 1
        self.bot.delete_message(ctx.message)
        if counter == 100:
            await self.bot.edit_message(tmp, "There are at least {} messages in {}".format(counter, channel.mention))
        elif counter <= 99:
            await self.bot.edit_message(tmp, "There are {} messages in {}".format(counter, channel.mention))
        else:
            await self.bot.edit_message(tmp, "Counter Bug")

def setup(bot):
    bot.add_cog(Count(bot))