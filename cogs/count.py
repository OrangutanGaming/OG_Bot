from discord.ext import commands
import discord

class Count():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mcount"])
    async def msgcount(self, ctx, user: discord.Member = None, channel: discord.TextChannel = None):
        counter = 0
        tmp = await ctx.send("Counting messages...")
        if not user:
            user = ctx.message.author
        if not channel:
            channel = ctx.message.channel
        async for log in channel.history(limit=100, before=ctx.message):
            if log.author == user:
                counter += 1
        await ctx.message.delete
        if counter == 100:
            await tmp.edit(content="{} has at least {} messages in {}".format(user, counter, channel.mention))
        elif counter <= 99:
            await tmp.edit(content="{} has {} messages in {}".format(user, counter, channel.mention))
        else:
            await tmp.edit(content="Counter Bug")
    
    @commands.command(aliases=["amcount"])
    async def amsgcount(self, ctx, channel: discord.TextChannel = None):
        counter = 0
        tmp = await ctx.send("Counting messages...")
        if not channel:
            channel = ctx.message.channel
        async for log in channel.history(before=ctx.message):
            counter += 1
        await ctx.message.delete
        if counter == 100:
            await tmp.edit(content="There are at least {} messages in {}".format(counter, channel.mention))
        elif counter <= 99:
            await tmp.edit(content="There are {} messages in {}".format(counter, channel.mention))
        else:
            await tmp.edit(content="Counter Bug")

    @commands.command(aliases=["recents", "last"])
    async def recent(self, ctx, user: discord.Member = None, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.message.channel
        if not user:
            user = ctx.message.author
        quote = None
        async for message in channel.history(before=ctx.message, limit=100):
            if message.author == user:
                quote = message
                embed = discord.Embed(description=quote.content)
                embed.set_author(name=quote.author.name, icon_url=quote.author.avatar_url)
                embed.timestamp = quote.timestamp
                await ctx.message.delete
                await ctx.send(embed=embed)
                return
            if not quote:
                continue

def setup(bot):
    bot.add_cog(Count(bot))